# Functional Smoke Output: 01-daily-work-capture

## Prompt

I had a messy operator day: reviewed a weekly report, answered five team questions, joined two meetings, researched an AI tool, wrote a handoff, and forgot to log two follow-ups. Turn this into a task log and tell me what could become skills.

## Expected Output Shape

A categorized task table with work type, automation potential, and best skill candidates.

## Smoke Verdict

PASS

## Why This Is A Useful Skill Test

This prompt is realistic enough to trigger the skill and specific enough to show whether the workflow, output contract, and safety boundaries are usable.

## Checks

- PASS: SKILL.md exists - skills/01-daily-work-capture/SKILL.md
- PASS: Frontmatter includes name - job-to-ai-daily-work-capture
- PASS: Frontmatter includes description - Use when someone wants to turn rough notes from one real workday into a clean task log for AI skill discovery. Trigger o
- PASS: Name is kebab-case and under 64 characters - name='job-to-ai-daily-work-capture', length=28
- PASS: Description is specific and under 1024 characters - description length=285
- PASS: Includes  section - Found
- PASS: Includes Inputs section - Found
- PASS: Includes Workflow section - Found
- PASS: Includes Output section - Found
- PASS: Includes Safety section - Found
- PASS: Workflow starts with numbered steps - Found numbered workflow
- PASS: Safety section has at least three guardrails - guardrails=3
- PASS: No forbidden CMS wording in skill body - No hits
- PASS: Eval prompt is present and realistic - I had a messy operator day: reviewed a weekly report, answered five team questions, joined two meetings, researched an AI tool, wrote a handoff, and forgot to l
- PASS: Eval expectations exist - The skill has required YAML frontmatter with name and description. The skill defines Inputs, Workflow, Output, and Safety sections. The expected output asks for
