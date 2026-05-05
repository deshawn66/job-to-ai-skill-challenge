# Functional Smoke Output: 02-repeat-task-finder

## Prompt

Here is my task list from yesterday: meeting recap, report review, three email follow-ups, sales coaching prep, tool research, LinkedIn draft, team handoff, and updating a spreadsheet. Pick the 12 best AI skills from this.

## Expected Output Shape

A ranked list of skill candidates with job pain, input, output, safety boundary, and top 3 to build first.

## Smoke Verdict

PASS

## Why This Is A Useful Skill Test

This prompt is realistic enough to trigger the skill and specific enough to show whether the workflow, output contract, and safety boundaries are usable.

## Checks

- PASS: SKILL.md exists - skills/02-repeat-task-finder/SKILL.md
- PASS: Frontmatter includes name - job-to-ai-repeat-task-finder
- PASS: Frontmatter includes description - Use when someone has a task log or messy list of job duties and wants to identify the best tasks to automate or turn int
- PASS: Name is kebab-case and under 64 characters - name='job-to-ai-repeat-task-finder', length=28
- PASS: Description is specific and under 1024 characters - description length=281
- PASS: Includes  section - Found
- PASS: Includes Inputs section - Found
- PASS: Includes Workflow section - Found
- PASS: Includes Output section - Found
- PASS: Includes Safety section - Found
- PASS: Workflow starts with numbered steps - Found numbered workflow
- PASS: Safety section has at least three guardrails - guardrails=3
- PASS: No forbidden CMS wording in skill body - No hits
- PASS: Eval prompt is present and realistic - Here is my task list from yesterday: meeting recap, report review, three email follow-ups, sales coaching prep, tool research, LinkedIn draft, team handoff, and
- PASS: Eval expectations exist - The skill prioritizes repeated, structured, high-friction work. The skill avoids automating final human judgment. The output contract includes input, output, an
