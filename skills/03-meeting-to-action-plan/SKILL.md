---
name: job-to-ai-meeting-to-action-plan
description: Use when someone wants to turn meeting notes, transcripts, or a rough recap into decisions, action items, owners, open questions, risks, and follow-up messages. Trigger on "meeting recap", "turn this meeting into action items", "what did we decide", or "make an action plan."
---

# Meeting To Action Plan

Convert meeting notes into clear next steps.

## Inputs

- Meeting notes or transcript
- Attendee list, if available
- Agenda, if available
- Desired audience for the recap

## Workflow

1. Identify decisions that were clearly made.
2. Identify action items, owners, and deadlines.
3. Mark missing owners or dates instead of guessing.
4. Separate risks, blockers, and unresolved questions.
5. Draft a concise follow-up message if useful.

## Output

Return:

- Decisions
- Action items
- Owners
- Deadlines
- Open questions
- Risks or blockers
- Optional follow-up message

## Safety

- Do not assign an owner unless the notes support it.
- Do not create a deadline unless one was stated.
- Do not include sensitive meeting details in public examples.
- Make uncertainty visible.

