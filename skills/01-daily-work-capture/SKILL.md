---
name: job-to-ai-daily-work-capture
description: Use when someone wants to turn rough notes from one real workday into a clean task log for AI skill discovery. Trigger on requests like "track my workday", "turn my day into tasks", "what did I do today", "find automation opportunities from my day", or "document my job for AI skills."
---

# Daily Work Capture

Turn a messy workday into a structured task log.

## Inputs

- Rough workday notes
- Calendar or meeting notes
- Email or message highlights
- Completed tasks
- Decisions made
- Follow-ups sent or received

## Workflow

1. Extract only work the user actually mentioned.
2. Group tasks into meetings, follow-ups, reports, decisions, research, handoffs, admin, and repeat questions.
3. Mark each task as repeatable, judgment-heavy, research-heavy, admin-heavy, or relationship-heavy.
4. Add an automation-potential rating: low, medium, or high.
5. Flag missing context only when it changes the usefulness of the task log.

## Output

Return a table with:

- Task
- Category
- Work type
- Repeats how often
- Automation potential
- Notes

Then add a short "best skill candidates" list.

## Safety

- Do not invent work the user did not mention.
- Do not include private names, customer data, borrower data, or employee-sensitive details unless the user explicitly asks.
- If the output is public-facing, sanitize all examples.

