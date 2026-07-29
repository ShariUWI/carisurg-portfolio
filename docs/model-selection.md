# Model-Selection Results Table (Final — Week 8)

**Purpose:** the audit trail Martina Griffith asked for — every model trained across Weeks 6–8, not just the final one. Full reasoning behind the winning model is in [`docs/decisions/SOliver_Week7_Model_Choice.md`](decisions/SOliver_Week7_Model_Choice.md) and [`docs/week-7/SOliver_Week7_Cost_Benefit_Memo.md`](week-7/SOliver_Week7_Cost_Benefit_Memo.md).

**Winner: 🏆 Logistic Regression** — pinned as the Phase 3 model in [`config.yaml`](../config.yaml), on ESI Level 1 recall grounds (see reasoning below the table). One model, one set of hyperparameters, no model-shopping code remains in `scripts/train.py`.

---

## All Models Trained, Weeks 6–7

| Model | Week | Key Hyperparameters | Accuracy | Precision (macro) | Recall (macro) | F1 (macro) | Training Time (s) | Inference Time (ms/pred) |
|---|---|---|---|---|---|---|---|---|
| 🏆 **Logistic Regression** | 6 | `max_iter=2000`, `class_weight="balanced"` | 0.592 | 0.426 | **0.644** | 0.430 | 23.32 | 11.59 |
| Decision Tree | 6 | `max_depth=5`, `class_weight="balanced"` | 0.359 | 0.383 | 0.374 | 0.258 | **2.81** | 18.90 |
| Random Forest | 7 | `n_estimators=300`, `max_depth=10`, `class_weight="balanced"` | 0.491 | 0.364 | 0.434 | 0.340 | 19.86 | 91.01 |
| XGBoost | 7 | `n_estimators=300`, `max_depth=6`, `learning_rate=0.1`, balanced sample weights | 0.628 | **0.554** | 0.545 | 0.496 | 26.70 | 10.35 |
| LightGBM | 7 | `n_estimators=300`, `learning_rate=0.1`, `class_weight="balanced"` | **0.662** | 0.548 | 0.516 | **0.497** | 9.74 | **10.02** |

*Bold = best value on that axis. All models above trained and evaluated on the identical 80/20 stratified split (`random_state=42`), n = 8,060 test rows.*

## Week 8: Pinned Model, Re-Run on the Full Dataset via `scripts/train.py`

Running the refactored `src/` pipeline against the complete local dataset (55,121 rows — larger than any prior notebook run; see note below) surfaced two additional data points for the pinned logistic regression model, addressing Week 7 tutor feedback on engineered features.

| Model | Engineered Features? | Accuracy | Precision (macro) | Recall (macro) | F1 (macro) | Training Time (s) |
|---|---|---|---|---|---|---|
| Logistic Regression (pinned) | No | 0.587 | 0.425 | 0.622 | 0.427 | 14.14 |
| 🏆 **Logistic Regression (pinned)** | **Yes** (`shock_index`, `pulse_pressure`) | **0.591** | 0.425 | **0.635** | **0.429** | 14.74 |

*n = 44,096 train / 11,025 test rows. Inference timing from this run uses a different (batch-averaged) methodology than the Weeks 6–7 rows above and is not directly comparable — see `scripts/train.py` timing note.*

Engineered features produced a small but consistent improvement, most notably on macro recall (+0.013) — the metric this project prioritises. `shock_index` (heart rate ÷ systolic BP) and `pulse_pressure` (systolic − diastolic BP) are both standard clinical early-warning indicators, not arbitrary derived columns, which is why they were the first features added rather than a broader automated feature-engineering sweep.

**Dataset size note:** this run's row count (55,121) is substantially larger than any prior notebook run (54,080 in the earliest run; 8,060 test rows in the most recent Week 7 run). This strongly suggests earlier runs were working from a smaller or partial copy of the dataset, not a bug in the split logic — the random seed and split code are unchanged throughout. This run, against what appears to be the complete file, should be treated as the most reliable figure going forward, though this is inference, not confirmed fact, and is flagged here rather than asserted.

## Critical-Class Breakdown — ESI Levels 1 and 2

Added in response to Week 7 tutor feedback: macro-averaged metrics above can mask how each model handles the two most critical ESI levels specifically. ESI Level 1 (most critical) and Level 2 are broken out below.

| Model | ESI 1 Precision | ESI 1 Recall | ESI 1 F1 | ESI 2 Precision | ESI 2 Recall | ESI 2 F1 |
|---|---|---|---|---|---|---|
| 🏆 Logistic Regression | 0.020 | **0.700** | 0.040 | 0.670 | 0.646 | 0.658 |
| Decision Tree | 0.009 | 0.300 | 0.017 | 0.472 | 0.434 | 0.452 |
| Random Forest | 0.000 | 0.000 | 0.000 | 0.553 | 0.709 | 0.622 |
| XGBoost | **0.667** | 0.200 | 0.308 | 0.663 | **0.728** | 0.694 |
| LightGBM | 0.500 | 0.100 | 0.167 | **0.681** | 0.721 | **0.700** |

**Reading this table:** logistic regression is the clear outlier on ESI 1 recall — it catches far more true critical patients than any other model, but at the cost of a very high false-alarm rate (0.020 precision). On ESI 2, the picture flips: logistic regression is the *weakest* model on both precision and recall, while XGBoost and LightGBM are consistently strongest across nearly every ESI 2 metric. This means the "winning" model is not uniformly best — it wins specifically on the single highest-stakes class (ESI 1), and gives up ground on ESI 2 performance to do so. This trade-off is explicit in the Week 7 memo's "what this recommendation does not solve" section.

## Why Logistic Regression Won

One sentence: **logistic regression correctly identifies far more true ESI Level 1 (most critical) patients than any other model tested (7 of 10 vs. 2 of 10 for XGBoost, the next-best candidate), and missing a critical patient is the costliest possible failure mode for a triage-support tool.**

Full three-arguments-for / three-arguments-against reasoning, risks and the explicit statement of what this choice does *not* solve are in `docs/week-7/SOliver_Week7_Cost_Benefit_Memo.md`. The condensed decision record is in `docs/decisions/SOliver_Week7_Model_Choice.md`.

## Notes

- This table reports macro-averaged Precision/Recall/F1 for the six-axis columns and separates out ESI 1/2 for the critical-class view, per the Week 7 tutor feedback on checking the most critical classes specifically.
- Engineered features (`shock_index`, `pulse_pressure`) have been re-run against the full local dataset (see the Week 8 section above) — a small, consistent improvement, strongest on recall. The Weeks 6–7 comparison table above still describes the un-engineered feature set on an earlier, smaller copy of the dataset; a full re-run of every model on the complete dataset with engineered features would be a reasonable next step beyond this handover, not a gap in it.
- XGBoost's strong ESI 2 performance and near-competitive overall metrics keep it flagged as a near-term follow-up candidate (see memo Section 6) — not fully closed off in favour of logistic regression, but not the pinned production model either.