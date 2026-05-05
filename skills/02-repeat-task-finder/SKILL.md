---
name: job-to-ai-repeat-task-finder
description: Use when someone has a task log or messy list of job duties and wants to identify the best tasks to automate or turn into AI skills. Trigger on "what should I automate", "find repeatable tasks", "choose my 12 skills", "turn this workday into skill ideas", or "AI skill candidates."
---

# Repeat Task Finder

Find the work that is worth turning into reusable AI skills.

## Inputs

- Workday task log
- Rough list of responsibilities
- Known pain points
- Time estimates, if available
- Frequency notes, if available

## Workflow

1. Read the task list and remove one-off tasks that are not likely to repeat.
2. Prioritize work that repeats, takes mental energy, follows a similar structure, delays decisions, or creates handoff friction.
3. Avoid recommending tasks where AI would own final judgment, approval, or sensitive communication.
4. Pick the strongest 12 skill ideas.
5. For each skill idea, define job pain, audience, input, output, tool touchpoints, and safety boundary.

## Output

Return:

- Ranked list of 12 skill candidates
- One-sentence reason each candidate is worth building
- Input and output for each candidate
- Safety boundary for each candidate
- Top 3 to build first

## Safety

- Do not recommend automation that sends, approves, deletes, pays, or changes records without human review.
- Do not treat sensitive personal or customer judgment as fully automatable.
- If evidence is thin, say which recommendations are assumptions.

