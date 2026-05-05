# Functional Smoke Output: 06-scorecard-explainer

## Prompt

Explain this scorecard for a sales team: 12 people are above goal, 8 are close, 5 are behind, and we need to decide where coaching goes next.

## Expected Output Shape

Headline, three insights, what changed, what needs attention, recommended next action, and data gaps.

## Smoke Verdict

PASS

## Why This Is A Useful Skill Test

This prompt is realistic enough to trigger the skill and specific enough to show whether the workflow, output contract, and safety boundaries are usable.

## Checks

- PASS: SKILL.md exists - skills/06-scorecard-explainer/SKILL.md
- PASS: Frontmatter includes name - job-to-ai-scorecard-explainer
- PASS: Frontmatter includes description - Use when someone needs a report, dashboard, scorecard, spreadsheet, or metric snapshot translated into plain-English ins
- PASS: Name is kebab-case and under 64 characters - name='job-to-ai-scorecard-explainer', length=29
- PASS: Description is specific and under 1024 characters - description length=289
- PASS: Includes  section - Found
- PASS: Includes Inputs section - Found
- PASS: Includes Workflow section - Found
- PASS: Includes Output section - Found
- PASS: Includes Safety section - Found
- PASS: Workflow starts with numbered steps - Found numbered workflow
- PASS: Safety section has at least three guardrails - guardrails=4
- PASS: No forbidden CMS wording in skill body - No hits
- PASS: Eval prompt is present and realistic - Explain this scorecard for a sales team: 12 people are above goal, 8 are close, 5 are behind, and we need to decide where coaching goes next.
- PASS: Eval expectations exist - The skill tells the assistant not to invent causes behind numbers. The skill translates metrics into action. The output includes unknowns or data gaps.
