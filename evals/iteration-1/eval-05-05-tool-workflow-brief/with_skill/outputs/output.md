# Functional Smoke Output: 05-tool-workflow-brief

## Prompt

Explain in plain English how Arive updates flow into our database and then into GoHighLevel for follow-up. I need the filing-cabinet version and the risk points.

## Expected Output Shape

Plain-English workflow summary, system flow, risk points, next checks, and technical-owner questions if needed.

## Smoke Verdict

PASS

## Why This Is A Useful Skill Test

This prompt is realistic enough to trigger the skill and specific enough to show whether the workflow, output contract, and safety boundaries are usable.

## Checks

- PASS: SKILL.md exists - skills/05-tool-workflow-brief/SKILL.md
- PASS: Frontmatter includes name - job-to-ai-tool-workflow-brief
- PASS: Frontmatter includes description - Use when a business leader wants a plain-English explanation of how tools, systems, or databases interact. Trigger on "e
- PASS: Name is kebab-case and under 64 characters - name='job-to-ai-tool-workflow-brief', length=29
- PASS: Description is specific and under 1024 characters - description length=260
- PASS: Includes  section - Found
- PASS: Includes Inputs section - Found
- PASS: Includes Workflow section - Found
- PASS: Includes Output section - Found
- PASS: Includes Safety section - Found
- PASS: Workflow starts with numbered steps - Found numbered workflow
- PASS: Safety section has at least three guardrails - guardrails=4
- PASS: No forbidden CMS wording in skill body - No hits
- PASS: Eval prompt is present and realistic - Explain in plain English how Arive updates flow into our database and then into GoHighLevel for follow-up. I need the filing-cabinet version and the risk points
- PASS: Eval expectations exist - The skill uses Arive by name. The skill uses GoHighLevel or GHL by name. The skill avoids exposing passwords, secrets, or private configuration values.
