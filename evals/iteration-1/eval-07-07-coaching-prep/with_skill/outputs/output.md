# Functional Smoke Output: 07-coaching-prep

## Prompt

Prepare me for a coaching conversation with a sales professional who is below goal but improved activity over the last two weeks. I want to encourage the effort and set a clear next standard.

## Expected Output Shape

Conversation goal, affirmations, challenge, questions, next commitment, and optional opening script.

## Smoke Verdict

PASS

## Why This Is A Useful Skill Test

This prompt is realistic enough to trigger the skill and specific enough to show whether the workflow, output contract, and safety boundaries are usable.

## Checks

- PASS: SKILL.md exists - skills/07-coaching-prep/SKILL.md
- PASS: Frontmatter includes name - job-to-ai-coaching-prep
- PASS: Frontmatter includes description - Use when a manager, founder, or sales leader needs to prepare for a coaching conversation, performance conversation, or 
- PASS: Name is kebab-case and under 64 characters - name='job-to-ai-coaching-prep', length=23
- PASS: Description is specific and under 1024 characters - description length=294
- PASS: Includes  section - Found
- PASS: Includes Inputs section - Found
- PASS: Includes Workflow section - Found
- PASS: Includes Output section - Found
- PASS: Includes Safety section - Found
- PASS: Workflow starts with numbered steps - Found numbered workflow
- PASS: Safety section has at least three guardrails - guardrails=4
- PASS: No forbidden CMS wording in skill body - No hits
- PASS: Eval prompt is present and realistic - Prepare me for a coaching conversation with a sales professional who is below goal but improved activity over the last two weeks. I want to encourage the effort
- PASS: Eval expectations exist - The skill keeps the tone direct and respectful. The skill includes affirm and challenge sections. The safety section prevents personal diagnosis.
