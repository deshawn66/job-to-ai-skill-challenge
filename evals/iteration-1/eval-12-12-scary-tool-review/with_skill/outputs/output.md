# Functional Smoke Output: 12-scary-tool-review

## Prompt

I tried OpenClaw for two hours. Setup was confusing, but I can see how local agents could control files and workflows. Turn this into an honest field report for non-technical operators.

## Expected Output Shape

Field report with confusion, surprises, what worked, what failed, what feels powerful, what is too early, and recommendation.

## Smoke Verdict

PASS

## Why This Is A Useful Skill Test

This prompt is realistic enough to trigger the skill and specific enough to show whether the workflow, output contract, and safety boundaries are usable.

## Checks

- PASS: SKILL.md exists - skills/12-scary-tool-review/SKILL.md
- PASS: Frontmatter includes name - job-to-ai-scary-tool-review
- PASS: Frontmatter includes description - Use when someone tries an intimidating, technical, experimental, local, or frontier AI tool and wants an honest field re
- PASS: Name is kebab-case and under 64 characters - name='job-to-ai-scary-tool-review', length=27
- PASS: Description is specific and under 1024 characters - description length=301
- PASS: Includes  section - Found
- PASS: Includes Inputs section - Found
- PASS: Includes Workflow section - Found
- PASS: Includes Output section - Found
- PASS: Includes Safety section - Found
- PASS: Workflow starts with numbered steps - Found numbered workflow
- PASS: Safety section has at least three guardrails - guardrails=4
- PASS: No forbidden CMS wording in skill body - No hits
- PASS: Eval prompt is present and realistic - I tried OpenClaw for two hours. Setup was confusing, but I can see how local agents could control files and workflows. Turn this into an honest field report for
- PASS: Eval expectations exist - The skill separates setup friction from product value. The skill does not pretend early tools are production-ready. The safety section warns against connecting 
