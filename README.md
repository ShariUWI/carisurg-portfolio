# CariSurg Portfolio

## Shari Oliver's CariSurg MedTech Pathways Portfolio

## 60-Second Summary

| Question                                | Answer                                                                                                                                                                       |
| ---------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **What is this project?**               | My CariSurg MedTech Pathways portfolio documenting clinical AI, emergency department triage data work, proposal development and project documentation.                       |
| **Who is it for?**                      | CariSurg tutors, clinical reviewers and members of the Clinical AI & Innovation Unit who need to quickly review my work.                                                     |
| **How do I install and run it?**        | Clone the repository, install the requirements, and run `python scripts/train.py --config config.yaml` to train the pinned model. See Installation and Usage below. |
| **Where does the data come from?**      | The work uses programme-provided emergency department triage data. Sensitive or programme-controlled datasets are not uploaded unless permission is given.                   |
| **Who built it and how can I connect?** | Built by Shari Oliver for the CariSurg MedTech Pathways Programme. LinkedIn: [Shari Oliver](https://www.linkedin.com/in/shari-oliver-87906b1ba/).                            |

---

## Purpose

The purpose of this repository is to keep my CariSurg programme work organised, reproducible and audit-ready.

It includes:

- Week 0 Jupyter notebooks on emergency department triage data cleaning, validation and visualisation
- Week 0 reports, written reflections and exploratory plots
- Week 1 proposal documents on AI-assisted early risk stratification in emergency department triage
- Week 2 updated proposal deliverable with Zotero-generated citations and bibliography
- Week 3 workflow mapping, systems thinking and refined proposal documentation
- Week 4 ethics, safety, risk register and AI-harm case study documentation
- Week 5 final data exploration, data-quality visualisation dashboard, feasibility memo and top-10 clinically justified feature shortlist
- Week 6 baseline modelling notebook (logistic regression and decision tree), initial model evaluation, stratified random baseline comparison and confusion matrix artefacts, with a focus on ESI Level 1 recall as the primary clinical metric
- Week 7 final complex model benchmarking: Random Forest, XGBoost and LightGBM classifiers trained on the Week 6 feature set and train/test split, evaluated against the Week 6 baselines on a six-axis quantitative benchmark (accuracy, precision, recall, F1, training time, inference time) plus a qualitative interpretability axis, with a final benchmark table and a documented model-selection decision journal. **Logistic regression was retained as the Phase 3 model** on ESI Level 1 recall grounds, with XGBoost — the strongest of the three complex-model candidates — flagged as a near-term follow-up.
- Week 8 reproducibility and handover: the pinned logistic regression model refactored out of notebooks into a modular `src/` package driven by a single `config.yaml`, a `scripts/train.py` entry point, pytest sanity checks, a model-selection audit table covering every model trained across Weeks 6–7, and a handover document
- Supporting documentation for project setup and review

The main clinical focus is the use of routinely collected triage data to support safer and earlier identification of high-risk emergency department patients. As the portfolio develops, the project also considers workflow fit, stakeholder needs, ethical risks, equity, accountability, compute/deployment cost and safe implementation of AI-assisted triage support.

---

## Repository Structure

```
carisurg-portfolio/
│
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── setup_notes.md
├── config.yaml               ← Week 8: single source of truth for the pinned model
├── pytest.ini
│
├── src/                       ← Week 8: modular, importable package (no notebook logic)
│   ├── __init__.py
│   ├── data.py                 (dataset loading, feature selection, leakage check)
│   ├── features.py             (engineered features: shock_index, pulse_pressure)
│   ├── model.py                (preprocessing, training, evaluation)
│   └── utils.py                (seeding, config loading)
│
├── scripts/                   ← Week 8: entry point
│   └── train.py                (reads config.yaml, trains and saves the pinned model)
│
├── tests/                     ← Week 8: pytest sanity checks
│   ├── test_data.py             (schema checks)
│   └── test_model.py            (end-to-end training smoke test)
│
├── models/                    ← Week 8: trained model artefacts (git-ignored, not committed)
│
├── data/
│   └── README.md
│
├── docs/
│   ├── README.md
│   ├── model-selection.md    ← Week 8: audit trail, every model trained Weeks 6–8
│   ├── week-0/
│   │   └── Week 0 reports, written submissions and supporting documents
│   ├── week-1/
│   │   └── Week 1 interim and final preliminary proposal documents
│   ├── week-2/
│   │   └── Week 2 updated proposal deliverable
│   ├── week-3/
│   │   └── Week 3 workflow mapping, systems thinking and refined proposal documents
│   ├── week-4/
│   │   └── Week 4 interim and final proposals containing ethics, safety, risk register and AI harm case study
│   ├── week-5/
│   │   └── Week 5 final feasibility memo, memo outline, summary CSVs and top-10 feature shortlist
│   ├── week-6/
│   │   └── Week 6 baseline model evaluation outputs and supporting documentation
│   ├── week-7/
│   │   └── Week 7 final benchmark table, per-class metrics, ESI Level 1 failure summary, compute-cost reflection and cost–benefit memo
│   ├── week-8/
│   │   └── Week 8 handover document (HANDOVER.md)
│   └── decisions/
│       └── Week 7 model-selection decision journal
│
├── notebooks/                 ← unchanged by the Week 8 refactor; kept as the exploratory record
│   ├── Week 0 Jupyter notebooks
│   ├── week-5/
│   │   └── Week 5 final exploration and data profiling notebooks
│   ├── week-6/
│   │   └── Week 6 baseline modelling notebook (logistic regression, decision tree)
│   └── week-7/
│       └── Week 7 final complex model benchmarking notebook (Random Forest, XGBoost, LightGBM)
│
├── plots/
│   ├── week-0/
│   │   └── Week 0 exploratory plots
│   ├── week-4/
│   │   └── Week 4 workflow diagram output
│   ├── week-5/
│   │   └── Week 5 data-quality and exploratory visualisations
│   ├── week-6/
│   │   └── Week 6 confusion matrix and model evaluation plots
│   └── week-7/
│       └── Week 7 final confusion matrices (Random Forest, XGBoost, LightGBM), feature importance plots and final model comparison chart
│
└── screenshots/
    └── Supporting screenshots for documentation and programme submissions
```

---

## Installation

To review or run the notebooks locally, clone this repository and install the required Python packages.

```
git clone https://github.com/ShariUWI/carisurg-portfolio.git
cd carisurg-portfolio
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

For Windows PowerShell, use:

```
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

If you are using Google Colab, you can upload notebooks directly from the relevant weekly notebook folder, such as `notebooks/week-0/`, `notebooks/week-5/`, `notebooks/week-6/` or `notebooks/week-7/`, and run the cells there.

If you are using **GitHub Codespaces**, open a codespace on this repository from the green **Code** button, then run the same `pip install -r requirements.txt` command in the built-in terminal. `requirements.txt` pins exact versions for every dependency, including `scikit-learn`, `pyyaml`, `joblib` and `pytest`, added in Week 8.

---

## Usage

### Running the Pinned Model (Week 8 — Recommended Starting Point)

The fastest way to see this project work end-to-end no longer requires opening a notebook:

```
pip install -r requirements.txt
pytest tests/ -v          # confirm the environment is set up correctly (10 tests, synthetic data, no dataset required)
python scripts/train.py --config config.yaml   # trains the pinned logistic regression model
```

`scripts/train.py` reads every setting — dataset path, target column, engineered-feature toggles, train/test split, model hyperparameters, output paths — from `config.yaml`. Changing the model or its hyperparameters means editing `config.yaml`, not the code. The raw dataset (`yaleemmlc_admissionprediction_triage.csv`) is not included in this repository; place it at the path specified in `config.yaml` before running.

### Exploratory Notebooks

```
jupyter lab notebooks/week-0/
```

Recommended notebook review order:

1. `SOliver_Week0_Day1_Gender_Cleaning.ipynb`
2. `SOliver_Week0_Day1_Gender_Cleaning_Updated.ipynb`
3. `SOliver_Week0_Tutorial2_Advanced_Cleaning.ipynb`
4. `SOliver_Week0_Tutorial3_Visualisation.ipynb`
5. `SOliver_Week0_Final_Tasks2_4.ipynb`

Supporting reports, written submissions and proposal documents are stored in the `docs/` folder and organised by programme week.

Week 5 data exploration work is stored in:

```
notebooks/week-5/
docs/week-5/
plots/week-5/
```

The Week 5 final notebook focuses on exploration of the programme-provided ED triage dataset, `yaleemmlc_admissionprediction_triage.csv`, including missingness analysis, ESI target review, demographic and fairness-sensitive review, vital sign exploration, clinical plausibility checks, chief complaint review, feature-signal review and early feasibility assessment.

Week 6 baseline modelling work is stored in:

```
notebooks/week-6/
docs/week-6/
plots/week-6/
```

The Week 6 notebook builds and evaluates two interpretable baseline classifiers — logistic regression and a bounded-depth (`max_depth=5`) decision tree — against a stratified random baseline, using accuracy, per-class precision/recall/F1, macro F1, weighted F1 and confusion matrices. ESI Level 1 recall is treated as the primary clinical metric throughout, since it represents the model's ability to correctly flag the most critically ill patients.

Week 7 final complex model benchmarking work is stored in:

```
notebooks/week-7/
docs/week-7/
docs/decisions/
plots/week-7/
```

The Week 7 notebook reuses the exact Week 6 feature set, leakage checks and train/test split, then trains and benchmarks three complex model candidates for Phase 3 — Random Forest, XGBoost and LightGBM — against both Week 6 baselines. It evaluates all five models on six quantitative axes (accuracy, precision, recall, F1, training time, inference time) plus a qualitative interpretability axis, and produces the final benchmark table, per-class metrics, ESI Level 1 failure-mode breakdown and compute-cost reflection used to inform the Week 7 cost–benefit memo. **Logistic regression was retained as the Phase 3 model**, on the strength of its materially higher ESI Level 1 recall versus every complex-model candidate tested; **XGBoost** — the best-performing of the three complex candidates — was flagged as a near-term follow-up rather than adopted outright. Full reasoning is documented in `docs/decisions/SOliver_Week7_Model_Choice.md` and `docs/week-7/SOliver_Week7_Cost_Benefit_Memo.md`.

The raw dataset is not included in this repository for data governance reasons. All notebooks are written to load the dataset locally when available.

---

## Documentation Guide

The `docs/` folder is organised into weekly subfolders, plus a `decisions/` folder for cross-cutting decision records. The recommended document review order is:

1. `docs/week-0/` — Week 0 reports and written submissions
2. `docs/week-1/` — Week 1 preliminary proposal documents
3. `docs/week-2/` — Week 2 updated proposal deliverable
4. `docs/week-3/` — Week 3 workflow mapping, systems thinking and refined proposal documents
5. `docs/week-4/` — Week 4 ethics, safety, risk register and AI-harm case study documents
6. `docs/week-5/` — Week 5 final feasibility memo, memo outline, data-quality summaries and top-10 feature shortlist
7. `docs/week-6/` — Week 6 baseline model evaluation outputs and supporting documentation
8. `docs/week-7/` — Week 7 final benchmark table, per-class metrics, compute-cost reflection and cost–benefit memo
9. `docs/decisions/` — Model-selection decision journal documenting the Week 7 model choice rationale
10. `docs/model-selection.md` — Week 8 audit trail: every model trained across Weeks 6–8, with the winner marked and linked back to the Week 7 decision journal
11. `docs/week-8/` — Week 8 handover document (`HANDOVER.md`)

---

## Data Notes

The `data/` folder is reserved for programme-approved datasets.

The Week 5 through Week 8 work all uses the programme-provided emergency department triage dataset titled `yaleemmlc_admissionprediction_triage.csv`. This raw dataset is not uploaded to the repository for data governance reasons; its expected local path is set in `config.yaml` (`data.path`), not hard-coded into any script.

Only derived outputs are included, such as summary CSVs, plots, feasibility documentation, notebook outputs and trained-model metrics (`docs/final_model_metrics.json`). Trained model artefacts (`models/`) are git-ignored and never committed.

Sensitive, private or programme-controlled data should not be committed to this repository unless explicit permission is given.

---

## Week 5 Final Deliverables

The Week 5 final submission includes:

* Final exploration and data profiling notebook
* Data-quality visualisation dashboard
* 3-page clinical feasibility memo
* Top-10 feature shortlist with clinical reasoning
* Derived summary CSVs and supporting plots

The raw dataset `yaleemmlc_admissionprediction_triage.csv` is not included in the repository for data governance reasons.

---

## Week 6 Deliverables

The Week 6 final submission includes:

* Baseline modelling notebook (logistic regression and decision tree)
* Stratified random baseline comparison
* Evaluation metrics including accuracy, precision, recall and F1-score, by class, macro and weighted
* Logistic regression and decision tree confusion matrix artefacts
* ESI Level 1 failure-mode analysis, established as the primary clinical safety metric

The raw dataset `yaleemmlc_admissionprediction_triage.csv` is not included in the repository for data governance reasons.

---

## Week 7 Final Deliverables

The Week 7 final submission includes:

* Final complex model benchmarking notebook, training and evaluating Random Forest, XGBoost and LightGBM classifiers on the Week 6 feature set and train/test split
* Final six-axis quantitative benchmark against both Week 6 baselines: accuracy, precision, recall, F1, training time and inference time
* Qualitative interpretability assessment across all five models, including feature importance for the complex models
* Final benchmark table, per-class metrics, ESI Level 1 failure-mode breakdown and compute-cost reflection
* Confusion matrices for Random Forest, XGBoost and LightGBM
* Documented decision journal and cost–benefit memo: **logistic regression retained** for Phase 3 on ESI Level 1 recall grounds, with **XGBoost** flagged as the strongest complex-model candidate and a near-term follow-up

The raw dataset `yaleemmlc_admissionprediction_triage.csv` is not included in the repository for data governance reasons.

---

## Week 8 Interim Deliverables

The Week 8 interim submission includes:

* Modular `src/` package refactored from the Week 6/7 notebooks: `data.py`, `features.py`, `model.py`, `utils.py` — all importable with no top-level side effects, no reliance on notebook globals
* `config.yaml` pinning the final Phase 3 model (logistic regression) and its exact hyperparameters
* `scripts/train.py`, a single entry point that trains, evaluates and saves the pinned model from config
* Two engineered features (`shock_index`, `pulse_pressure`) added to `src/features.py` in response to Week 7 tutor feedback, with a measured (small, positive) impact on macro recall documented in `docs/model-selection.md`
* `tests/` — 10 passing pytest sanity checks (schema validation + end-to-end training smoke test on synthetic data)
* `docs/model-selection.md` — the audit trail covering every model trained across Weeks 6–8, winner marked, linked to the Week 7 decision journal
* `docs/week-8/HANDOVER.md` — handover document outline covering project summary, final model decision, how to run, data governance status and known limitations
* Original Week 6/7 exploratory notebooks preserved unchanged in `notebooks/`

The raw dataset `yaleemmlc_admissionprediction_triage.csv` is not included in the repository for data governance reasons.

---

## Main Outputs

This repository currently includes:

* Cleaned and documented Week 0 triage data notebooks
* Gender column cleaning report
* MAP cleaning report with clinical justifications
* Matplotlib visualisation report
* Digital ED triage model pseudocode document
* Week 1 proposal documents related to AI-assisted ED risk stratification
* Week 2 updated proposal deliverable with Zotero-generated citations and bibliography
* Week 3 workflow mapping and systems-thinking deliverables, including AI plug-in points, workflow constraints and stakeholder considerations
* Week 4 ethics and safety documentation, including a risk register and documented AI-harm case study
* Week 5 final exploration notebook, data-quality visualisation dashboard, 3-page clinical feasibility memo, top-10 feature shortlist and derived summary outputs
* Week 6 baseline modelling notebook, evaluation metrics, stratified random baseline comparison and confusion matrix artefacts
* Week 7 final complex model benchmarking notebook (Random Forest, XGBoost, LightGBM), final benchmark table, interpretability assessment, decision journal and cost–benefit memo recommending logistic regression, with XGBoost flagged as a follow-up candidate
* Week 8 modular `src/` package, config-driven training entry point, pytest sanity checks, model-selection audit table and handover document

---

## Reference Management

* Week 1 proposal documents related to AI-assisted ED risk stratification
* Week 2 updated proposal deliverable with Zotero-generated citations and bibliography
* Week 3 workflow mapping and systems-thinking deliverables, including AI plug-in points, workflow constraints and stakeholder considerations
* Week 4 ethics and safety submission, including a risk register and documented AI-harm case study
* Week 5 data exploration and feasibility memo outputs based on programme-provided ED triage data
* Week 6 baseline modelling and evaluation outputs based on programme-provided ED triage data
* Week 7 complex model benchmarking, final evaluation and cost–benefit analysis based on programme-provided ED triage data
* Week 8 reproducibility refactor and model-selection audit trail based on the Week 6–7 modelling outputs

### Zotero Reference Libraries

* Week 2 Reference Library: https://www.zotero.org/groups/6588971/s._oliver-_week_2_reference_library
* Week 3 Reference Library: https://www.zotero.org/groups/6599337/s._oliver-_week_3_reference_list
* Week 4 Reference Library: https://www.zotero.org/groups/6599645/s._oliver-_week_4_reference_library

---

## Contributing

This repository is primarily maintained by **Shari Oliver** as part of the CariSurg MedTech Pathways Programme.

CariSurg tutors, mentors and reviewers may provide feedback through GitHub issues, pull request comments or programme communication channels.

Before merging any changes into this repository:

1. File paths are reviewed.
2. Notebooks and documents are checked to ensure that they open correctly.
3. The repository is checked to confirm that no private data or credentials are included.
4. Documentation is reviewed to ensure that a clinical or technical reviewer can understand the project within 60 seconds.

---

## AI Use

AI tools were used to support drafting, refactoring, documentation and code review. All AI-generated content was reviewed, edited and verified before being committed.

No real patient data, private credentials or sensitive information was pasted into AI tools.

Unless otherwise stated, machine learning experiments from Week 6 onward use:

- Random Seed = **42**
- 80/20 stratified train-test split

---

## License

This repository is licensed under the MIT License. See the `LICENSE` file for details.

---

## Connect

**Shari Oliver**
CariSurg MedTech Pathways Scholar
Aspiring Medical Physicist | Healthcare AI & Clinical Innovation

**LinkedIn:** [Shari Oliver](https://www.linkedin.com/in/shari-oliver-87906b1ba/)
