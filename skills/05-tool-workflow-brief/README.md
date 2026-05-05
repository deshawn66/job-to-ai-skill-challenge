# Skill 05: Tool Workflow Brief

## What It Does

Explains how one business tool interacts with another in plain English.

## Who It Helps

Business leaders who need to understand systems without reading technical docs.

## Inputs Needed

- Tool names
- What each tool is supposed to do
- Where the workflow starts
- Where the data should end up
- Known problem or question

## Tools It May Interact With

- Arive
- GoHighLevel
- Supabase
- Airtable
- Zapier
- Internal dashboards

## Prompt

Explain this workflow in plain English. Use a filing cabinet or phone-call analogy if helpful. Show where the work starts, what system receives it, what can go wrong, and what a non-technical leader should check next. Avoid jargon unless you explain it.

## Sample Input

Arive sends loan updates to an internal database. Some updates also need to reach GoHighLevel for follow-up. I need to understand the flow and the risk points.

## Sample Output

Plain-English version:

Arive is the source system. It is where the loan activity starts.

The database is the filing cabinet. It stores the clean record so reports and dashboards can use it.

GoHighLevel is the follow-up system. It should only receive the right updates after the record is clean.

Risk points:

- The update may not leave Arive.
- The database may receive it but not process it.
- GoHighLevel may reject it or create the wrong follow-up.

## Safety Notes

- Do not expose passwords or secret keys.
- Do not recommend changing live production systems without review.
- Do not call Arive by any other system name.

