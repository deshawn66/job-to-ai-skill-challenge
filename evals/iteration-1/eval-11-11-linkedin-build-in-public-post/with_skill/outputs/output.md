# Functional Smoke Output: 11-linkedin-build-in-public-post

## Prompt

Write the LinkedIn post for launching this project: I tracked one workday, turned it into 12 AI skills, published the GitHub repo, and built the landing page.

## Expected Output Shape

A ready-to-post LinkedIn draft with hook, problem, action, lesson, and question.

## Smoke Verdict

PASS

## Why This Is A Useful Skill Test

This prompt is realistic enough to trigger the skill and specific enough to show whether the workflow, output contract, and safety boundaries are usable.

## Checks

- PASS: SKILL.md exists - skills/11-linkedin-build-in-public-post/SKILL.md
- PASS: Frontmatter includes name - job-to-ai-linkedin-build-in-public-post
- PASS: Frontmatter includes description - Use when someone wants to turn real work, a shipped artifact, a GitHub repo, a portfolio page, a tool review, or an AI e
- PASS: Name is kebab-case and under 64 characters - name='job-to-ai-linkedin-build-in-public-post', length=39
- PASS: Description is specific and under 1024 characters - description length=297
- PASS: Includes  section - Found
- PASS: Includes Inputs section - Found
- PASS: Includes Workflow section - Found
- PASS: Includes Output section - Found
- PASS: Includes Safety section - Found
- PASS: Workflow starts with numbered steps - Found numbered workflow
- PASS: Safety section has at least three guardrails - guardrails=4
- PASS: No forbidden CMS wording in skill body - No hits
- PASS: Eval prompt is present and realistic - Write the LinkedIn post for launching this project: I tracked one workday, turned it into 12 AI skills, published the GitHub repo, and built the landing page.
- PASS: Eval expectations exist - The skill requires a specific closing question. The style section avoids emojis, em dashes, filler, and unexplained jargon. The safety section prevents exaggera
