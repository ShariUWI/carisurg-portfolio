# Handover Document

**Purpose of this document:** answer Martina Griffith's question — *"Can a new hire, arriving Monday morning, clone this repo, read this document, and be running the model by end of day?"* Everything needed to do that is below.

---

## (a) Project Summary

This project builds a clinical decision-support model that predicts a patient's Emergency Severity Index (ESI) — a five-level triage urgency scale, where Level 1 is most critical — from information available at the point of triage: vital signs, arrival mode, chief complaint and age. It was developed across Weeks 5–8 of the CariSurg MedTech Pathways programme for the ED Board and Mercer IT Governance, with the goal of flagging critically ill patients (ESI Level 1) faster and more reliably than manual triage alone, without replacing clinician judgement. The pipeline was refactored in Week 8 out of exploratory notebooks into a modular, config-driven codebase so the pinned model can be retrained and audited by someone who did not build it.

## (b) Final Model Decision

**Model:** Logistic Regression (scikit-learn `LogisticRegression`, `class_weight="balanced"`, `max_iter=2000`, `random_state=42`), pinned in [`config.yaml`](../../config.yaml).

**One-sentence reason:** it correctly identifies far more true ESI Level 1 (most critical) patients than any complex-model alternative tested (Random Forest, XGBoost, LightGBM) — 7 of 10 vs. 2 of 10 for the next-best candidate, XGBoost — and missing a critical patient is the costliest possible failure mode for a triage-support tool.

Full reasoning, including the arguments against this choice and what it explicitly does not solve, is in [`docs/week-7/SOliver_Week7_Cost_Benefit_Memo.md`](../week-7/SOliver_Week7_Cost_Benefit_Memo.md) and the condensed record in [`docs/decisions/SOliver_Week7_Model_Choice.md`](../decisions/SOliver_Week7_Model_Choice.md). The full comparison across every model trained is in [`docs/model-selection.md`](../model-selection.md).

## (c) How to Run

```bash
git clone https://github.com/ShariUWI/carisurg-portfolio.git
cd carisurg-portfolio
pip install -r requirements.txt

# Place yaleemmlc_admissionprediction_triage.csv in the repo root
# (see section (d) below — not committed to the repo)

pytest tests/ -v                                # optional but recommended first: confirms the environment works
python scripts/train.py --config config.yaml    # trains and saves the pinned model
```

**Expected output:** console progress (row counts, split sizes, engineered features added, timing), a saved model at `models/final_model.joblib`, and metrics written to `docs/final_model_metrics.json`. On the full dataset (55,121 rows), this run completes in under 20 seconds and reports approximately 0.591 accuracy, 0.635 macro recall.

All hyperparameters, file paths and the random seed are set in `config.yaml`, not hard-coded in `scripts/train.py` or anywhere in `src/` — to retrain with different settings, edit `config.yaml`, not the code.

## (d) Where the Data Lives

- **Dataset:** `yaleemmlc_admissionprediction_triage.csv` — programme-provided emergency department triage data, 55,121 rows.
- **Governance status:** not committed to this repository (listed in `.gitignore` by filename). It is programme-controlled data; a new hire would need to request access through the CariSurg programme / Mercer Health data governance process before placing it locally at the path `config.yaml`'s `data.path` expects.
- **Derived outputs only** (summary CSVs, plots, trained-model metrics) are committed — never raw patient-level rows. Trained model artefacts (`models/`) are also git-ignored, since they are regenerable from `scripts/train.py` and the raw data, not source artefacts themselves.

## (e) Known Limitations

- **Very low ESI Level 1 precision (0.020).** The pinned model flags the overwhelming majority of ESI Level 1 alerts incorrectly. This is a known, accepted trade-off for higher recall, but it carries a real alarm-fatigue risk that has not yet been mitigated (e.g. via threshold tuning) and should be monitored if this model reaches a live setting.
- **Small ESI Level 1 sample size (10 patients in the current test set).** Recall and precision estimates for the class that matters most are built on very few cases and should be treated as noisy, not stable, until cross-validated across multiple folds.
- **No hyperparameter tuning has been performed on any model tested**, including the pinned logistic regression. XGBoost, the strongest complex-model candidate, was also tested with a single untuned configuration — a tuned version could plausibly narrow the recall gap driving this decision, and is flagged as a near-term follow-up rather than a closed question.

---

*This document is also summarised in the repository [`README.md`](../../README.md), per the Week 8 brief's note that this content would be useful there too.*