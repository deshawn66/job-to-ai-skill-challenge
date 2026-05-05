# Functional Smoke Output: 03-meeting-to-action-plan

## Prompt

Turn these meeting notes into a clear action plan: Maria owns the report review, James is checking partner follow-up, we agreed the training needs a pilot, and nobody picked a date for the dashboard fix.

## Expected Output Shape

Decisions, action items, owners, deadlines, open questions, risks, and optional follow-up message.

## Smoke Verdict

PASS

## Why This Is A Useful Skill Test

This prompt is realistic enough to trigger the skill and specific enough to show whether the workflow, output contract, and safety boundaries are usable.

## Checks

- PASS: SKILL.md exists - skills/03-meeting-to-action-plan/SKILL.md
- PASS: Frontmatter includes name - job-to-ai-meeting-to-action-plan
- PASS: Frontmatter includes description - Use when someone wants to turn meeting notes, transcripts, or a rough recap into decisions, action items, owners, open q
- PASS: Name is kebab-case and under 64 characters - name='job-to-ai-meeting-to-action-plan', length=32
- PASS: Description is specific and under 1024 characters - description length=275
- PASS: Includes  section - Found
- PASS: Includes Inputs section - Found
- PASS: Includes Workflow section - Found
- PASS: Includes Output section - Found
- PASS: Includes Safety section - Found
- PASS: Workflow starts with numbered steps - Found numbered workflow
- PASS: Safety section has at least three guardrails - guardrails=4
- PASS: No forbidden CMS wording in skill body - No hits
- PASS: Eval prompt is present and realistic - Turn these meeting notes into a clear action plan: Maria owns the report review, James is checking partner follow-up, we agreed the training needs a pilot, and 
- PASS: Eval expectations exist - The skill tells the assistant not to invent owners. The skill tells the assistant not to invent deadlines. The output separates decisions, action items, and ope
