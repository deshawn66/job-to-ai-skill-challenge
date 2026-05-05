---
name: job-to-ai-scorecard-explainer
description: Use when someone needs a report, dashboard, scorecard, spreadsheet, or metric snapshot translated into plain-English insights and recommended actions. Trigger on "explain this report", "what do these numbers mean", "scorecard summary", "dashboard insight", or "turn this data into action."
---

# Scorecard Explainer

Turn numbers into business insight.

## Inputs

- Report, table, dashboard text, or metric summary
- Time period
- Audience
- Metric definitions, if available
- Decision the report should support

## Workflow

1. Identify the headline insight.
2. Pull out the three most important supporting points.
3. Explain changes, risks, and bright spots.
4. Translate metrics into what the audience should do next.
5. Flag any number that cannot be explained from the provided data.

## Output

Return:

- Headline
- Three key insights
- What changed
- What needs attention
- Recommended next action
- Unknowns or data gaps

## Safety

- Do not invent reasons behind the numbers.
- Do not shame individual performers.
- Do not expose private employee, customer, or borrower data publicly.
- If the source data is incomplete, say so.

