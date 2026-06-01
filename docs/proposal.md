# Final Project Proposal - Group: Pitch to Passport

---

> **NOTE FOR US**
>
> Martin's key points for the proposal:
> - Practice a structured approach to software development
> - Evaluate **feasibility before starting to program**
> - The **process is more important than the outcome** -> be realistic and convincing
> - An **individual reflection after group submission is mandatory** (submitted separately, not in this document)
> - 1-2 pages maximum
> (See Blackboard for more info under: Final Project Proposal)

---

**Course:** Basics of Software Development Practice SS 2026
**Department:** Z_GIS, University of Salzburg

**Group Members:**
- Max Elixhauser
- Emily Panzl

## Project Title

Pitch to Passport — A Women's Champions League Talent Map (? Map.. well its both CLI and Map)

## Description

> *Martin: Description of what you want to (try to) do*

...

Link to our Repo: https://github.com/Secreez/pitch-to-passport

### Overall Goal

> *Martin: the overall goal of your project (what should the software do)?*

...

### Feasibility & Known Risks

> **@Emily I suggest putting feasibility/risks here as its own subsection. Does that work for you?**

- The data is manually sourced from FBref rather than scraped, which is a conscious tradeoff to keep the scope realistic and avoid bot-protection issues.
- Emily: Some players appear twice in the dataset due to mid-season club transfers. This is a known data quirk that will be documented and handled in the cleaning step.
- **@Emily ... add any other data discrepancies you found here so far**

### Programming Paradigm & Approach

> *Martin: The programming paradigm and approach (object-oriented, procedural, external packages, ...)*

...

**External packages**

- `pandas` - data cleaning and analysis
- `folium` - interactive map generation
- `argparse` / `cmd` - CLI interface

### Milestones & Intermediate Steps

> *Martin: Intermediate steps and milestones*

1. ...
2. ...
3. ...
4. ...

## Learning Goals

> *Martin: your goals of what each of you wants to learn more about*

**Max:**
- **Data Cleaning with pandas** ... I'm very familiar with R when it comes to data cleaning (tidyverse/dplyr <3), but I have no clue about the "way of the pandas" nor am I a certified Pythonista. And I've quite literally dragged that along for years, even though I had Python in my Bachelor's Digitalization for a lot of ECTS. So... that's a big one. [HMM... MORE CONCRETE?]

- **Documentation & GitHub** structuring things properly is my bread and butter at work, explaining and selling things to stakeholders. But I want to get better at doing that specifically in a software development context. [HOW, WHAT EXACTLY? I ALREADY DO GITHUB / STAKEHOLDER DOCUMENTATION AND UNDERSTANDING + FEATURE TRIAGE FOR A LIVING. WHAT SPECIFICALLY IN SOFTWARE DEV?]

- **CLI development** I genuinely felt a spark of joy when we first touched argparse in class, (don't ask me for shit of why.). I want to spend a solid chunk of the ~25 hours diving deeper into building interactive CLI tools with `argparse` and `cmd`. [OKEH.. eh.]

**Emily:**

## Responsibilities

> *Martin: Include who in the group is responsible for what*

| Task | Responsible |
|------|-------------|
| Data cleaning (`format.py`) | Max |
| CLI logic (`main.py`) | Max |
| Repo structure & documentation | Max |
| Data analysis & validation | Emily |
| Football domain expertise | Emily |
| Map design (folium) | Emily |
| Proposal | Both |

- **@Emily - should we be more concretre here?**

## Deadline

> *Martin: When you plan to have it done: set your own deadline -> any time from July until end of August*

**Submission deadline: ...**

- **@Emily - .. August somethingsomething?**

## Effort Estimate

> *Martin: How much effort and resources will be required*

- **Time:** ~25 hours per person (~50 hours total)
- **Data:** Manually sourced from FBref (401 players, 2025-26 Women's CL season)
- **Tools:** Python, GitHub, IDE: VS Code (Emily) / Positron (Max)
- **@Emily - anything to add here?**