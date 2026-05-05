# Functional Smoke Output: 09-compliance-first-pass

## Prompt

Review this public copy before we post it: We guarantee faster approvals than anyone else and will get every customer the best possible rate.

## Expected Output Shape

Risk flags, why each item is risky, safer wording options, review-needed items, and publish-readiness note.

## Smoke Verdict

PASS

## Why This Is A Useful Skill Test

This prompt is realistic enough to trigger the skill and specific enough to show whether the workflow, output contract, and safety boundaries are usable.

## Checks

- PASS: SKILL.md exists - skills/09-compliance-first-pass/SKILL.md
- PASS: Frontmatter includes name - job-to-ai-compliance-first-pass
- PASS: Frontmatter includes description - Use when public-facing copy, recruiting material, sales content, ads, emails, landing pages, or social posts need a firs
- PASS: Name is kebab-case and under 64 characters - name='job-to-ai-compliance-first-pass', length=31
- PASS: Description is specific and under 1024 characters - description length=311
- PASS: Includes  section - Found
- PASS: Includes Inputs section - Found
- PASS: Includes Workflow section - Found
- PASS: Includes Output section - Found
- PASS: Includes Safety section - Found
- PASS: Workflow starts with numbered steps - Found numbered workflow
- PASS: Safety section has at least three guardrails - guardrails=4
- PASS: No forbidden CMS wording in skill body - No hits
- PASS: Eval prompt is present and realistic - Review this public copy before we post it: We guarantee faster approvals than anyone else and will get every customer the best possible rate.
- PASS: Eval expectations exist - The skill says it is not legal advice. The skill flags guarantees and broad comparison claims. The skill suggests safer wording instead of approving content.
