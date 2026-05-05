# Functional Smoke Output: 10-founder-research-and-feedback

## Prompt

I tried an AI sales follow-up startup. It wrote fast drafts but had no approval step and did not understand regulated sales language. Turn this into a scorecard and founder message.

## Expected Output Shape

Product summary, useful parts, hype or weak spots, missing workflow pieces, would-pay-if condition, and founder message.

## Smoke Verdict

PASS

## Why This Is A Useful Skill Test

This prompt is realistic enough to trigger the skill and specific enough to show whether the workflow, output contract, and safety boundaries are usable.

## Checks

- PASS: SKILL.md exists - skills/10-founder-research-and-feedback/SKILL.md
- PASS: Frontmatter includes name - job-to-ai-founder-research-and-feedback
- PASS: Frontmatter includes description - Use when someone is testing an AI startup, researching "AI for my job" tools, comparing products, forming a public opini
- PASS: Name is kebab-case and under 64 characters - name='job-to-ai-founder-research-and-feedback', length=39
- PASS: Description is specific and under 1024 characters - description length=298
- PASS: Includes  section - Found
- PASS: Includes Inputs section - Found
- PASS: Includes Workflow section - Found
- PASS: Includes Output section - Found
- PASS: Includes Safety section - Found
- PASS: Workflow starts with numbered steps - Found numbered workflow
- PASS: Safety section has at least three guardrails - guardrails=4
- PASS: No forbidden CMS wording in skill body - No hits
- PASS: Eval prompt is present and realistic - I tried an AI sales follow-up startup. It wrote fast drafts but had no approval step and did not understand regulated sales language. Turn this into a scorecard
- PASS: Eval expectations exist - The skill separates useful, hype, missing, and worth-paying-for. The skill drafts specific respectful founder feedback. The safety section prevents claiming unt
