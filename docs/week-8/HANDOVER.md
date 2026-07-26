# Handover Document (Outline — Week 8 Interim)

**Audience test:** can a new hire, arriving Monday morning, clone this repo, read this document, and be running the model by end of day? This outline sketches each required section; full prose is due at final submission.

---

## (a) Project Summary

*Draft paragraph — to be tightened for final submission:*

This project builds a clinical decision-support model that predicts a patient's Emergency Severity Index (ESI) — a five-level triage urgency scale, where Level 1 is most critical — from information available at the point of triage: vital signs, arrival mode, chief complaint and age. It was developed across Weeks 5–8 of the CariSurg MedTech Pathways programme for the ED Board and Mercer IT Governance, with the goal of flagging critically ill patients (ESI Level 1) faster and more reliably than manual triage alone, without replacing clinician judgement.

## (b) Final Model Decision

**Model:** Logistic Regression (scikit-learn `LogisticRegression`, `class_weight="balanced"`, `max_iter=2000`, `random_state=42`).

**One-sentence reason:** it correctly identifies far more true ESI Level 1 (most critical) patients than any complex-model alternative tested (Random Forest, XGBoost, LightGBM) — 7 of 10 vs. 2 of 10 for the next-best candidate — and missing a critical patient is the costliest possible failure mode for a triage-support tool.

*(Full reasoning: `docs/week-7-cost-benefit.md` and `docs/decisions/2026-week-7-model-choice.md`.)*

## (c) How to Run

```bash
git clone https://github.com/ShariUWI/carisurg-portfolio.git
cd carisurg-portfolio
pip install -r requirements.txt

# Place yaleemmlc_admissionprediction_triage.csv in the repo root
# (see section (d) — not committed to the repo)

python scripts/train.py --config config.yaml
```

*Expected output:* console progress (row counts, split sizes, timing), a saved model at `models/final_model.joblib`, and metrics written to `docs/final_model_metrics.json`.

*Still to confirm for final submission:* exact `requirements.txt` versions pinned (Task 1 asks for this explicitly); a one-line `pytest` command new hires should run first (`pytest tests/ -v`) to confirm their environment is set up correctly before training.

## (d) Where the Data Lives

- **Dataset:** `yaleemmlc_admissionprediction_triage.csv` — programme-provided emergency department triage data.
- **Governance status:** not committed to this repository. It is programme-controlled data; a new hire would need to request access through the CariSurg programme / Mercer Health data governance process before it can be placed locally at the path `config.yaml` expects (`data.path`).
- **Derived outputs only** (summary CSVs, plots, trained model metrics) are committed — never raw patient-level rows.

*Still to confirm for final submission:* the actual internal process/contact for requesting dataset access, once known.

## (e) Known Limitations

- **Very low ESI Level 1 precision (0.020).** The pinned model flags the overwhelming majority of ESI Level 1 alerts incorrectly. This is a known, accepted trade-off for higher recall, but it carries a real alarm-fatigue risk that has not yet been mitigated (e.g. via threshold tuning) and should be monitored if this model reaches a live setting.
- **Small ESI Level 1 sample size (10 patients in the current test set).** Recall and precision estimates for the class that matters most are built on very few cases and should be treated as noisy, not stable, until cross-validated.
- **Unresolved reproducibility question.** The test set size changed between two notebook runs in Week 7 (10,816 vs. 8,060 rows) despite an unchanged random seed and split logic, suggesting the underlying dataset itself may have changed between runs. This needs investigating before the current numbers are treated as fully final.

---

## Outline Status

This is the **interim** version of the handover document — every section above has real, project-specific content rather than placeholder headings, but is still draft-level prose. Final submission will tighten the language, confirm the two "still to confirm" items in sections (c) and (d), and fold this content into the repository README per the Week 8 brief's note that "this content will also be useful for your README."
