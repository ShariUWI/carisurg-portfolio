# Week 7 Cost–Benefit Memo
## Evaluation of Complex Machine Learning Models for Emergency Severity Index Prediction

### 1. Verdict

**LightGBM is recommended as the preferred model for future deployment because it achieved the best overall balance of predictive performance, computational efficiency and practical interpretability when compared with the baseline Logistic Regression model and the other complex machine learning models.** While no model is perfect, LightGBM demonstrated the strongest combination of accuracy, training efficiency and prediction speed, making it the most suitable candidate for supporting Emergency Severity Index (ESI) classification.

---

## 2. Dataset and Methods Recap

The objective of this study was to evaluate whether a more complex machine learning model could improve the prediction of Emergency Severity Index (ESI) categories compared with the baseline Logistic Regression model developed previously.

To ensure a fair comparison, the same training and testing split from Week 6 was reused for every model. A fixed random seed (`RANDOM_SEED = 42`) was also used throughout the experiments to ensure that all results were reproducible.

Four models were evaluated:

- Logistic Regression (baseline)
- Random Forest
- XGBoost
- LightGBM

Each model was assessed using the following performance measures:

- Accuracy
- Precision
- Recall
- Macro F1-score
- Training time
- Inference time per prediction

Interpretability was also considered because clinical decision support systems should provide explanations that clinicians can understand and trust.

---

## 3. Benchmark Comparison

| Model | Accuracy | Precision | Recall | Macro F1 | Training Time (s) | Inference Time (ms) | Interpretability |
|-------|---------:|----------:|-------:|---------:|------------------:|--------------------:|------------------|
| Logistic Regression | 0.5924 | 0.4256 | 0.6436 | 0.4299 | 23.3209 | 11.5944 | Excellent – coefficients directly explain predictions. |
| Random Forest | 0.4906 | 0.3639 | 0.4338 | 0.3403 | 19.8585 | 91.0090 | Moderate – feature importance provides global explanations. |
| XGBoost | 0.6275 | 0.5539 | 0.5446 | 0.4964 | 26.6963 | 10.3501 | Good – feature importance and SHAP values explain predictions. |
| **LightGBM** | **0.6619** | **0.5477** | **0.5157** | **0.4973** | **9.7358** | **10.0149** | Good – feature importance and SHAP values explain predictions. |

The benchmark results show that LightGBM achieved the highest overall accuracy and Macro F1-score while also requiring the shortest training time and fastest inference time. Although Logistic Regression remains the easiest model to interpret, its predictive performance was lower than the leading gradient boosting models.

---

## 4. Arguments Supporting the Recommended Model

### 1. Strongest Overall Predictive Performance

LightGBM achieved the highest overall accuracy (66.19%) and the highest Macro F1-score among all evaluated models. These results indicate that it classified Emergency Severity Index categories more effectively than the baseline Logistic Regression model as well as the other complex models considered.

### 2. Excellent Computational Efficiency

Despite being a sophisticated gradient boosting algorithm, LightGBM completed training in only 9.74 seconds, making it the fastest model evaluated. Its inference time of approximately 10 milliseconds per prediction also makes it suitable for real-time emergency department workflows where rapid clinical decision support is essential.

### 3. Acceptable Interpretability

Although LightGBM is more complex than Logistic Regression, it still provides meaningful explanations through feature importance analysis and SHAP values. These methods allow clinicians and technical staff to identify the variables that contributed most strongly to individual predictions and overall model behaviour. This level of interpretability is generally sufficient for supporting clinical governance and model validation.

---

## 5. Arguments Against the Recommended Model

### 1. Reduced Transparency

Unlike Logistic Regression, LightGBM does not provide coefficients that can be interpreted directly. Understanding why a prediction was made requires additional explanation techniques such as SHAP values or feature importance plots.

### 2. Greater Implementation Complexity

Deploying and maintaining LightGBM requires additional software dependencies, hyperparameter tuning and monitoring compared with simpler statistical models. This increases the technical expertise required for long-term maintenance.

### 3. Risk of Reduced Generalisation

Although LightGBM performed best on the available dataset, there is no guarantee that identical performance will be achieved when the model is applied to hospitals with different patient populations, workflows or data collection practices. External validation would therefore be required before clinical deployment.

---

## 6. Risks and Unknowns

Several important considerations remain before a model such as LightGBM could be adopted within a clinical environment.

First, the evaluation was performed using historical data rather than a live emergency department setting. Real-world performance may differ because patient populations and operational conditions can change over time.

Secondly, the current evaluation focused primarily on predictive performance and computational efficiency. Additional work should investigate fairness across demographic groups, robustness to missing or noisy data and long-term model stability.

Finally, while feature importance and SHAP values improve interpretability, successful adoption also depends on clinician trust, regulatory approval and appropriate governance procedures. Machine learning models should therefore be viewed as decision-support tools rather than replacements for professional clinical judgement.

---

## 7. Final Recommendation

Based on the benchmark results, **LightGBM is recommended as the preferred model for future development and potential deployment**. It achieved the highest overall predictive performance while simultaneously providing the fastest training and inference times. These characteristics make it well suited to environments such as emergency departments where timely and accurate predictions are essential.

However, this recommendation does **not** solve every challenge associated with clinical decision support. The model does not eliminate the need for clinician oversight, guarantee fairness across all patient groups or ensure perfect prediction accuracy. Before deployment, further external validation, fairness assessment and prospective clinical evaluation should be completed to ensure that the model performs safely and reliably within routine healthcare practice.