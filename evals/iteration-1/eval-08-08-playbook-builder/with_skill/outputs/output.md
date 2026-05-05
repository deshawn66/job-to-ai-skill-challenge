# Functional Smoke Output: 08-playbook-builder

## Prompt

Build a practical playbook for following up with past customers after a market update. Audience is sales professionals. Keep it motivating and simple.

## Expected Output Shape

Title, goal, audience, when to use it, steps, examples, common mistakes, and checklist.

## Smoke Verdict

PASS

## Why This Is A Useful Skill Test

This prompt is realistic enough to trigger the skill and specific enough to show whether the workflow, output contract, and safety boundaries are usable.

## Checks

- PASS: SKILL.md exists - skills/08-playbook-builder/SKILL.md
- PASS: Frontmatter includes name - job-to-ai-playbook-builder
- PASS: Frontmatter includes description - Use when someone wants to turn a repeatable business process, sales motion, training topic, or operating habit into a pr
- PASS: Name is kebab-case and under 64 characters - name='job-to-ai-playbook-builder', length=26
- PASS: Description is specific and under 1024 characters - description length=270
- PASS: Includes  section - Found
- PASS: Includes Inputs section - Found
- PASS: Includes Workflow section - Found
- PASS: Includes Output section - Found
- PASS: Includes Safety section - Found
- PASS: Workflow starts with numbered steps - Found numbered workflow
- PASS: Safety section has at least three guardrails - guardrails=4
- PASS: No forbidden CMS wording in skill body - No hits
- PASS: Eval prompt is present and realistic - Build a practical playbook for following up with past customers after a market update. Audience is sales professionals. Keep it motivating and simple.
- PASS: Eval expectations exist - The skill turns a process into steps. The skill includes examples and common mistakes. The safety section flags unsupported or regulated claims.
