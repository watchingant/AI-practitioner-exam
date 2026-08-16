# Core ML Evaluation Concepts

Evaluating a Core ML model means measuring how well it performs for the real task, on data it has not seen during training. Good evaluation does more than produce a single score: it tests whether the model is accurate, reliable, efficient, and appropriate for the people and devices that will use it.

## 1. Separate training, validation, and test data

Use distinct data splits for distinct purposes:

- **Training set:** used to fit the model’s parameters.
- **Validation set:** used during development to compare model versions, tune settings, and choose thresholds.
- **Test set:** held back until final evaluation to estimate real-world performance.

The test set should represent the inputs the app will actually receive. If it is too similar to the training data, the results can be overly optimistic.

## 2. Match the metric to the task

The right evaluation metric depends on what the model predicts.

| Task | Useful metrics | What they indicate |
| --- | --- | --- |
| Classification | Accuracy, precision, recall, F1 score | Whether classes are predicted correctly and which errors matter most |
| Object detection | Precision, recall, mean average precision (mAP) | Whether objects are found and localized correctly |
| Regression | MAE, RMSE, R² | How close numeric predictions are to the true values |
| Segmentation | Intersection over Union (IoU), Dice score | How closely predicted regions match ground truth |
| Ranking or recommendations | Precision@k, recall@k, NDCG | Quality of the top results shown to a user |

**Accuracy alone can be misleading** when classes are imbalanced. For example, a model that predicts “no defect” for every image may achieve high accuracy if defects are rare, while failing at the job it was built to do.

## 3. Read a confusion matrix

For a binary classifier, a confusion matrix separates predictions into four outcomes:

|  | Predicted positive | Predicted negative |
| --- | --- | --- |
| Actually positive | True positive | False negative |
| Actually negative | False positive | True negative |

From these counts:

- **Precision** = true positives / predicted positives. Of the positive predictions, how many were right?
- **Recall** = true positives / actual positives. Of the real positives, how many did the model find?
- **F1 score** balances precision and recall.

The preferred trade-off is product-specific. A safety alert may prioritize recall to avoid missed hazards; a costly manual-review workflow may prioritize precision to avoid unnecessary alerts.

## 4. Evaluate confidence and thresholds

Many Core ML classifiers provide a predicted label plus class probabilities. A probability threshold controls when the app accepts a prediction or defers to another action.

Changing the threshold changes the balance of false positives and false negatives. Evaluate several thresholds on validation data, select one based on the product’s error costs, and confirm the choice on held-out test data.

Confidence is not always perfectly calibrated: a prediction reported as 90% confident should ideally be correct about 90% of the time. Calibration checks can reveal when model probabilities are overconfident or underconfident.

## 5. Test representative and difficult cases

Aggregate scores can hide important failures. Break results down by conditions that matter to the application, such as:

- device model and operating-system version;
- lighting, noise, motion, orientation, or image quality;
- locale, language, accents, or writing styles;
- user-relevant demographic groups, where appropriate and responsibly collected;
- rare classes and edge cases.

This analysis helps identify distribution shift: production inputs that differ from the examples used to train the model.

## 6. Evaluate on-device performance

Core ML runs models on Apple devices, so model quality includes runtime behavior. Measure on the lowest-capability devices you intend to support:

- **Latency:** time required for one prediction.
- **Throughput:** predictions completed over time, especially for camera or streaming workflows.
- **Memory use:** working memory needed to load and run the model.
- **Energy impact:** battery cost during sustained use.
- **Model size:** download, storage, and app-bundle impact.

A highly accurate model may still create a poor experience if it is too slow, drains the battery, or delays a real-time interface.

## 7. Validate the full Core ML pipeline

Evaluate the model as integrated into the app, not only in a training environment. Confirm that preprocessing and postprocessing match the training pipeline:

- input image size, orientation, color format, and normalization;
- text tokenization and vocabulary handling;
- audio sample rate and windowing;
- output label mapping, thresholds, and coordinate conversions.

Small mismatches in these steps can significantly lower production accuracy even when the underlying model is sound.

## 8. Monitor after release

Model evaluation continues after deployment. When privacy and product design permit, monitor aggregate outcomes, user corrections, failures, latency, and changes in input characteristics. Re-evaluate when the app, supported devices, or real-world data changes.

Use a feedback loop:

1. Measure production behavior.
2. Identify meaningful failure patterns.
3. Collect or label representative new data with appropriate consent and privacy protections.
4. Retrain or adjust the model.
5. Compare the candidate model against the current model on the same locked test set.

## Practical evaluation checklist

- Define the user outcome and the cost of each error type.
- Keep a realistic, untouched test set.
- Report task-appropriate metrics, not only accuracy.
- Inspect per-class and per-condition results.
- Choose and validate confidence thresholds.
- Test the integrated Core ML pipeline on target hardware.
- Measure latency, memory, energy, and model size.
- Reassess performance as production data and devices evolve.

Strong Core ML evaluation combines statistical validity with real device testing and product judgment. The result is not simply a model with a high score, but one that performs dependably in the conditions where it matters.

