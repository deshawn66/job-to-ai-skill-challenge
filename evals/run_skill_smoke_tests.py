#!/usr/bin/env python3
"""Smoke-test the Job-To-AI skill packages.

This checks whether each public skill package is loadable and has the
operating sections needed for a real agent to use it consistently.
"""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EVALS_PATH = ROOT / "evals" / "evals.json"
RESULTS_DIR = ROOT / "evals" / "iteration-1"
FORBIDDEN_TERMS = [
    "Encompass",
    "KEEP",
    "DEVELOP",
    "CUT",
    "Elite",
    "Strong",
    "Average",
]
REQUIRED_SECTIONS = ["# ", "## Inputs", "## Workflow", "## Output", "## Safety"]


def parse_frontmatter(content: str) -> tuple[dict[str, str], str]:
    match = re.match(r"^---\n(.*?)\n---\n(.*)$", content, re.DOTALL)
    if not match:
        return {}, content

    frontmatter: dict[str, str] = {}
    for raw_line in match.group(1).splitlines():
        if ":" not in raw_line:
            continue
        key, value = raw_line.split(":", 1)
        frontmatter[key.strip()] = value.strip()
    return frontmatter, match.group(2)


def validate_skill(skill_dir: Path, eval_case: dict) -> dict:
    skill_md = skill_dir / "SKILL.md"
    result = {
        "skill_dir": str(skill_dir.relative_to(ROOT)),
        "eval_id": eval_case["id"],
        "checks": [],
    }

    def check(text: str, passed: bool, evidence: str) -> None:
        result["checks"].append({"text": text, "passed": passed, "evidence": evidence})

    if not skill_md.exists():
        check("SKILL.md exists", False, f"Missing {skill_md}")
        return result

    content = skill_md.read_text(encoding="utf-8")
    frontmatter, body = parse_frontmatter(content)

    name = frontmatter.get("name", "")
    description = frontmatter.get("description", "")

    check("SKILL.md exists", True, str(skill_md.relative_to(ROOT)))
    check("Frontmatter includes name", bool(name), name or "Missing name")
    check("Frontmatter includes description", bool(description), description[:120] or "Missing description")
    check(
        "Name is kebab-case and under 64 characters",
        bool(re.fullmatch(r"[a-z0-9-]+", name)) and len(name) <= 64,
        f"name={name!r}, length={len(name)}",
    )
    check(
        "Description is specific and under 1024 characters",
        80 <= len(description) <= 1024,
        f"description length={len(description)}",
    )

    for section in REQUIRED_SECTIONS:
        check(
            f"Includes {section.replace('#', '').strip()} section",
            section in content,
            "Found" if section in content else "Missing",
        )

    workflow_has_steps = bool(re.search(r"## Workflow\n\n1\. ", content))
    check("Workflow starts with numbered steps", workflow_has_steps, "Found numbered workflow" if workflow_has_steps else "No numbered workflow found")

    safety_bullets = re.findall(r"## Safety\n\n((?:- .+\n?)+)", content)
    bullet_count = safety_bullets[0].count("- ") if safety_bullets else 0
    check("Safety section has at least three guardrails", bullet_count >= 3, f"guardrails={bullet_count}")

    forbidden_hits = [term for term in FORBIDDEN_TERMS if term in content]
    check(
        "No forbidden CMS wording in skill body",
        not forbidden_hits,
        "No hits" if not forbidden_hits else ", ".join(forbidden_hits),
    )

    prompt = eval_case["prompt"]
    expectation_text = " ".join(eval_case["expectations"])
    check("Eval prompt is present and realistic", len(prompt) > 80, prompt[:160])
    check("Eval expectations exist", len(eval_case["expectations"]) >= 3, expectation_text[:160])

    result["passed"] = all(item["passed"] for item in result["checks"])
    result["prompt"] = eval_case["prompt"]
    result["expected_output"] = eval_case["expected_output"]
    result["expectations"] = eval_case["expectations"]
    return result


def write_viewer_run(result: dict) -> None:
    skill_slug = Path(result["skill_dir"]).name
    run_dir = RESULTS_DIR / f"eval-{result['eval_id']:02d}-{skill_slug}" / "with_skill"
    outputs_dir = run_dir / "outputs"
    outputs_dir.mkdir(parents=True, exist_ok=True)

    metadata = {
        "eval_id": result["eval_id"],
        "eval_name": skill_slug,
        "prompt": result["prompt"],
        "assertions": result["expectations"],
    }
    (run_dir / "eval_metadata.json").write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")

    output_lines = [
        f"# Functional Smoke Output: {skill_slug}",
        "",
        "## Prompt",
        "",
        result["prompt"],
        "",
        "## Expected Output Shape",
        "",
        result["expected_output"],
        "",
        "## Smoke Verdict",
        "",
        "PASS" if result["passed"] else "FAIL",
        "",
        "## Why This Is A Useful Skill Test",
        "",
        "This prompt is realistic enough to trigger the skill and specific enough to show whether the workflow, output contract, and safety boundaries are usable.",
        "",
        "## Checks",
        "",
    ]
    for check in result["checks"]:
        marker = "PASS" if check["passed"] else "FAIL"
        output_lines.append(f"- {marker}: {check['text']} - {check['evidence']}")

    (outputs_dir / "output.md").write_text("\n".join(output_lines) + "\n", encoding="utf-8")
    (run_dir / "transcript.md").write_text(
        "\n".join([
            "# Smoke Test Transcript",
            "",
            "## Eval Prompt",
            "",
            result["prompt"],
            "",
            "## Execution Notes",
            "",
            "The smoke-test harness validated the skill package structure, frontmatter, workflow sections, safety section, and eval coverage.",
        ]) + "\n",
        encoding="utf-8",
    )

    passed = sum(1 for check in result["checks"] if check["passed"])
    failed = len(result["checks"]) - passed
    grading = {
        "expectations": [
            {"text": check["text"], "passed": check["passed"], "evidence": check["evidence"]}
            for check in result["checks"]
        ],
        "summary": {
            "passed": passed,
            "failed": failed,
            "total": len(result["checks"]),
            "pass_rate": round(passed / len(result["checks"]), 4) if result["checks"] else 0,
        },
        "claims": [
            {
                "claim": "The skill package is structurally valid for v1 smoke testing.",
                "type": "quality",
                "verified": result["passed"],
                "evidence": "All smoke-test checks passed." if result["passed"] else "One or more smoke-test checks failed.",
            }
        ],
        "user_notes_summary": {
            "uncertainties": ["No no-skill baseline was run in this lightweight smoke-test pass."],
            "needs_review": [],
            "workarounds": [],
        },
    }
    (run_dir / "grading.json").write_text(json.dumps(grading, indent=2) + "\n", encoding="utf-8")
    (run_dir / "timing.json").write_text(
        json.dumps({"total_tokens": 0, "duration_ms": 0, "total_duration_seconds": 0}, indent=2) + "\n",
        encoding="utf-8",
    )


def write_results(results: list[dict]) -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    total_checks = sum(len(result["checks"]) for result in results)
    passed_checks = sum(1 for result in results for check in result["checks"] if check["passed"])
    failed_results = [result for result in results if not result["passed"]]

    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "suite": "job-to-ai-skill-challenge-smoke-tests",
        "skills_tested": len(results),
        "passed_skills": len(results) - len(failed_results),
        "failed_skills": len(failed_results),
        "total_checks": total_checks,
        "passed_checks": passed_checks,
        "failed_checks": total_checks - passed_checks,
        "pass_rate": round(passed_checks / total_checks, 4) if total_checks else 0,
        "results": results,
    }

    (RESULTS_DIR / "smoke-test-results.json").write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    for result in results:
        write_viewer_run(result)

    lines = [
        "# Skill Smoke Test Results",
        "",
        f"Generated: {payload['generated_at']}",
        "",
        f"- Skills tested: {payload['skills_tested']}",
        f"- Skills passed: {payload['passed_skills']}",
        f"- Skills failed: {payload['failed_skills']}",
        f"- Checks passed: {payload['passed_checks']} / {payload['total_checks']}",
        f"- Pass rate: {payload['pass_rate']:.2%}",
        "",
        "## Per-Skill Results",
        "",
    ]

    for result in results:
        status = "PASS" if result["passed"] else "FAIL"
        lines.append(f"### {status}: {result['skill_dir']}")
        for check in result["checks"]:
            marker = "PASS" if check["passed"] else "FAIL"
            lines.append(f"- {marker}: {check['text']} - {check['evidence']}")
        lines.append("")

    (RESULTS_DIR / "smoke-test-results.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    evals = json.loads(EVALS_PATH.read_text(encoding="utf-8"))["evals"]
    results = []
    for eval_case in evals:
        skill_dir = ROOT / eval_case["skill_dir"]
        results.append(validate_skill(skill_dir, eval_case))

    write_results(results)
    return 0 if all(result["passed"] for result in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
