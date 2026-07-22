# Decision Journal — Week 7 Model Selection

## Context

- This week focused on comparing the baseline Logistic Regression model with three more complex machine learning models: Random Forest, XGBoost and LightGBM.
- All models were trained and evaluated using the same training and testing split and random seed from Week 6 to ensure that performance comparisons were fair and reproducible.

## Alternatives Considered

- **Logistic Regression** – retained as the baseline due to its simplicity, fast prediction time and excellent interpretability, although its predictive performance was lower than the best-performing complex models.
- **Random Forest** – considered because it is a robust ensemble learning method with reasonable interpretability through feature importance, but it achieved the weakest overall predictive performance and the slowest inference time.
- **XGBoost** – delivered strong predictive performance and useful feature importance analysis, making it a competitive option despite requiring a longer training time than LightGBM.

## Decision

**LightGBM was selected as the preferred model because it achieved the strongest overall balance of predictive performance, computational efficiency and practical interpretability.**

## Reasoning

- LightGBM achieved the highest overall accuracy (66.19%) and the highest Macro F1 score among all evaluated models, indicating the best overall classification performance.
- It required the shortest training time (9.74 seconds) and the fastest inference time (10.01 ms per prediction), making it well suited for real-time emergency department triage.
- Although more complex than Logistic Regression, LightGBM remains sufficiently interpretable through feature importance analysis and SHAP values, allowing clinicians to understand the factors influencing individual predictions.

## Things Not Yet Known

- Additional validation is required to determine whether the model maintains similar performance when applied to data from other hospitals or different patient populations.
- Further work is needed to evaluate clinical acceptance, fairness across demographic groups and the effectiveness of explanation methods in supporting real-world decision-making.
