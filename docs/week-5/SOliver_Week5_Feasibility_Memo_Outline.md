# Week 5 Feasibility Memo Outline

## One-Sentence Verdict

The dataset appears suitable for continued triage modelling exploration, but only with important caveats around missingness, class imbalance, data quality and local validation.

## Dataset Summary

This dataset contains de-identified emergency department arrival records with demographic variables, triage vital signs, Emergency Severity Index (ESI) triage levels and chief complaint indicators. The dataset is intended to support early exploration of whether routinely collected ED data can be used to build a triage support model.

## Top 3 Quality Concerns

1. **Missingness in key clinical fields**  
   Some variables may have missing values, which could affect model reliability if important triage information such as vital signs or presenting complaints is incomplete.

2. **Potential imbalance in ESI triage levels**  
   If some ESI levels are much more common than others, a model may perform well overall while still performing poorly for the highest-acuity or lowest-frequency groups.

3. **Single-site data limitations**  
   The dataset reflects one hospital’s patient population, documentation habits and workflow. This may limit how well a future model generalises to other ED settings.

## Top 3 Reasons to Proceed

1. **Clinically relevant triage features are available**  
   The dataset includes important variables such as age, vital signs, ESI level and chief complaint flags.

2. **The target variable is clinically meaningful**  
   ESI provides a recognised triage acuity label that can support baseline modelling.

3. **The dataset is rich enough for exploratory modelling**  
   With many clinical and complaint-related features, the dataset is suitable for Week 6 baseline modelling once quality concerns are documented.

## Caveats

This dataset should not be treated as immediately ready for clinical deployment. Further cleaning, missingness review, outlier checking, subgroup analysis and local validation would be required before any AI-assisted triage tool could be considered for real-world use.

## Initial Top-10 Feature Shortlist

1. Respiratory rate  
2. Oxygen saturation  
3. Systolic blood pressure  
4. Heart rate  
5. Temperature  
6. Glucose  
7. Age  
8. Arrival mode  
9. Chest pain chief complaint  
10. Shortness of breath chief complaint