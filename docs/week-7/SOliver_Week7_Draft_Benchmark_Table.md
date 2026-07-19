# Week 7 — Draft Benchmark Table (Interim Submission)

**Student:** Shari Oliver
**Programme:** CariSurg MedTech Pathways
**Submission stage:** Interim Submission (Saturday 11:59 p.m. AST)
**Source:** `notebooks/SOliver_Week7_Interim_Complex_Model_Benchmark.ipynb`

---

## Purpose

This is the draft six-axis benchmark table required for the Week 7 interim KPI: *"Draft benchmark table committed to GitHub."* It compares the two Week 6 baseline models (logistic regression, decision tree) against the Week 7 complex model (Random Forest), trained and evaluated on the exact same feature set and train/test split.

Results below are from the actual notebook run (`week7_outputs/docs/SOliver_Week7_Draft_Benchmark_Table.csv`), test set n = 10,816, ESI Level 1 patients in test set n = 15.

## Benchmark Table

| Model | Accuracy | Macro F1 | Weighted F1 | ESI 1 Precision | ESI 1 Recall | ESI 1 F1 | Training Time (s) | Inference — Batch (ms/pred) | Inference — Single Row (ms/pred) |
|---|---|---|---|---|---|---|---|---|---|
| Logistic Regression (Week 6) | 0.580 | 0.424 | 0.612 | 0.019 | **0.733** | 0.037 | 22.80 | 0.011 | 7.42 |
| Decision Tree (Week 6) | 0.252 | 0.169 | 0.288 | 0.012 | 0.533 | 0.024 | **2.06** | **0.006** | **6.91** |
| Random Forest (Week 7) | 0.477 | 0.400 | 0.473 | **0.333** | 0.333 | 0.333 | 20.36 | 0.053 | 100.11 |

*(Bold = best value on that axis. ESI Level 1 recall — the primary clinical metric per the Week 6 methodology — is the column that matters most.)*

## Seventh Axis — Interpretability (Qualitative)

| Model | Interpretability | Justification |
|---|---|---|
| Logistic Regression (Week 6) | Moderate | Each feature has a signed coefficient, but many one-hot chief-complaint columns make explaining a single prediction slower than it looks on paper. |
| Decision Tree (Week 6, `max_depth=5`) | High | A single prediction is one path of at most 5 yes/no questions — explainable to Dr Reyes on a whiteboard in under a minute. |
| Random Forest (Week 7, 300 trees) | Lower (without added tooling) | No single decision path exists — a prediction is a vote across 300 trees. Global feature importance is available now; individual-prediction explanations (SHAP/permutation importance) are planned before final submission. |

## Early Read on the Numbers (draft — not the final recommendation)

Three things stand out and are worth building the memo around:

1. **Logistic regression has by far the best ESI Level 1 recall (0.733)** — it correctly flagged 11 of 15 truly critical patients, versus 8/15 for the decision tree and only 5/15 for the Random Forest. On the metric this project has treated as primary (missing a critical patient is the worst failure mode), added complexity made things *worse*, not better.
2. **The Random Forest is ~13× slower per prediction than the decision tree** (100.1 ms vs 6.9 ms, single-row) for a *lower* ESI 1 recall. That is a hard case to defend to Martina Griffith on cost grounds alone, before even discussing interpretability.
3. **The decision tree's accuracy (0.252) looks unusually low** compared to what would be expected from a `max_depth=5` tree with balanced class weights, and is worth double-checking before it goes in the memo — re-run the Week 6 notebook's decision tree cell in isolation and confirm the numbers match. It's possible, but not yet confirmed, that this is a real effect of the class-weight balancing pushing the tree toward over-predicting rare classes.

**Working implication for the memo:** on this evidence, the case for Random Forest over the Week 6 logistic regression baseline is weak — it costs more to train and infer, is harder to explain, and recalls fewer true emergencies. That's a legitimate, defensible finding in itself ("we tested complexity and it didn't pay off"), but it's worth trying one round of hyperparameter tuning (e.g. `class_weight` variants, shallower trees in the forest, `RandomizedSearchCV`) before finalising, so the memo isn't recommending against a complex model that was simply mis-tuned.

## Notes for Final Submission

- This table is **draft** — Random Forest hyperparameters (`n_estimators=300`, `max_depth=10`, `class_weight="balanced"`) are a starting point, not yet tuned.
- Compute-cost reflection (placeholder ED volume of 150 patients/day, 12 retrains/year) is in `SOliver_Week7_Compute_Cost_Reflection.csv` — swap in real ED volume figures before the memo.
- Per-class metrics for all three models are in `SOliver_Week7_Per_Class_Metrics.csv`.
- The final cost-benefit memo (`docs/week-7-cost-benefit.md`) and decision journal entry (`docs/decisions/2026-week-7-model-choice.md`) will be written from the finalised version of this table.