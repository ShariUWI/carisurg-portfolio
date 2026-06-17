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
* Week 0 reports and written submissions
* Week 1 interim and final preliminary proposal documents
* Week 2 updated proposal deliverable with Zotero-generated citations and bibliography
* Supporting documentation for project setup and review

The main clinical focus is the use of routinely collected triage data to support safer and earlier identification of high-risk emergency department patients.

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
│   └── week-2/
│       └── Week 2 updated proposal deliverable
│
├── notebooks/
│   ├── README.md
│   └── week-0/
│       └── Week 0 Jupyter notebooks
│
└── src/
    └── README.md
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

If you are using Google Colab, you can upload the notebook directly from the `notebooks/week-0/` folder and run the cells there.

---

## Usage

Open the Week 0 notebooks from the `notebooks/week-0/` folder.

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

---

## Documentation Guide

The `docs/` folder is organised into weekly subfolders:

* `docs/week-0/` contains Week 0 reports and supporting documents related to clinical triage data cleaning, MAP validation, visualisation, vital sign review, time management and digital ED triage model design.
* `docs/week-1/` contains the Week 1 interim submission and final preliminary proposal.
* `docs/week-2/` contains the Week 2 updated proposal deliverable with Zotero-generated citations and bibliography.

---

## Data Notes

The `data/` folder is reserved for programme-approved datasets.

The work presented uses programme-provided emergency department triage data. Sensitive, private or programme-controlled data is not uploaded to this repository unless permission is given. If a dataset is excluded from the repository, the notebook or documentation clearly explains where the data came from and how it was used.

---

## Main Outputs

This repository currently includes:

* Cleaned and documented Week 0 triage data notebooks
* Gender column cleaning report
* MAP cleaning report with clinical justifications
* Matplotlib visualisation report
* Vital sign review document
* Digital ED triage model pseudocode document
* Week 1 interim and final preliminary proposal documents
* Week 2 updated proposal deliverable with Zotero-generated citations and bibliography

---

## Reference Management

The Week 2 updated proposal uses Zotero-generated citations and bibliography. The reference library was organised to support citation hygiene, reproducibility and clear tracking of the peer-reviewed sources used in the proposal.

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
