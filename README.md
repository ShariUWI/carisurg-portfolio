# carisurg-week0

# CariSurg MedTech Pathways: Week 0 Portfolio

This repository contains my Week 0 submissions for the **CariSurg MedTech Pathways Programme**.

Week 0 focuses on onboarding, environment setup, Python readiness, basic data cleaning, exploratory data analysis, and clinical context development using a de-identified emergency triage dataset.

## Programme Context

The CariSurg MedTech Pathways Programme is a 13-week intensive designed to develop Caribbean talent in clinical AI, health technology, data analytics, and healthcare innovation.

Week 0 introduces the tools and workflow that will be used throughout the programme, including Google Colab, Google Drive, Python, pandas, GitHub, and basic clinical data analysis.

## Week 0 Objectives

The main objectives for Week 0 are to:

- Set up Google Drive and Google Colab
- Confirm that Python 3.10+ is available
- Create and use a public GitHub repository
- Load and inspect the Week 0 emergency triage dataset
- Clean selected dataset columns
- Perform basic exploratory data analysis
- Create simple data visualizations
- Explain a clinical vital sign in plain language
- Develop simple rule-based logic to identify at-risk patients
- Submit a final documented notebook

---

## Day 1 Submission: Gender Column Cleaning

The Day 1 task focused on cleaning the `Gender` column in the Week 0 emergency triage dataset.

The completed notebook includes:
- Loading the dataset into pandas
- Inspecting the original `Gender` column
- Identifying inconsistent values such as `0`, `1`, `Male`, `MALE`, `Female`, and `FEMALE`
- Standardizing the gender values into human-readable labels:
  - `Male`
  - `Female`
- Checking for missing or unmapped values
- Verifying the cleaned column using value counts
- Saving the cleaned dataset for future Week 0 tasks

Based on feedback, the updated version uses readable labels instead of numeric codes to improve clarity and interpretation.

### Files
- `S_Oliver_Week0_Day1_Gender_Cleaning_Updated.ipynb`
- `Gender_Cleaning_Report_Updated.pdf`

---

## Day 2 Submission: Advanced MAP Cleaning

The Day 2 task focused on cleaning the assigned `MAP` column. Since MAP is calculated from systolic and diastolic blood pressure, we first prepared `SBP` and `DBP`, then recalculated MAP using:

`MAP = (SBP + 2 × DBP) / 3`

This submission was completed as part of a group task. Our group worked collaboratively to clean and validate the assigned `MAP` column, with the process documented through the notebook, justification report, and evidence screenshots.

Group members: Shari Oliver, Tianna Bassaragh, Josiah-John Green, Gabrielle Johnson, and Ansarah Mohammed.

The submission includes:

- Completed Colab/Jupyter notebook
- MAP cleaning justification report
- Screenshots showing environment setup and final cleaning outputs
- Evidence of DBP, SBP, and MAP validation checks

### Files
- `S_Oliver_Week0_Tutorial2_Advanced_Cleaning.ipynb`
- `MAP_Cleaning_Report (Extra Justifications).pdf`
- `Assignment_2_Cleaned_MAP_Column.csv`
- `screenshots/`

### Evidence Screenshots

Screenshots are stored in the `screenshots/` folder and show the notebook outputs used to verify the cleaning process.

## Cleaning Considerations

Several considerations were made during the MAP cleaning process:

1. **Clinical dependency of MAP**  
   MAP is not an independent value. It is calculated from systolic blood pressure (`SBP`) and diastolic blood pressure (`DBP`) using:

   `MAP = (SBP + 2 × DBP) / 3`

   Because of this, we prepared `SBP` and `DBP` before recalculating `MAP`.

2. **Valid clinical ranges**  
   We used the following ranges to identify invalid values:

   - `SBP`: 50-250 mmHg
   - `DBP`: 30-150 mmHg
   - `MAP`: 40-180 mmHg

3. **Invalid values were not deleted immediately**  
   Values outside the valid range were converted to `NaN` instead of deleting patient rows. This preserved other useful patient information.

4. **Median imputation was used where appropriate**  
   Median imputation was selected because blood pressure values may contain outliers, and the median is less affected by extreme values than the mean.

## Submission Evidence

The repository includes:

- Completed Day 2 notebook
- MAP cleaning justification report
- Screenshots showing the cleaning outputs
    - `screenshots/tut2_environment_setup.png`
    - `screenshots/dbp_cleaning.png`
    - `screenshots/sbp_cleaning.png`
    - `screenshots/map_cleaning1.png`
    - `screenshots/map_nan_output.png`
- Evidence of the considerations used to clean SBP, DBP, and MAP

6. **MAP was recalculated from cleaned SBP and DBP**  
   After preparing `SBP` and `DBP`, we recalculated `MAP` using the clinical formula. This was more appropriate than only filtering or imputing the original MAP column.

7. **Clinically significant values were preserved**  
   One MAP value was slightly below the expected range. Since it was calculated from valid SBP and DBP values, it was preserved and flagged as a possible critically low MAP rather than treated as a data error.

---
## Day 3 Submission: Basic Data Visualisation with Matplotlib

The Day 3 task focused on creating clinically meaningful plots from the cleaned Mercer General ED triage dataset using `matplotlib`.

The goal of this task was not just to create graphs, but to create visualisations that answer specific clinical or data questions. Each plot includes a clear title, labelled axes, clinical reference lines or zones where appropriate, and saved image output.

### Individual Student Task

For my individual challenge, I created two main plots:

1. **Scatter Plot: Pulse vs MAP**
   - Clinical question: Do patients with lower MAP tend to have higher pulse rates, which may suggest possible physiological stress or compensation?
   - This plot compares pulse and mean arterial pressure.
   - Reference lines were added at `MAP = 65 mmHg` and `Pulse = 100 bpm`.
   - An annotation was added to identify the possible review zone for patients with low MAP and high pulse.

2. **Histogram: Distribution of SBP Values**
   - Clinical question: What is the distribution of systolic blood pressure values among patients in the Mercer General ED triage dataset?
   - This plot shows how SBP values are distributed across the cleaned dataset.
   - Shaded reference zones were added for SBP values below `90 mmHg` and above `180 mmHg`.

### Files Included

- `S_Oliver_Week0_Tutorial3_Visualisation.ipynb`
- `Matplotlib_Visualization_Report.pdf`
- `plots/pulse_vs_map.png`
- `plots/sbp_distribution_histogram.png`

### Cleaning and Clinical Context

The plots were created using the cleaned Week 0 triage dataset. Clinical reference lines and shaded zones were included to make the plots more meaningful for emergency department triage interpretation.

The main clinical considerations were:

- `MAP < 65 mmHg` may suggest reduced perfusion and may require clinical review.
- `Pulse > 100 bpm` may suggest tachycardia.
- `SBP < 90 mmHg` may suggest hypotension or shock risk.
- `SBP > 180 mmHg` may suggest severe hypertension and may require review.

Abnormal values were not automatically treated as errors because emergency department patients may present with genuinely abnormal vital signs.

### Submission Evidence

The repository includes:

- Completed Day 3 visualisation notebook
- Day 3 visualisation report
- Saved plot images generated from the notebook
- Evidence that the required histogram and scatter plot were produced

---

## Final Week 0 Submission: Combined Tasks 2–5

This final submission combines Tasks 2–5 into one documented Jupyter notebook. The purpose of the final notebook is to show how the Week 0 tasks connect together: visualising cleaned triage data, explaining the clinical meaning of vital signs, and designing basic rule-based logic for identifying at-risk patients.

### Included Tasks

**Task 2: Data Visualisation**
- Created clinically meaningful plots using `matplotlib`
- Included a histogram and scatter plot
- Used labelled axes, titles, clinical reference lines, shaded zones, and saved plot outputs
- Focused on vital signs such as SBP, MAP, and pulse

**Task 3: Clinical Context Write-Up**
- Selected a vital sign from the dataset
- Explained what the vital sign measures
- Identified normal and abnormal ranges
- Connected the vital sign to emergency department triage decision-making

**Task 4: Digital Triage Pseudocode**
- Designed pseudocode for a digital ED triage support model
- Used patient vital signs to assign risk levels
- Included clinical flags for abnormal values
- Added critical override rules for high-risk findings
- Included human-in-the-loop review so the model supports, rather than replaces, clinical judgement

### Final Submission Files

- `S_Oliver_Week0_Final_Tasks2-4.ipynb`
- `Week 0 Digital ED Triage Model Pseudocode.pdf`
- `Matplotlib_Visualization_Report.pdf`
- `plots/pulse_vs_map.png`
- `plots/sbp_distribution_histogram.png`

### Overall Purpose

This final notebook demonstrates how cleaned clinical data can be used to support emergency department triage. The visualisations help identify patterns in vital signs, the clinical write-up explains why vital signs matter, and the pseudocode shows how a digital system could flag patients who may be at risk.

The model is intended as a clinical decision-support tool. It does not replace nurses or clinicians, but helps organize patient information, identify abnormal vital signs, and highlight patients who may need urgent review.
