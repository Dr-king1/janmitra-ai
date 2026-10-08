# JanMitra AI — From Eligibility to Action

JanMitra AI is a citizen-benefit navigation prototype that helps people discover potentially relevant government schemes, understand why they may be relevant, prepare required documents, and identify the next official action.

## Problem

Many citizens may be eligible for government schemes but face difficulty in:

- discovering relevant schemes
- understanding eligibility conditions
- knowing which documents are required
- identifying the correct next step
- navigating complex government information

JanMitra AI focuses on this last-mile information gap.

## Solution

JanMitra AI uses a citizen profile and a small verified/sample scheme database to identify potentially relevant benefits.

The prototype follows:

**Find → Understand → Prepare → Act**

For each potentially relevant benefit, the system provides:

- Benefit name and category
- Why the benefit may be relevant
- Documents to prepare
- Suggested next official action
- Eligibility disclaimer

JanMitra does not make the final eligibility decision. Final eligibility is determined by the concerned government authority.

## Prototype Flow

1. Citizen enters age, state, monthly income and citizen type.
2. The eligibility engine checks the profile against available scheme rules.
3. Potentially relevant benefits are displayed.
4. The system explains why a benefit may be relevant.
5. Required documents are shown.
6. The user receives a suggested next official action.

## Technical Architecture

```text
Citizen Profile
      ↓
Input Validation
      ↓
Eligibility / Rule Engine
      ↓
Scheme & Benefit Data
      ↓
Potentially Relevant Benefits
      ↓
Explainability
      ↓
Documents to Prepare
      ↓
Next Official Action
