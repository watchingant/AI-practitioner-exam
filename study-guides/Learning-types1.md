# Training: Understanding Machine Learning Types

## Learning goal

By the end of this short lesson, you should be able to distinguish supervised learning, unsupervised learning, and two related approaches: semi-supervised and reinforcement learning.

## 1. The core idea

Machine learning uses examples or feedback to find useful patterns. The main learning types differ in the kind of information available during learning.

| Learning type | What the model receives | Typical goal |
| --- | --- | --- |
| Supervised learning | Inputs with correct answers (labels) | Predict an answer for a new input |
| Unsupervised learning | Inputs without correct answers | Discover structure or groups in the data |
| Semi-supervised learning | A small labeled set plus a larger unlabeled set | Improve predictions when labels are expensive |
| Reinforcement learning | Actions, rewards, and consequences | Learn choices that maximize long-term reward |

## 2. Supervised learning

In **supervised learning**, every training example has an input and the desired output. The model learns the relationship between them.

### Example: email filtering

| Email text | Label |
| --- | --- |
| “Your receipt is attached.” | Not spam |
| “Claim your prize now!” | Spam |

After training, the model can classify a new email as spam or not spam.

Two common supervised tasks are:

- **Classification:** choose a category, such as cat vs. dog or fraud vs. non-fraud.
- **Regression:** predict a number, such as a house price or delivery time.

**Use supervised learning when:** you have trustworthy examples with known answers and want predictions for future inputs.

## 3. Unsupervised learning

In **unsupervised learning**, the data has no supplied answers. The model looks for meaningful patterns on its own.

### Example: customer groups

Imagine a store has customer purchase histories but no predefined customer categories. A clustering model might discover groups such as:

- frequent high-value shoppers;
- occasional discount-focused shoppers;
- new customers with small first purchases.

The groups are inferred from similarity, rather than taught by labels.

Common unsupervised tasks include:

- **Clustering:** group similar examples.
- **Dimensionality reduction:** represent many features with fewer, more useful ones.
- **Anomaly detection:** identify unusual inputs, such as unexpected transactions.

**Use unsupervised learning when:** labels are unavailable or you want to explore the structure of a dataset.

## 4. Semi-supervised learning

**Semi-supervised learning** combines a smaller set of labeled data with a larger set of unlabeled data.

### Example: photo organization

A team labels 1,000 photos as “beach,” “mountain,” or “city,” while it has 100,000 additional unlabeled photos. The labeled examples guide the model, and the unlabeled examples can help it learn the overall structure of the image collection.

**Use semi-supervised learning when:** labeling is costly or slow, but you can obtain many unlabeled examples.

## 5. Reinforcement learning

In **reinforcement learning**, an agent chooses actions in an environment and receives rewards or penalties. It learns through trial and feedback.

### Example: game-playing agent

An agent decides which move to make in a game. Winning earns a positive reward; losing earns a negative reward. Over many rounds, it learns actions that lead to better long-term outcomes.

Unlike supervised learning, the agent is not usually told the ideal action for every moment. It must explore and learn from the results of its choices.

**Use reinforcement learning when:** decisions happen in sequence and one action changes what happens next—for example, robotics, game play, or resource allocation.

## 6. Quick comparison

| Question | Supervised | Unsupervised | Semi-supervised | Reinforcement |
| --- | --- | --- | --- | --- |
| Are correct answers supplied? | Yes | No | Some | No; rewards are supplied |
| What is learned? | Input-to-answer mapping | Hidden structure | Input-to-answer mapping aided by unlabeled data | Action strategy |
| Example | Detecting spam | Grouping customers | Classifying a large photo library | Learning to play a game |

## 7. Practice

Choose the best learning type for each scenario.

1. Predict whether a medical image contains a condition using images reviewed by specialists.
2. Find natural groups in music listeners based on listening behavior, with no group names provided.
3. Train a delivery robot to choose routes based on travel time and successful deliveries.
4. Classify millions of product photos when only a few thousand have category labels.

### Answers

1. **Supervised learning** — specialist reviews provide labels.
2. **Unsupervised learning** — the goal is to discover groups without labels.
3. **Reinforcement learning** — the robot makes sequential decisions and learns from outcomes.
4. **Semi-supervised learning** — a limited labeled set is combined with a large unlabeled set.

## Key takeaway

Start by asking what feedback your data provides:

- Known answers → **supervised learning**
- No answers, only examples → **unsupervised learning**
- A few answers and many unlabeled examples → **semi-supervised learning**
- Rewards from actions over time → **reinforcement learning**

