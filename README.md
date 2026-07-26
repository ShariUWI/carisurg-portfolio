# CariSurg Portfolio

## Shari Oliver's CariSurg MedTech Pathways Portfolio

## 60-Second Summary

| Question                                | Answer                                                                                                                                                                       |
| ---------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **What is this project?**               | My CariSurg MedTech Pathways portfolio documenting clinical AI, emergency department triage data work, proposal development and project documentation.                       |
| **Who is it for?**                      | CariSurg tutors, clinical reviewers and members of the Clinical AI & Innovation Unit who need to quickly review my work.                                                     |
| **How do I install and run it?**        | Clone the repository, install the requirements and open the notebooks in Jupyter Lab or Google Colab. See the Installation and Usage sections below for copy-paste commands. |
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
- Week 7 final complex model benchmarking: Random Forest, XGBoost and LightGBM classifiers trained on the Week 6 feature set and train/test split, evaluated against the Week 6 baselines on a six-axis quantitative benchmark (accuracy, precision, recall, F1, training time, inference time) plus a qualitative interpretability axis, with a final benchmark table, SHAP/feature-importance-based interpretability, a documented model-selection decision journal and a cost–benefit memo recommending LightGBM for deployment
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
│
├── data/
│   └── README.md
│
├── docs/
│   ├── README.md
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
│   └── decisions/
│       └── Week 7 model-selection decision journal
│
├── notebooks/
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
├── screenshots/
│   └── Supporting screenshots for documentation and programme submissions
│
└── src/
    └── Future reusable scripts or functions
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

---

## Usage

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

The Week 7 notebook reuses the exact Week 6 feature set, leakage checks and train/test split, then trains and benchmarks three complex model candidates for Phase 3 — Random Forest, XGBoost and LightGBM — against both Week 6 baselines. It evaluates all five models on six quantitative axes (accuracy, precision, recall, F1, training time, inference time) plus a qualitative interpretability axis, and produces the final benchmark table, per-class metrics, ESI Level 1 failure-mode breakdown and compute-cost reflection used to inform the Week 7 cost–benefit memo. Based on this benchmarking, **LightGBM was selected as the preferred model**, per the documented rationale in `docs/decisions/SOliver_Week7_Model_Choice.md`, on the strength of its overall accuracy, Macro F1, training/inference speed and interpretability via feature importance and SHAP values.

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
8. `docs/week-7/` — Week 7 final benchmark table, per-class metrics, compute-cost reflection and cost–benefit memo recommending LightGBM
9. `docs/decisions/` — Model-selection decision journal documenting the Week 7 model choice rationale

---

## Data Notes

The `data/` folder is reserved for programme-approved datasets.

The Week 5, Week 6 and Week 7 work all use the programme-provided emergency department triage dataset titled `yaleemmlc_admissionprediction_triage.csv`. This raw dataset is not uploaded to the repository for data governance reasons.

Only derived outputs are included, such as summary CSVs, plots, feasibility documentation and notebook outputs. The Week 5, Week 6 and Week 7 notebooks are written to load the raw dataset locally when available.

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
* Qualitative interpretability assessment across all five models, including feature importance and SHAP-based explanations for the complex models
* Final benchmark table, per-class metrics, ESI Level 1 failure-mode breakdown and compute-cost reflection
* Confusion matrices for Random Forest, XGBoost and LightGBM, plus feature importance plots for Random Forest and the selected best-performing complex model
* Documented decision journal and cost–benefit memo recommending LightGBM as the preferred model for future development and potential deployment

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
* Week 7 final complex model benchmarking notebook (Random Forest, XGBoost, LightGBM), final benchmark table, interpretability assessment, decision journal and cost–benefit memo recommending LightGBM

---

## Reference Management

* Week 1 proposal documents related to AI-assisted ED risk stratification
* Week 2 updated proposal deliverable with Zotero-generated citations and bibliography
* Week 3 workflow mapping and systems-thinking deliverables, including AI plug-in points, workflow constraints and stakeholder considerations
* Week 4 ethics and safety submission, including a risk register and documented AI-harm case study
* Week 5 data exploration and feasibility memo outputs based on programme-provided ED triage data
* Week 6 baseline modelling and evaluation outputs based on programme-provided ED triage data
* Week 7 complex model benchmarking, final evaluation and cost–benefit analysis based on programme-provided ED triage data

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
