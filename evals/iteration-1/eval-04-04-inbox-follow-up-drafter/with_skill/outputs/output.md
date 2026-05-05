# Functional Smoke Output: 04-inbox-follow-up-drafter

## Prompt

Draft a warm follow-up to a partner who asked for an update. I need to acknowledge the delay, say we are still working on it, and ask whether tomorrow morning is soon enough.

## Expected Output Shape

A recommended draft, optional softer version, subject line if email, and one-line reason the draft works.

## Smoke Verdict

PASS

## Why This Is A Useful Skill Test

This prompt is realistic enough to trigger the skill and specific enough to show whether the workflow, output contract, and safety boundaries are usable.

## Checks

- PASS: SKILL.md exists - skills/04-inbox-follow-up-drafter/SKILL.md
- PASS: Frontmatter includes name - job-to-ai-inbox-follow-up-drafter
- PASS: Frontmatter includes description - Use when someone needs a clear follow-up email, chat message, GoHighLevel message, or partner response drafted from thre
- PASS: Name is kebab-case and under 64 characters - name='job-to-ai-inbox-follow-up-drafter', length=33
- PASS: Description is specific and under 1024 characters - description length=259
- PASS: Includes  section - Found
- PASS: Includes Inputs section - Found
- PASS: Includes Workflow section - Found
- PASS: Includes Output section - Found
- PASS: Includes Safety section - Found
- PASS: Workflow starts with numbered steps - Found numbered workflow
- PASS: Safety section has at least three guardrails - guardrails=4
- PASS: No forbidden CMS wording in skill body - No hits
- PASS: Eval prompt is present and realistic - Draft a warm follow-up to a partner who asked for an update. I need to acknowledge the delay, say we are still working on it, and ask whether tomorrow morning i
- PASS: Eval expectations exist - The skill keeps follow-up output draft-only. The skill prevents unapproved promises. The output supports a softer version for sensitive topics.
