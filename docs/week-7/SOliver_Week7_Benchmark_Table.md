# Week 7 Benchmark Comparison

| Model | Accuracy | Precision | Recall | Macro F1 | Training Time (s) | Inference Time (ms) | Interpretability |
|-------|---------:|----------:|-------:|---------:|------------------:|--------------------:|------------------|
| Logistic Regression | 0.5924 | 0.4256 | 0.6436 | 0.4299 | 23.3209 | 11.5944 | Excellent – coefficients directly explain predictions. |
| Random Forest | 0.4906 | 0.3639 | 0.4338 | 0.3403 | 19.8585 | 91.0090 | Moderate – feature importance provides global explanations. |
| XGBoost | 0.6275 | 0.5539 | 0.5446 | 0.4964 | 26.6963 | 10.3501 | Good – feature importance and SHAP values explain predictions. |
| **LightGBM** | **0.6619** | **0.5477** | **0.5157** | **0.4973** | **9.7358** | **10.0149** | Good – feature importance and SHAP values explain predictions. |

## Interpretability Assessment

Logistic Regression remains the easiest model to interpret because the influence of each feature can be understood directly from the learned coefficients.

Among the complex models, XGBoost and LightGBM support feature importance analysis and SHAP explanations, allowing individual predictions to be interpreted within approximately one minute. The feature importance analysis identified arrival by ambulance and several presenting complaints as the strongest contributors to prediction.
