# CariSurg Portfolio

## Shari Oliver's CariSurg MedTech Pathways Portfolio

## 60-Second Summary

| Question                                | Answer                                                                                                                                                                       |
| ---------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **What is this project?**               | My CariSurg MedTech Pathways portfolio documenting clinical AI, emergency department triage data work, proposal development, HCI/HRI system design and project documentation. |
| **Who is it for?**                      | CariSurg tutors, clinical reviewers and members of the Clinical AI & Innovation Unit who need to quickly review my work.                                                     |
| **How do I install and run it?**        | Clone the repository, install the requirements, and run `python scripts/train.py --config config.yaml` to train the pinned model. See Installation and Usage below. |
| **Where does the data come from?**      | The work uses programme-provided emergency department triage data. Sensitive or programme-controlled datasets are not uploaded unless permission is given.                   |
| **Who built it and how can I connect?** | Built by Shari Oliver for the CariSurg MedTech Pathways Programme. LinkedIn: [Shari Oliver](https://www.linkedin.com/in/shari-oliver-87906b1ba/).                            |
| **Is there a video walkthrough?**       | Yes - [Week 9 walkthrough video](https://drive.google.com/file/d/1D9IdOUpf6XSMbYS8ktBIxD3Ho8fbjRUl/view?usp=sharing), covering the CARISURG Triage Guardian implementation.       |

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
- Week 9 designing and prototyping human-centred systems: system integration notes covering inputs, AI processing and outputs; HCI and HRI co-design canvasses and interface mockups for the clinician-facing triage dashboard; a deployment system requirements specification; safety considerations documentation; and the Week 9 progress report
- Supporting documentation for project setup and review

The main clinical focus is the use of routinely collected triage data to support safer and earlier identification of high-risk emergency department patients. As the portfolio develops, the project also considers workflow fit, stakeholder needs, ethical risks, equity, accountability, compute/deployment cost, human-computer interaction design and safe implementation of AI-assisted triage support.

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
│   │   ├── Week 7 final benchmark table, per-class metrics, ESI Level 1 failure summary, compute-cost reflection and cost–benefit memo
│   │   └── drafts/
│   │       └── Superseded draft versions, kept for audit-trail purposes (see docs/model-selection.md for what's current)
│   ├── week-8/
│   │   └── Week 8 handover document (HANDOVER.md)
│   ├── week-9/                ← Week 9: HCI/HRI system design and deployment documentation
│   │   ├── SOliver_Week9_Integration_Notes.pdf
│   │   ├── SOliver_Week9_HCI_Canvasses.pdf
│   │   ├── SOliver_Week9_HCI_Mockup.pdf
│   │   ├── SOliver_Week9_HRI_Canvasses.pdf
│   │   ├── SOliver_Week9_HRI_Mockup.pdf
│   │   ├── SOliver_Week9_Deployment_System_Requirements.pdf
│   │   ├── SOliver_Week9_Safety_Considerations.pdf
│   │   └── SOliver_Week9_Progress_Report.pdf
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


If you are using **GitHub Codespaces**, open a codespace on this repository from the green **Code** button, then run the same `pip install -r requirements.txt` command in the built-in terminal. `requirements.txt` pins an exact version for every dependency (added in Week 8 for reproducibility — no bare package names, e.g. `scikit-learn==1.5.2` rather than `scikit-learn`).

---

## Usage

Each week's work is self-contained: a short "stored in" path list, then what that week actually did. Weeks run in order below, 0 through 9. Weeks 1–4 are proposal and documentation only, so their entries are a single `docs/` path with no notebook or install step.

### Week 0 — Data Cleaning & Exploration

```
notebooks/week-0/
docs/week-0/
plots/week-0/
```

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

### Week 1 — Preliminary Proposal

```
docs/week-1/
```

Week 1 documents the preliminary proposal for AI-assisted early risk stratification in emergency department triage.

### Week 2 — Updated Proposal & Referencing

```
docs/week-2/
```

Week 2 updates the proposal deliverable with Zotero-generated citations and a full bibliography (see the Week 2 Reference Library under Reference Management).

### Week 3 — Workflow Mapping & Systems Thinking

```
docs/week-3/
```

Week 3 refines the proposal through workflow mapping and systems thinking, identifying AI plug-in points, workflow constraints and stakeholder considerations for the proposed ED triage system.

### Week 4 — Ethics, Safety & Risk Register

```
docs/week-4/
plots/week-4/
```

Week 4 documents ethics and safety considerations for AI-assisted ED triage, including a risk register, a documented AI-harm case study and the workflow diagram output.

### Week 5 — Data Exploration & Feasibility

```
notebooks/week-5/
docs/week-5/
plots/week-5/
```

The Week 5 final notebook focuses on exploration of the programme-provided ED triage dataset, `yaleemmlc_admissionprediction_triage.csv`, including missingness analysis, ESI target review, demographic and fairness-sensitive review, vital sign exploration, clinical plausibility checks, chief complaint review, feature-signal review and early feasibility assessment.

### Week 6 — Baseline Modelling

```
notebooks/week-6/
docs/week-6/
plots/week-6/
```

The Week 6 notebook builds and evaluates two interpretable baseline classifiers — logistic regression and a bounded-depth (`max_depth=5`) decision tree — against a stratified random baseline, using accuracy, per-class precision/recall/F1, macro F1, weighted F1 and confusion matrices. ESI Level 1 recall is treated as the primary clinical metric throughout, since it represents the model's ability to correctly flag the most critically ill patients.

### Week 7 — Complex Model Benchmarking

```
notebooks/week-7/
docs/week-7/
docs/decisions/
plots/week-7/
```

The Week 7 notebook reuses the exact Week 6 feature set, leakage checks and train/test split, then trains and benchmarks three complex model candidates for Phase 3 — Random Forest, XGBoost and LightGBM — against both Week 6 baselines. It evaluates all five models on six quantitative axes (accuracy, precision, recall, F1, training time, inference time) plus a qualitative interpretability axis, and produces the final benchmark table, per-class metrics, ESI Level 1 failure-mode breakdown and compute-cost reflection used to inform the Week 7 cost–benefit memo. **Logistic regression was retained as the Phase 3 model**, on the strength of its materially higher ESI Level 1 recall versus every complex-model candidate tested; **XGBoost** — the best-performing of the three complex candidates — was flagged as a near-term follow-up rather than adopted outright. Full reasoning is documented in `docs/decisions/SOliver_Week7_Model_Choice.md` and `docs/week-7/SOliver_Week7_Cost_Benefit_Memo.md`.

### Week 8 — Running the Pinned Model (Recommended Starting Point)

```
src/
scripts/
tests/
config.yaml
docs/week-8/
docs/model-selection.md
```

The fastest way to see this project work end-to-end no longer requires opening a notebook:

```
pip install -r requirements.txt
pytest tests/ -v          # confirm the environment is set up correctly (10 tests, synthetic data, no dataset required)
python scripts/train.py --config config.yaml   # trains the pinned logistic regression model
```

`scripts/train.py` reads every setting — dataset path, target column, engineered-feature toggles, train/test split, model hyperparameters, output paths — from `config.yaml`. Changing the model or its hyperparameters means editing `config.yaml`, not the code. The raw dataset (`yaleemmlc_admissionprediction_triage.csv`) is not included in this repository; place it at the path specified in `config.yaml` before running.

### Week 9 — Human-Centred System Design

```
docs/week-9/
```

Week 9 moves the pinned model from Week 8 into the design of the clinician-facing system around it: how a triage nurse enters patient information, how the CARISURG Triage Guardian AI processes it, and how the AI's recommendation, confidence score and explanation are surfaced for human review, acceptance or override. This is documented through system integration notes, HCI and HRI co-design canvasses, interface mockups, a deployment system requirements specification, a safety considerations document and a recorded walkthrough video — see the Week 9 Deliverables section below.

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
8. `docs/week-7/` — Week 7 final benchmark table, per-class metrics, compute-cost reflection and cost–benefit memo (`docs/week-7/drafts/` holds superseded draft versions, kept for audit-trail purposes rather than deleted)
9. `docs/decisions/` — Model-selection decision journal documenting the Week 7 model choice rationale
10. `docs/model-selection.md` — Week 8 audit trail: every model trained across Weeks 6–8, with the winner marked and linked back to the Week 7 decision journal
11. `docs/week-8/` — Week 8 handover document (`HANDOVER.md`)
12. `docs/week-9/` — Week 9 system integration notes, HCI and HRI co-design canvasses and mockups, deployment system requirements, safety considerations and the Week 9 progress report

---

## Data Notes

The `data/` folder is reserved for programme-approved datasets. Weeks 1–4 are proposal, workflow and ethics documentation and don't reference the dataset directly.

The Week 5 through Week 8 work all uses the programme-provided emergency department triage dataset titled `yaleemmlc_admissionprediction_triage.csv`. This raw dataset is not uploaded to the repository for data governance reasons; its expected local path is set in `config.yaml` (`data.path`), not hard-coded into any script.

Only derived outputs are included, such as summary CSVs, plots, feasibility documentation, notebook outputs and trained-model metrics (`docs/final_model_metrics.json`). Trained model artefacts (`models/`) are git-ignored and never committed.

Sensitive, private or programme-controlled data should not be committed to this repository unless explicit permission is given. The Week 9 interface mockups in `docs/week-9/` use simulated patient data only.

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

## Week 8 Final Deliverables

The Week 8 final submission includes:

* Modular `src/` package refactored from the Week 6/7 notebooks: `data.py`, `features.py`, `model.py`, `utils.py` — all importable with no top-level side effects, no reliance on notebook globals, confirmed via `python -c "import src.data; import src.model"`
* `config.yaml` pinning the final Phase 3 model (logistic regression) and its exact hyperparameters — one model, one set of hyperparameters, no model-shopping code in `scripts/train.py`
* `scripts/train.py`, a single entry point that reads every setting (paths, seed, hyperparameters) from config and trains, evaluates and saves the pinned model — verified working end-to-end against the full 55,121-row dataset (accuracy 0.591, macro recall 0.635, training time under 20 seconds)
* Two engineered features (`shock_index`, `pulse_pressure`) added to `src/features.py` in response to Week 7 tutor feedback, with a measured, positive impact on macro recall (+0.013) documented in `docs/model-selection.md`
* `tests/` — 10 passing pytest sanity checks (schema validation + end-to-end training smoke test on ~50 rows of synthetic data), runnable with a single `pytest tests/ -v`
* `requirements.txt` with pinned library versions for every dependency
* `docs/model-selection.md` — the final audit trail covering every model trained across Weeks 6–8, winner marked, linked to the Week 7 decision journal
* `docs/week-8/HANDOVER.md` — the completed handover document: project summary, final model decision with reasoning, exact run command, data governance status and three known limitations
* Original Week 6/7 exploratory notebooks preserved unchanged in `notebooks/`
* Dataset confirmed excluded from version control via `.gitignore`

The raw dataset `yaleemmlc_admissionprediction_triage.csv` is not included in the repository for data governance reasons.

---

## Week 9 Deliverables

Week 9, *Designing & Prototyping Human-Centred Systems (HCI)*, moves the project from a pinned predictive model into the design of the clinical decision support system built around it — CARISURG Triage Guardian. The Week 9 final submission includes:

* `SOliver_Week9_Progress_Report.pdf` — the Week 9 progress report: project overview, background, objectives, current development progress across system planning, ML development and UI development, proposed system workflow, system features, HCI considerations, current module status and remaining work
* `SOliver_Week9_Integration_Notes.pdf` — system integration notes documenting system inputs (manual entry, medical device inputs, EHR data), AI processing, system outputs (recommended triage level, confidence score, colour-coded urgency alert, explanation, suggested clinical action, audit log entry), the human-interaction workflow following an AI recommendation, and integration considerations for the existing ED workflow
* `SOliver_Week9_HCI_Canvasses.pdf` — the HCI co-design canvas work
* `SOliver_Week9_HCI_Mockup.pdf` — the clinician-facing Human-Computer Interaction interface mockup: dashboard, live triage queue, new patient assessment, and the AI recommendation review screen supporting accept/override with a recorded audit trail
* `SOliver_Week9_HRI_Canvasses.pdf` — the HRI co-design canvas work
* `SOliver_Week9_HRI_Mockup.pdf` — the HRI interface mockup
* `SOliver_Week9_Deployment_System_Requirements.pdf` — the deployment system requirements specification
* `SOliver_Week9_Safety_Considerations.pdf` — safety considerations documentation for the proposed system
* **Week 9 walkthrough video:** [Watch on Google Drive](https://drive.google.com/file/d/1D9IdOUpf6XSMbYS8ktBIxD3Ho8fbjRUl/view?usp=sharing) — a recorded walkthrough of the CARISURG Triage Guardian implementation

Across both the HCI and integration documentation, the system is designed so that the AI functions as decision support rather than an autonomous decision-maker: the triage nurse always reviews the recommendation and its explanation, and may accept it or override it with a recorded reason, preserving clinician oversight and an auditable decision trail.

The raw dataset `yaleemmlc_admissionprediction_triage.csv` is not included in the repository for data governance reasons. Week 9 interface mockups use simulated patient data only.

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
* Week 9 system integration notes, HCI and HRI co-design canvasses and mockups, deployment system requirements, safety considerations documentation and progress report for the CARISURG Triage Guardian clinical decision support system

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
* Week 9 human-centred system design outputs — integration notes, HCI/HRI canvasses and mockups, deployment requirements and safety considerations — based on the Week 8 pinned model

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
