# CariSurg Portfolio

## Shari Oliver's CariSurg MedTech Pathways Portfolio

## 60-Second Summary

| Question                                | Answer                                                                                                                                                                       |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **What is this project?**               | My CariSurg MedTech Pathways portfolio documenting clinical AI, emergency department triage data work, proposal development and project documentation.                       |
| **Who is it for?**                      | CariSurg tutors, clinical reviewers and members of the Clinical AI & Innovation Unit who need to quickly review my work.                                                     |
| **How do I install and run it?**        | Clone the repository, install the requirements and open the notebooks in Jupyter Lab or Google Colab. See the Installation and Usage sections below for copy-paste commands. |
| **Where does the data come from?**      | The work uses programme-provided emergency department triage data. Sensitive or programme-controlled datasets are not uploaded unless permission is given.                   |
| **Who built it and how can I connect?** | Built by Shari Oliver for the CariSurg MedTech Pathways Programme. LinkedIn: [Shari Oliver](https://www.linkedin.com/in/shari-oliver-87906b1ba/).                            |

---

## Purpose

The purpose of this repository is to keep my CariSurg programme work organised, reproducible and audit-ready.

It includes:

* Week 0 Jupyter notebooks on emergency department triage data cleaning, validation and visualisation
* Week 0 reports, written reflections and exploratory plots
* Week 1 proposal documents on AI-assisted early risk stratification in emergency department triage
* Week 2 updated proposal deliverable with Zotero-generated citations and bibliography
* Week 3 workflow mapping, systems thinking and refined proposal documentation
* Week 4 ethics, safety, risk register and AI-harm case study documentation
* Week 5 final data exploration, data-quality visualisation dashboard, feasibility memo and top-10 clinically justified feature shortlist
* Week 6 interim baseline modelling, initial model evaluation, random baseline comparison and draft confusion matrix artefact
* Supporting documentation for project setup and review


The main clinical focus is the use of routinely collected triage data to support safer and earlier identification of high-risk emergency department patients. As the portfolio develops, the project also considers workflow fit, stakeholder needs, ethical risks, equity, accountability and safe implementation of AI-assisted triage support.


---

## Repository Structure

```text
carisurg-portfolio/
│
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
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
│   └── week-5/
│    └── Week 5 final feasibility memo, memo outline, summary CSVs and top-10 feature shortlist
    └── week-6/
│       └── Week 6 interim model evaluation outputs and supporting documentation
│
│
├── notebooks/
│   ├── Week 0 Jupyter notebooks
│   └── week-5/
│       └── Week 5 final exploration and data profiling notebooks
│   └── week-6/
│       └── Week 6 interim baseline modelling notebook
│
├── plots/
│   ├── week-0/
│   │   └── Week 0 exploratory plots
│   ├── week-4/
│   │   └── Week 4 workflow diagram output
│   └── week-5/
│       └── Week 5 data-quality and exploratory visualisations
│   └── week-6/
│       └── Week 6 interim confusion matrix and model evaluation plots
└── src/
└── Future reusable scripts or functions

```

---

## Installation

To review or run the notebooks locally, clone this repository and install the required Python packages.

```bash
git clone https://github.com/ShariUWI/carisurg-portfolio.git
cd carisurg-portfolio
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

For Windows PowerShell, use:

```bash
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

If you are using Google Colab, you can upload notebooks directly from the relevant weekly notebook folder, such as `notebooks/week-0/`, `notebooks/week-5/` or `notebooks/week-6/`, and run the cells there.

---

## Usage

```bash
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

```text
notebooks/week-5/
```

Week 5 supporting outputs are stored in:

```text
docs/week-5/
plots/week-5/
```

The Week 5 final notebook focuses on exploration of the programme-provided ED triage dataset, `yaleemmlc_admissionprediction_triage.csv`, including missingness analysis, ESI target review, demographic and fairness-sensitive review, vital sign exploration, clinical plausibility checks, chief complaint review, feature-signal review and early feasibility assessment.

The raw dataset is not included in this repository for data governance reasons. The notebook is written to load the dataset locally when available.

Week 6 interim baseline modelling work is stored in:

```text
notebooks/week-6/
---
docs/week-6/
plots/week-6/


## Documentation Guide

The `docs/` folder is organised into weekly subfolders.
The recommended document review order is

1. `docs/week-0/` — Week 0 reports and written submissions
2. `docs/week-1/` — Week 1 preliminary proposal documents
3. `docs/week-2/` — Week 2 updated proposal deliverable
4. `docs/week-3/` — Week 3 workflow mapping, systems thinking and refined proposal documents
5. `docs/week-4/` — Week 4 ethics, safety, risk register and AI-harm case study documents
6. `docs/week-5/` — Week 5 final feasibility memo, memo outline, data-quality summaries and top-10 feature shortlist
7. `docs/week-6/` — Week 6 interim model evaluation outputs, draft confusion matrix artefact and supporting documentation

---

## Data Notes


The `data/` folder is reserved for programme-approved datasets.

The Week 5 and Week 6 work use the programme-provided emergency department triage dataset titled `yaleemmlc_admissionprediction_triage.csv`. This raw dataset is not uploaded to the repository for data governance reasons.

Only derived outputs are included, such as summary CSVs, plots, feasibility documentation and notebook outputs. The Week 5 and Week 6 notebooks are written to load the raw dataset locally when available.

Sensitive, private or programme-controlled data should not be committed to this repository unless explicit permission is given.


## Week 5 Final Deliverables

The Week 5 final submission includes:

* Final exploration and data profiling notebook
* Data-quality visualisation dashboard
* 3-page clinical feasibility memo
* Top-10 feature shortlist with clinical reasoning
* Derived summary CSVs and supporting plots

The raw dataset `yaleemmlc_admissionprediction_triage.csv` is not included in the repository for data governance reasons.

## Week 6 Interim Deliverables

The Week 6 interim submission includes:

* Interim baseline modelling notebook
* Logistic regression baseline model
* Stratified random baseline comparison
* Initial evaluation metrics including accuracy, precision, recall and F1-score
* Draft logistic regression confusion matrix artefact

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
* Week 6 interim baseline modelling notebook, initial evaluation metrics, stratified random baseline comparison and draft confusion matrix artefact

---

## Reference Management
* Week 1 proposal documents related to AI-assisted ED risk stratification
* Week 2 updated proposal deliverable with Zotero-generated citations and bibliography
* Week 3 workflow mapping and systems-thinking deliverables, including AI plug-in points, workflow constraints and stakeholder considerations
* Week 4 ethics and safety interim submission, including a draft risk register and documented AI-harm case study
* Week 5 data exploration and feasibility memo outputs based on programme-provided ED triage data
* Week 6 baseline modelling and evaluation outputs based on programme-provided ED triage data

## Zotero Reference libraries
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

---

## License

This repository is licensed under the MIT License. See the `LICENSE` file for details.

---

## Connect

**Shari Oliver**
CariSurg MedTech Pathways Scholar
Aspiring Medical Physicist | Healthcare AI & Clinical Innovation

**LinkedIn:** [Shari Oliver](https://www.linkedin.com/in/shari-oliver-87906b1ba/)
