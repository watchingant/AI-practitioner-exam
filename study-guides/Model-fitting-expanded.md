
````markdown
# Model Fitting in Machine Learning

## What Is Model Fitting?

**Model fitting** is the process of training a machine-learning model so that it learns the relationship or patterns between the input data and the desired output.

In simple terms:

> **Model fitting = teaching a model how to make predictions from data.**

For example, suppose we want to predict house prices.

We might have:

| Size | Bedrooms | Location | Actual Price |
|---:|---:|---|---:|
| 1,500 sq ft | 3 | Atlanta | $350,000 |
| 2,000 sq ft | 4 | Atlanta | $450,000 |
| 2,500 sq ft | 4 | Atlanta | $550,000 |

The model looks at these examples and tries to learn relationships such as:

```text
House characteristics
        ↓
    ML Model
        ↓
Predicted house price
````

The goal is for the model to learn patterns that allow it to make good predictions on **new houses it has never seen before**.

---

# 1. What Does "Fit" Mean?

When we say:

> "We fit a model to the data."

we mean that we allow the model to adjust its internal parameters so that its predictions become closer to the correct answers.

For example:

```text
Input → Model → Prediction
```

Suppose the actual price is:

```text
$400,000
```

but the model predicts:

```text
$350,000
```

The model has made an error.

During training, the model adjusts its parameters to reduce these errors.

Conceptually:

```text
Data
 ↓
Model
 ↓
Prediction
 ↓
Calculate Error
 ↓
Adjust Parameters
 ↓
Better Prediction
 ↓
Repeat
```

This process is **model fitting**.

---

# 2. Parameters

A machine-learning model contains **parameters** that it learns from the training data.

For example, a simple linear model might look like:

$$
y = wx + b
$$

Where:

* `x` = input
* `y` = prediction
* `w` = learned weight
* `b` = learned bias/intercept

During training, the model learns values for `w` and `b`.

For example:

```text
Before training:

w = 0.2
b = 10

        ↓
    Training
        ↓

After training:

w = 2.7
b = 15
```

The values are adjusted to make the model's predictions better.

---

# 3. Loss Function

The model needs a way to measure **how wrong its predictions are**.

This is the job of the **loss function**.

For example:

```text
Actual value:     100
Prediction:        80

Error:             20
```

The loss function converts prediction errors into a numerical value.

Conceptually:

```text
Prediction
    ↓
Compare with actual value
    ↓
Loss
```

A common regression loss is **Mean Squared Error (MSE)**:

$$
MSE = \frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y}_i)^2
$$

The training process attempts to **minimize the loss**.

---

# 4. Optimization

Once the model knows how wrong it is, it needs to determine:

> "How should I change my parameters to make the error smaller?"

This is the job of an **optimization algorithm**.

One of the most common is:

**Gradient Descent**

Conceptually:

```text
Current parameters
        ↓
Calculate loss
        ↓
Calculate gradients
        ↓
Adjust parameters
        ↓
Lower loss
        ↓
Repeat
```

The model gradually moves toward parameter values that produce lower loss.

---

# 5. Gradient Descent

Imagine the loss function as a landscape:

```text
Loss
 ↑
 |       *
 |      / \
 |     /   \
 |    /     \
 |   /       \____
 |__/              \____
 +------------------------→ Parameters
```

The goal is to find a point where the loss is as small as possible.

Gradient descent repeatedly moves the model in the direction that reduces the loss.

```text
High Loss
    ↓
    ↓
Lower Loss
    ↓
    ↓
Lowest Loss
```

This process happens many times during training.

---

# 6. Epochs

An **epoch** is one complete pass through the training dataset.

Suppose you have:

```text
10,000 training examples
```

One epoch means the model has processed all 10,000 examples once.

For example:

```text
Epoch 1 → Model sees all training data
Epoch 2 → Model sees all training data again
Epoch 3 → Model sees all training data again
...
```

As training continues, the model typically gets better at fitting the training data.

---

# 7. Batches

Large datasets are usually divided into smaller groups called **batches**.

For example:

```text
Training dataset = 100,000 examples

Batch size = 100

Batch 1 → examples 1–100
Batch 2 → examples 101–200
Batch 3 → examples 201–300
...
```

The model updates its parameters after processing a batch.

This is usually much more computationally efficient than processing the entire dataset at once.

---

# 8. Training Loop

Putting the concepts together:

```text
                 Training Data
                      ↓
                  Batch Data
                      ↓
                    Model
                      ↓
                 Prediction
                      ↓
                 Loss Function
                      ↓
                   Loss
                      ↓
                Gradient Descent
                      ↓
              Update Parameters
                      ↓
                  Next Batch
                      ↓
                    Repeat
```

After all batches have been processed:

```text
                One Epoch
```

Then the process can repeat for another epoch.

---

# 9. Underfitting

**Underfitting** occurs when the model is too simple or insufficiently trained to capture the underlying patterns in the data.

Example:

```text
Training performance:   Poor
Validation performance: Poor
```

The model hasn't learned enough.

### Typical causes

* Model is too simple
* Not enough training
* Insufficient features
* Excessive regularization
* Poor model architecture

### Conceptually

```text
Real relationship
     ~~~~~~~~
    /        \
   /          \

Model
──────────────
```

The model is too simple to represent the actual relationship.

---

# 10. Good Fit

A good model learns the important patterns without simply memorizing the training examples.

Example:

```text
Training performance:   Good
Validation performance: Good
Test performance:       Good
```

Conceptually:

```text
Training data
     ↓
Learn underlying patterns
     ↓
Good predictions
     ↓
New unseen data
     ↓
Good predictions
```

This is what we ultimately want.

---

# 11. Overfitting

**Overfitting** occurs when the model learns the training data too closely, including noise or patterns that don't generalize to new data.

Example:

```text
Training performance:   Excellent
Validation performance: Poor
Test performance:       Poor
```

The model may effectively be memorizing the training examples.

### Conceptually

```text
Actual relationship
     ~~~~~~~~

Overly complex model

  /\    /\
 /  \__/  \___/\_
/              \
```

The model is following the training data too closely rather than learning the underlying pattern.

---

# 12. Underfitting vs. Good Fit vs. Overfitting

|                      | Underfitting | Good Fit    | Overfitting |
| -------------------- | ------------ | ----------- | ----------- |
| **Model complexity** | Too low      | Appropriate | Too high    |
| **Training error**   | High         | Low         | Very low    |
| **Validation error** | High         | Low         | High        |
| **Generalization**   | Poor         | Good        | Poor        |
| **Bias**             | High         | Balanced    | Low         |
| **Variance**         | Low          | Balanced    | High        |

The key pattern is:

```text
                 Model Complexity
                        →
                        
Underfitting     Good Fit     Overfitting
     ↓               ↓             ↓
 High Bias       Balanced      High Variance
     ↓               ↓             ↓
Too simple      Generalizes    Too complex
                well            / memorizes
```

---

# 13. Bias-Variance Tradeoff

The relationship between underfitting and overfitting is often described as the:

> **Bias-Variance Tradeoff**

### High Bias

The model makes overly simplistic assumptions.

```text
High Bias
    ↓
Underfitting
```

### High Variance

The model is too sensitive to the particular training data.

```text
High Variance
    ↓
Overfitting
```

The goal is to find a balance:

```text
        Bias
          ↓
          \
           \
            → Best Generalization
           /
          /
       Variance
```

---

# 14. Training Error vs. Validation Error

One of the most useful ways to understand model fitting is to compare training and validation performance.

### Underfitting

```text
Training Error:   HIGH
Validation Error: HIGH
```

The model performs poorly everywhere.

### Good Fit

```text
Training Error:   LOW
Validation Error: LOW
```

The model performs well on both training and unseen validation data.

### Overfitting

```text
Training Error:   VERY LOW
Validation Error: HIGH
```

The model performs extremely well on training data but poorly on unseen data.

---

# 15. Learning Curves

A **learning curve** shows how model performance changes as training progresses or as more training data is added.

For example:

```text
Error
 ↑
 |\
 | \
 |  \       Validation
 |   \______/--------
 |
 |\
 | \
 |  \______________ Training
 |
 +--------------------------→ Training
```

Learning curves can help identify:

* Underfitting
* Overfitting
* Whether more training data might help
* Whether the model needs more or less complexity

---

# 16. Regularization

**Regularization** is a technique used to reduce overfitting.

The idea is:

> Don't allow the model to become unnecessarily complex.

Instead of simply minimizing prediction error, the model also receives a penalty for complexity.

Conceptually:

$$
Total\ Loss = Prediction\ Loss + Complexity\ Penalty
$$

Common regularization techniques include:

* **L1 regularization**
* **L2 regularization**
* **Dropout**
* **Early stopping**
* **Data augmentation**

---

# 17. Hyperparameters

It's important to distinguish **parameters** from **hyperparameters**.

### Parameters

Learned automatically during training.

Examples:

```text
Weights
Biases
```

### Hyperparameters

Chosen by the developer/data scientist.

Examples:

```text
Learning rate
Number of layers
Number of neurons
Batch size
Number of epochs
Regularization strength
```

For example:

```text
Learning rate = 0.001
Batch size    = 32
Epochs        = 20
```

The model does not normally discover these values itself during ordinary training. They are configuration choices.

---

# 18. Model Fitting vs. Model Evaluation

These concepts are related but different.

### Model fitting

> **Learn parameters from training data.**

```text
Training Data
     ↓
   Model
     ↓
Learn Parameters
```

### Model evaluation

> **Measure how well the trained model performs.**

```text
Unseen Data
     ↓
Trained Model
     ↓
Predictions
     ↓
Evaluation Metrics
```

For example:

```text
FIT:

Training data
     ↓
Model learns
     ↓
Weights are updated


EVALUATE:

Test data
     ↓
Trained model
     ↓
Predictions
     ↓
Accuracy / F1 / RMSE / AUC
```

---

# 19. Training, Validation, and Test Data

A common workflow is:

```text
                 Complete Dataset
                       |
          +------------+------------+
          |            |            |
          ↓            ↓            ↓
      Training     Validation      Test
          |            |            |
          ↓            ↓            ↓
      Fit model    Tune model    Final evaluation
```

### Training Data

Used to **fit the model**.

### Validation Data

Used during development to:

* Compare models
* Tune hyperparameters
* Select model architecture
* Detect overfitting

### Test Data

Used for the final evaluation of the selected model.

The test set should ideally remain untouched until the final evaluation.

---

# 20. Example: House Price Prediction

Suppose we want to predict house prices.

### Step 1: Collect Data

```text
House size
Number of bedrooms
Location
Age
Garage
Actual price
```

### Step 2: Split Data

```text
80% → Training
10% → Validation
10% → Test
```

### Step 3: Fit the Model

The model learns relationships such as:

```text
Larger house → generally higher price
More bedrooms → generally higher price
Location → affects price
```

### Step 4: Evaluate

Suppose we get:

```text
Training RMSE:   $15,000
Validation RMSE: $18,000
Test RMSE:       $19,000
```

This looks reasonably healthy.

But suppose instead:

```text
Training RMSE:   $2,000
Validation RMSE: $30,000
Test RMSE:       $32,000
```

That is a strong sign of **overfitting**.

---

# 21. Model Fitting in Deep Learning

The same concepts apply to neural networks.

A neural network might look like:

```text
Input
  ↓
Layer 1
  ↓
Layer 2
  ↓
Layer 3
  ↓
Output
```

During training:

```text
Input
  ↓
Forward Pass
  ↓
Prediction
  ↓
Loss
  ↓
Backpropagation
  ↓
Gradient Descent
  ↓
Update Weights
  ↓
Repeat
```

### Forward Pass

The input moves through the network to produce a prediction.

### Loss

The prediction is compared with the correct answer.

### Backpropagation

The model calculates how each parameter contributed to the error.

### Optimization

An optimizer updates the parameters to reduce future error.

This process repeats over many batches and epochs.

---

# 22. The Complete Model-Fitting Process

A simplified view:

```text
                    DATA
                      ↓
               Split the Data
                      ↓
             +--------+--------+
             ↓        ↓        ↓
         Training Validation  Test
             ↓        ↓        ↓
             |        |        |
             ↓        ↓        |
        Fit Model   Tune Model |
             ↓        ↓        |
             +--------+        |
                      ↓        |
                 Final Model   |
                      ↓        |
                      +--------+
                           ↓
                     Test Model
                           ↓
                    Evaluate Model
                           ↓
                 Check Generalization
                           ↓
              +------------+------------+
              ↓                         ↓
         Good Fit                  Overfitting
              ↓                         ↓
       Deploy / Use             Improve Model
```

---

# 23. The Most Important Mental Model

Think about model fitting as a progression:

```text
Too Simple
    ↓
Underfitting
    ↓
Learn More
    ↓
Good Fit
    ↓
Increase Complexity
    ↓
Overfitting
```

The goal is **not** to maximize training performance.

The goal is:

> **Find the model that learns the underlying patterns and performs well on unseen data.**

---

# 24. Key Terminology

| Term                 | Meaning                                                       |
| -------------------- | ------------------------------------------------------------- |
| **Model fitting**    | Learning model parameters from training data                  |
| **Training**         | The overall process of learning from data                     |
| **Parameter**        | Value learned by the model                                    |
| **Hyperparameter**   | Configuration chosen before/during training                   |
| **Loss function**    | Measures how wrong predictions are                            |
| **Optimizer**        | Adjusts model parameters to reduce loss                       |
| **Gradient descent** | Common optimization method                                    |
| **Epoch**            | One complete pass through the training data                   |
| **Batch**            | A subset of training examples                                 |
| **Overfitting**      | Model fits training data too closely                          |
| **Underfitting**     | Model is too simple to learn the patterns                     |
| **Generalization**   | Performance on unseen data                                    |
| **Bias**             | Error caused by overly simplistic assumptions                 |
| **Variance**         | Sensitivity to the particular training data                   |
| **Regularization**   | Techniques used to reduce overfitting                         |
| **Cross-validation** | Repeated train/validation splits for more reliable evaluation |

---

# 25. The Big Picture

The concepts connect like this:

```text
                     Machine Learning
                           |
                           ↓
                         Data
                           |
                           ↓
                    Model Fitting
                           |
            +--------------+--------------+
            ↓              ↓              ↓
         Training        Loss        Optimization
                           |              |
                           +------+-------+
                                  ↓
                           Learned Model
                                  |
                                  ↓
                           Model Evaluation
                                  |
                     +------------+------------+
                     ↓                         ↓
                Training Data             Unseen Data
                     ↓                         ↓
                Performance               Performance
                     |                         |
                     +------------+------------+
                                  ↓
                           Generalization
                                  |
                    +-------------+-------------+
                    ↓                           ↓
               Underfitting                Overfitting
                    ↑                           ↑
                High Bias                  High Variance
```

## Final Takeaway

**Model fitting** is the process of adjusting a model's parameters so that it learns useful patterns from training data.

The central challenge is finding the right level of model complexity:

```text
Underfitting          Good Fit           Overfitting
     |                    |                   |
     ↓                    ↓                   ↓
Too simple          Learns patterns     Memorizes data
     |                    |                   |
     ↓                    ↓                   ↓
High bias          Good generalization  High variance
     |                    |                   |
     +--------------------+-------------------+
                          ↓
                 Goal of Machine Learning
                          ↓
                Perform well on NEW data
```

> **The purpose of model fitting isn't to make a model memorize the training data. It's to learn patterns that generalize to data the model has never seen before.**

```
```

