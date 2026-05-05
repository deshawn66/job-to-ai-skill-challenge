---
name: job-to-ai-tool-workflow-brief
description: Use when a business leader wants a plain-English explanation of how tools, systems, or databases interact. Trigger on "explain this workflow", "how do these systems talk", "map this process", "Arive to GoHighLevel", "tool workflow", or "explain the data flow."
---

# Tool Workflow Brief

Explain business systems in plain English.

## Inputs

- Tool names
- What starts the workflow
- What should happen next
- Where the data should end up
- Known problem or question

## Workflow

1. Name each system and its job.
2. Explain the flow from start to finish.
3. Use a real-world analogy when the workflow is technical.
4. Identify where work can fail or stall.
5. Give the user the next checks in plain English.

## Output

Return:

- Plain-English workflow summary
- Step-by-step system flow
- Risk points
- What to check next
- Questions for a technical owner, if needed

## Safety

- Do not expose passwords, secret keys, or private configuration values.
- Do not recommend changing live production systems without review.
- Call the loan origination system Arive when discussing mortgage workflows.
- Call the customer follow-up system GoHighLevel or GHL when discussing that workflow.

