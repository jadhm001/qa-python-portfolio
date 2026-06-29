# AI Test Strategy v1
### Consistency & Quality Evaluation of LLM Outputs

**Author:** Manisha Jadhav
**Purpose:** Personal practice applying QA principles to evaluating LLM (AI) outputs — exploring how traditional testing thinking maps to non-deterministic AI systems.

---

## Exercise 1 — Consistency Testing (Open-Ended Prompt)

**Feature tested:** Text generation
**Prompt:** "In one sentence, what is the most important thing to know about software testing?"
**Method:** Same prompt run 5 times, no changes between runs.

**Observations:**
- Responses varied in wording and angle across all 5 runs
- Thematic drift observed — focus shifted between "testing reveals defects" and "testing can't guarantee bug-free software"
- No response was factually wrong or misleading
- No single response was definitive on its own — but a pattern emerged across the set

**Conclusion:** For open-ended/subjective prompts, the model produces *thematically related but non-identical* outputs. Single-run testing is insufficient — multiple runs (ensemble evaluation) are needed to identify the true underlying answer.

---

## Exercise 2 — Scored Quality Evaluation (Factual Prompt)

**Feature tested:** Text generation
**Prompt:** "In 2 sentences, explain the difference between a defect and a risk in software testing."
**Method:** Same prompt run 3 times. Each run scored 1–5 on Accuracy and Clarity.

**Results:**

| Run | Accuracy | Clarity |
|-----|----------|---------|
| 1   | 5        | 5       |
| 2   | 5        | 4       |
| 3   | 5        | 4       |

**Consistency across runs:** 5/5

**Observation:** Definitions were consistent in meaning across all runs — only rephrased, not substantively different. Accuracy remained perfect; clarity had minor variation.

**Conclusion:** For factual/definitional prompts, the model is highly stable. Variation is lexical (wording) only, not semantic (meaning).

---

## Key Finding: Prompt Type Affects Output Stability

| Prompt Type | Example | Stability Observed |
|---|---|---|
| Open-ended / subjective | "Most important thing about testing" | Moderate thematic drift |
| Factual / definitional | "Defect vs. risk" | High consistency, wording-only variation |

**Implication for AI QA strategy:**
- Factual, compliance-related, or safety-critical outputs require **strict consistency testing** — drift here is high-risk
- Open-ended or creative outputs can tolerate more variation — lower testing rigor is acceptable
- A production-grade eval framework should **classify prompts by type first**, then define pass/fail criteria appropriate to that type — not a single one-size-fits-all standard

---

## Recommended Approach for a Production Eval Framework

1. Define acceptable output criteria *before* testing (not after seeing results)
2. Run a minimum of 3–5 iterations per test case — single-run testing is not reliable for non-deterministic systems
3. Evaluate against defined criteria and intended meaning, not exact string matching
4. Classify prompts/features by risk type (factual vs. open-ended) and apply matching rigor
5. Flag any response that drifts outside the acceptable theme or introduces inaccurate information
6. Track consistency scores over time — especially after model or prompt updates (regression risk)

---

## Why This Matters

Traditional QA assumes deterministic systems: same input → same output, every time. AI systems break that assumption. The job of AI QA is not to "prove" the AI is right every time — it's to define what *good enough, consistent, and safe* looks like, and build repeatable ways to measure against that bar.

This is the same quality mindset applied to manual and automated testing for 15+ years — applied to a new kind of system.

---

*Document version 1 — based on initial hands-on eval exercises. To be expanded with additional prompt types, edge cases, and structured eval tooling as learning continues.*
