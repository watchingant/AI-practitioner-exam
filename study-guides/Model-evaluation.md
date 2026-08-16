# Common Ways to Evaluate a Model

It depends heavily on **what kind of model you're evaluating**. There isn't one universal metric.

| Model / Task | Common evaluation metrics | What they tell you |
|---|---|---|
| **Binary classification** | Accuracy, Precision, Recall, F1, AUC-ROC, PR-AUC, Log Loss | How well the model distinguishes between two classes |
| **Multiclass classification** | Accuracy, Precision, Recall, F1, Log Loss, Confusion Matrix | How well it distinguishes multiple classes |
| **Regression** | MAE, MSE, RMSE, R², MAPE | How close predictions are to actual numerical values |
| **Clustering** | Silhouette Score, Davies-Bouldin Index, Calinski-Harabasz | How well the model finds meaningful groups |
| **Ranking / Recommendation** | Precision@K, Recall@K, NDCG, MAP, MRR | How well relevant items are ranked |
| **Generative AI / LLMs** | Perplexity, BLEU, ROUGE, BERTScore, human evaluation, LLM-as-judge | Quality/relevance of generated output |
| **Computer vision / Object detection** | IoU, mAP, Precision, Recall | How accurately objects are detected/localized |
| **Time series forecasting** | MAE, RMSE, MAPE, sMAPE, MASE | How accurately future values are predicted |

## Classification

### Accuracy

> "What percentage did I get right?"

$$
Accuracy = \frac{TP+TN}{TP+TN+FP+FN}
$$

Good when classes are reasonably balanced.

### Precision

> "When the model says positive, how often is it correct?"

$$
Precision = \frac{TP}{TP+FP}
$$

Important when **false positives are costly**.

Example: A spam detector marking legitimate emails as spam.

### Recall

> "Of all the actual positives, how many did I find?"

$$
Recall = \frac{TP}{TP+FN}
$$

Important when **false negatives are costly**.

Example: A disease detection system missing a sick patient.

### F1 Score

Combines precision and recall:

$$
F1 = 2\frac{Precision \times Recall}{Precision + Recall}
$$

Useful when you want a balance between precision and recall.

### AUC-ROC

Measures how well the model **ranks/separates positive and negative examples across thresholds**.

### PR-AUC

Area under the **Precision-Recall curve**.

This can be more informative than ROC-AUC when you're dealing with **highly imbalanced classes**.

For example:

- 99.9% normal transactions
- 0.1% fraudulent transactions

---

## Regression

If you're predicting a number—like house prices—some of the most common metrics are:

### MAE — Mean Absolute Error

> "On average, how far off am I?"

If MAE = $20,000, predictions are off by about $20K on average.

### MSE — Mean Squared Error

Penalizes large errors more heavily than MAE.

### RMSE — Root Mean Squared Error

Similar to MSE but brings the value back to the original units.

### R² — R-squared

Roughly:

> "How much of the variation in the target does my model explain?"

An R² of 0.80 means the model explains about 80% of the variance in the target under the usual interpretation.

---

## LLMs / Generative AI

This gets more complicated because there often isn't one objectively correct answer.

Common approaches include:

- **Perplexity** → how well a language model predicts text
- **BLEU** → similarity to reference text, historically common in translation
- **ROUGE** → overlap with reference text, commonly used for summarization
- **BERTScore** → semantic similarity
- **Human evaluation** → humans rate helpfulness, correctness, etc.
- **LLM-as-a-judge** → another model evaluates the output
- **Task-specific evaluations** → coding tests, math problems, factual QA, etc.

For modern LLMs, **task-specific evaluation + human/LLM evaluation** is often much more useful than relying on a single metric.

---

# An Important Concept: Generalization

You generally want to evaluate on data the model **didn't train on**.

A common setup is:

```text
Training data → Validation data → Test data
