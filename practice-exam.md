# AWS AI Practitioner Certification Practice Test

---

---

**Question 1**

A machine learning team is building a model to predict customer churn for a subscription service. They have historical data with labeled outcomes showing which customers canceled. Which type of machine learning approach is most appropriate for this use case?

A) Unsupervised learning with k-means clustering
B) Reinforcement learning with a reward function
C) Supervised learning with a classification algorithm
D) Semi-supervised learning with autoencoders

<details>
<summary>Show Answer</summary>
Correct Answer: C) Supervised learning with a classification algorithm

**Explanation:**
Since the team has labeled historical data (customers who did or did not churn), this is a supervised learning classification problem. Unsupervised learning would be used when labels are not available. Reinforcement learning is for sequential decision-making with rewards, not for predicting outcomes from historical data. Semi-supervised learning is used when only a small portion of data is labeled.
</details>

---

**Question 2**

A data scientist is analyzing customer purchase behavior to identify distinct groups for targeted marketing campaigns. The dataset contains transaction history but no predefined categories. Which machine learning approach should they use?

A) Supervised learning with logistic regression
B) Unsupervised learning with clustering algorithms
C) Supervised learning with random forests
D) Reinforcement learning with Q-learning

<details>
<summary>Show Answer</summary>
Correct Answer: B) Unsupervised learning with clustering algorithms

**Explanation:**
When there are no predefined categories or labels and the goal is to discover natural groupings in data, unsupervised learning with clustering is the appropriate approach. Supervised learning requires labeled data. Reinforcement learning is designed for sequential decision-making problems, not pattern discovery in static datasets.
</details>

---

**Question 3**

A company is training a deep learning model to classify medical images. The model performs well on training data but poorly on unseen test data. Which technique would MOST likely help address this issue?

A) Applying regularization techniques such as dropout
B) Increasing the number of layers in the neural network
C) Removing the validation dataset from the pipeline
D) Increasing the learning rate significantly

<details>
<summary>Show Answer</summary>
Correct Answer: A) Applying regularization techniques such as dropout

**Explanation:**
The described scenario is classic overfitting, where the model memorizes training data but fails to generalize. Regularization techniques like dropout help prevent overfitting by randomly disabling neurons during training. Increasing network depth or learning rate could worsen overfitting. Removing the validation dataset would eliminate the ability to detect overfitting early.
</details>

---

**Question 4**

A team is evaluating a binary classification model for fraud detection where fraudulent transactions are rare (0.1% of total). The model achieves 99.9% accuracy. Which metric would provide the MOST useful evaluation of model performance?

A) Precision and recall (F1 score)
B) Training loss
C) Overall accuracy
D) Mean absolute error

<details>
<summary>Show Answer</summary>
Correct Answer: A) Precision and recall (F1 score)

**Explanation:**
With highly imbalanced datasets, accuracy is misleading because a model that predicts all transactions as non-fraudulent would still achieve 99.9% accuracy. Precision and recall (combined in the F1 score) measure how well the model identifies actual fraud cases. Training loss measures optimization progress, not real-world performance. Mean absolute error is used for regression problems.
</details>

---

**Question 5**

A data scientist wants to reduce the dimensionality of a dataset with 500 features before training a model. They need to retain as much variance in the data as possible. Which technique is MOST appropriate?

A) L1 regularization (Lasso)
B) K-nearest neighbors
C) Gradient boosting
D) Principal Component Analysis (PCA)

<details>
<summary>Show Answer</summary>
Correct Answer: D) Principal Component Analysis (PCA)

**Explanation:**
PCA is a dimensionality reduction technique that transforms features into principal components while retaining maximum variance. L1 regularization performs feature selection but doesn't transform features. Gradient boosting is an ensemble learning method, not a dimensionality reduction technique. K-nearest neighbors is a classification/regression algorithm.
</details>

---

**Question 6**

A company is using Amazon SageMaker to train a model. They need to automatically find the best combination of hyperparameters to optimize model performance. Which SageMaker feature should they use?

A) SageMaker Data Wrangler
B) SageMaker Feature Store
C) SageMaker Automatic Model Tuning (Hyperparameter Optimization)
D) SageMaker Model Monitor

<details>
<summary>Show Answer</summary>
Correct Answer: C) SageMaker Automatic Model Tuning (Hyperparameter Optimization)

**Explanation:**
SageMaker Automatic Model Tuning (also called Hyperparameter Optimization) automatically searches for the best hyperparameter combinations using Bayesian optimization or other strategies. Data Wrangler is for data preparation and transformation. Feature Store manages ML features. Model Monitor detects data drift in deployed models.
</details>

---

**Question 7**

A team is building a convolutional neural network (CNN) for image classification. Which layer type is primarily responsible for detecting spatial features like edges and textures in input images?

A) Convolutional layers with filters/kernels
B) Recurrent layers
C) Fully connected (dense) layers
D) Embedding layers

<details>
<summary>Show Answer</summary>
Correct Answer: A) Convolutional layers with filters/kernels

**Explanation:**
Convolutional layers apply learnable filters/kernels across the input image to detect spatial features such as edges, textures, and patterns. Fully connected layers combine features for final classification but don't detect spatial patterns. Recurrent layers process sequential data. Embedding layers convert categorical data into dense vectors.
</details>

---

**Question 8**

A company is developing a time-series forecasting model to predict stock prices based on historical sequential data. Which neural network architecture is BEST suited for capturing temporal dependencies in this data?

A) Convolutional Neural Network (CNN)
B) Generative Adversarial Network (GAN)
C) Recurrent Neural Network (RNN) or LSTM
D) Feedforward Neural Network

<details>
<summary>Show Answer</summary>
Correct Answer: C) Recurrent Neural Network (RNN) or LSTM

**Explanation:**
RNNs and LSTMs are specifically designed to process sequential data and capture temporal dependencies through their recurrent connections and memory mechanisms. CNNs are optimized for spatial data like images. GANs are used for data generation. Feedforward networks don't have memory of previous inputs needed for sequence modeling.
</details>

---

**Question 9**

A machine learning engineer is splitting their dataset for model development. They want to ensure proper evaluation while maximizing training data usage for a small dataset of 2,000 samples. Which approach is MOST appropriate?

A) Using 100% of the data for training and evaluating on the same data
B) Using a 95/5 train/test split with no validation set
C) K-fold cross-validation
D) Training only on the most recent 50% of data

<details>
<summary>Show Answer</summary>
Correct Answer: C) K-fold cross-validation

**Explanation:**
K-fold cross-validation maximizes both training data usage and evaluation reliability by rotating which portion serves as the test set across multiple folds. Training and evaluating on the same data leads to overfitting without detection. A 95/5 split provides too few test samples for reliable evaluation. Using only recent data wastes valuable training samples.
</details>

---

**Question 10**

A data scientist notices that their gradient boosting model has high variance and is overfitting the training data. Which combination of techniques would MOST effectively address this? (Select TWO)

A) Increasing the maximum tree depth
B) Reducing the learning rate and increasing the number of estimators
C) Removing all regularization parameters
D) Adding L2 regularization and limiting tree depth
E) Converting the problem to unsupervised learning

<details>
<summary>Show Answer</summary>
Correct Answers: B) Reducing the learning rate and increasing the number of estimators and D) Adding L2 regularization and limiting tree depth

**Explanation:**
Reducing the learning rate with more estimators creates a more gradual learning process that generalizes better. L2 regularization penalizes complex models and limiting tree depth prevents individual trees from memorizing training data. Increasing tree depth or removing regularization would worsen overfitting. Converting to unsupervised learning changes the problem entirely.
</details>

---

**Question 11**

A company wants to deploy a machine learning model that predicts whether loan applications should be approved or denied. The model needs to minimize the number of approved loans that actually default. Which metric should they prioritize?

A) Recall (sensitivity)
B) Area Under the ROC Curve (AUC-ROC)
C) Overall accuracy
D) Precision for the "approve" class

<details>
<summary>Show Answer</summary>
Correct Answer: D) Precision for the "approve" class

**Explanation:**
Precision for the approve class measures what proportion of approved loans are actually good loans (true positives among predicted positives). This directly minimizes defaults among approved loans. Recall focuses on finding all good loans, which could approve risky ones. Overall accuracy doesn't distinguish between error types. AUC-ROC measures general discriminative ability but doesn't specifically optimize for minimizing defaults.
</details>

---

**Question 12**

A machine learning team is building a recommendation system for an e-commerce platform. They have user interaction data including clicks, purchases, and ratings. Which approach would MOST effectively leverage all these signal types?

A) Content-based filtering using only product descriptions
B) A simple popularity-based ranking system
C) Rule-based recommendations using only purchase history
D) Collaborative filtering combined with implicit and explicit feedback signals

<details>
<summary>Show Answer</summary>
Correct Answer: D) Collaborative filtering combined with implicit and explicit feedback signals

**Explanation:**
Collaborative filtering with both implicit signals (clicks) and explicit signals (ratings, purchases) leverages all available user interaction data for comprehensive recommendations. Content-based filtering ignores user behavior patterns. Popularity-based ranking doesn't personalize. Rule-based approaches using only purchases miss valuable click and rating signals.
</details>

---

**Question 13**

A data engineer is preparing features for a machine learning model. The dataset contains a categorical variable "country" with 195 unique values. Which feature engineering technique is MOST appropriate to encode this variable without creating excessive dimensionality?

A) One-hot encoding all 195 categories
B) Converting country names to their ASCII character sum
C) Dropping the country feature entirely
D) Target encoding (mean encoding) with proper cross-validation

<details>
<summary>Show Answer</summary>
Correct Answer: D) Target encoding (mean encoding) with proper cross-validation

**Explanation:**
Target encoding replaces each category with the mean of the target variable for that category, creating a single numeric feature regardless of cardinality. One-hot encoding 195 categories creates excessive dimensionality and sparse features. Dropping the feature loses potentially valuable information. ASCII character sums have no meaningful relationship to the target variable.
</details>

---

**Question 14**

A team is training a neural network and observes that the loss function oscillates wildly and fails to converge during training. Which adjustment is MOST likely to resolve this issue?

A) Reducing the learning rate
B) Increasing the batch size to the full dataset
C) Adding more hidden layers
D) Removing all activation functions

<details>
<summary>Show Answer</summary>
Correct Answer: A) Reducing the learning rate

**Explanation:**
Oscillating loss that fails to converge is a classic sign of a learning rate that is too high, causing gradient descent to overshoot the minimum. Reducing the learning rate allows smaller, more stable steps toward convergence. Using the full dataset as batch size would slow training significantly. Adding layers increases complexity. Removing activation functions eliminates the network's ability to learn non-linear patterns.
</details>

---

**Question 15**

A company wants to build a complete ML pipeline on AWS that includes data preparation, model training, and deployment. They need an integrated development environment with built-in algorithms and notebook support. Which AWS service provides this end-to-end capability?

A) AWS Lambda
B) Amazon SageMaker
C) Amazon Comprehend
D) AWS Glue

<details>
<summary>Show Answer</summary>
Correct Answer: B) Amazon SageMaker

**Explanation:**
Amazon SageMaker provides a complete ML platform with Jupyter notebooks, built-in algorithms, training infrastructure, and deployment capabilities for end-to-end ML workflows. AWS Lambda is for serverless computing, not ML development. Amazon Comprehend is a pre-built NLP service, not a development platform. AWS Glue is for ETL data processing, not model development.
</details>

---

**Question 16**

A data scientist is evaluating a regression model that predicts house prices. Which metric is MOST appropriate for measuring how far predictions deviate from actual values in the same unit as the target variable?

A) AUC-ROC
B) F1 Score
C) Root Mean Squared Error (RMSE)
D) Log loss

<details>
<summary>Show Answer</summary>
Correct Answer: C) Root Mean Squared Error (RMSE)

**Explanation:**
RMSE measures prediction error in the same units as the target variable (dollars for house prices), making it directly interpretable. AUC-ROC and F1 Score are classification metrics, not applicable to regression. Log loss measures probability calibration for classification tasks, not regression prediction accuracy.
</details>

---

**Question 17**

A machine learning engineer is implementing an ensemble method that trains multiple decision trees on random subsets of features and data, then aggregates their predictions by majority vote. Which algorithm does this describe?

A) Gradient Boosting
B) AdaBoost
C) Random Forest
D) Support Vector Machine

<details>
<summary>Show Answer</summary>
Correct Answer: C) Random Forest

**Explanation:**
Random Forest trains multiple decision trees on random subsets of both data (bagging) and features, then aggregates predictions through majority voting (classification) or averaging (regression). Gradient Boosting trains trees sequentially to correct previous errors. AdaBoost adjusts sample weights based on misclassifications. SVMs find optimal hyperplanes for classification.
</details>

---

**Question 18**

A team is working with a dataset where 5% of samples belong to the positive class and 95% to the negative class. They need to train a classifier that performs well on the minority class. Which strategies would help address this class imbalance? (Select TWO)

A) Using SMOTE (Synthetic Minority Over-sampling Technique) to generate synthetic samples
B) Removing all minority class samples to simplify the problem
C) Adjusting class weights in the loss function to penalize minority class errors more heavily
D) Increasing the decision threshold to 0.99
E) Using only accuracy as the evaluation metric

<details>
<summary>Show Answer</summary>
Correct Answers: A) Using SMOTE (Synthetic Minority Over-sampling Technique) to generate synthetic samples and C) Adjusting class weights in the loss function to penalize minority class errors more heavily

**Explanation:**
SMOTE creates synthetic examples of the minority class to balance the dataset distribution. Adjusting class weights makes the model pay more attention to minority class errors during training. Removing minority samples eliminates the signal entirely. A very high threshold would classify almost nothing as positive. Accuracy is misleading with imbalanced data.
</details>

---

**Question 19**

A company uses Amazon SageMaker to manage their ML workflow. They need to store, discover, and share curated features across multiple ML projects and teams. Which SageMaker component serves this purpose?

A) SageMaker Model Registry
B) SageMaker Feature Store
C) SageMaker Experiments
D) SageMaker Pipelines

<details>
<summary>Show Answer</summary>
Correct Answer: B) SageMaker Feature Store

**Explanation:**
SageMaker Feature Store is a centralized repository for storing, sharing, and managing ML features across teams and projects, supporting both online (low-latency) and offline (batch) access patterns. Model Registry manages model versions. Experiments tracks training runs. Pipelines orchestrates ML workflows.
</details>

---

**Question 20**

A data scientist is training a logistic regression model and wants to prevent overfitting while also performing automatic feature selection by driving some feature coefficients to exactly zero. Which regularization technique should they apply?

A) Elastic Net with alpha = 0
B) L2 regularization (Ridge)
C) L1 regularization (Lasso)
D) No regularization with early stopping

<details>
<summary>Show Answer</summary>
Correct Answer: C) L1 regularization (Lasso)

**Explanation:**
L1 regularization (Lasso) adds the absolute value of coefficients as a penalty, which can drive coefficients to exactly zero, effectively performing feature selection. L2 regularization (Ridge) shrinks coefficients toward zero but rarely makes them exactly zero. Elastic Net with alpha=0 is equivalent to pure L2. Early stopping without regularization doesn't provide feature selection.
</details>

---

**Question 21**

A machine learning team wants to track and compare multiple training experiments, including hyperparameters, metrics, and artifacts. Which Amazon SageMaker capability enables this systematic experiment tracking?

A) SageMaker Ground Truth
B) SageMaker Experiments
C) SageMaker Debugger
D) SageMaker Neo

<details>
<summary>Show Answer</summary>
Correct Answer: B) SageMaker Experiments

**Explanation:**
SageMaker Experiments enables tracking, organizing, and comparing ML experiments including hyperparameters, metrics, and model artifacts across multiple training runs. Ground Truth is for data labeling. Debugger monitors training issues in real-time. Neo optimizes models for deployment on edge devices.
</details>

---

**Question 22**

A company is building a fraud detection model and needs to understand which features contribute most to individual predictions for regulatory compliance. Which technique provides instance-level feature importance explanations?

A) Global feature importance from random forests
B) SHAP (SHapley Additive exPlanations) values
C) Confusion matrix analysis
D) Learning curve plots

<details>
<summary>Show Answer</summary>
Correct Answer: B) SHAP (SHapley Additive exPlanations) values

**Explanation:**
SHAP values provide instance-level (local) explanations showing how each feature contributes to a specific prediction, which is essential for regulatory compliance. Global feature importance shows overall importance but not per-prediction reasoning. Confusion matrices show aggregate performance. Learning curves show training progress, not feature contributions.
</details>

---

**Question 23**

A machine learning engineer observes that their model's training loss continues decreasing while validation loss starts increasing after epoch 50. Which strategy directly addresses this behavior?

A) Training for more epochs to allow further optimization
B) Increasing model complexity with additional layers
C) Implementing early stopping based on validation loss
D) Using a larger learning rate for faster convergence

<details>
<summary>Show Answer</summary>
Correct Answer: C) Implementing early stopping based on validation loss

**Explanation:**
When training loss decreases but validation loss increases, the model is overfitting. Early stopping halts training when validation loss stops improving, preventing further overfitting. Training for more epochs or increasing complexity would worsen overfitting. A larger learning rate might cause instability but doesn't address the fundamental overfitting issue.
</details>

---

**Question 24**

A team is using gradient descent to optimize a neural network. They notice training is very slow with their dataset of 10 million samples. Which variant of gradient descent balances computational efficiency with stable convergence?

A) Batch gradient descent using all samples per update
B) Stochastic gradient descent using one sample per update
C) Mini-batch gradient descent using subsets of 32-256 samples
D) Second-order optimization using the full Hessian matrix

<details>
<summary>Show Answer</summary>
Correct Answer: C) Mini-batch gradient descent using subsets of 32-256 samples

**Explanation:**
Mini-batch gradient descent strikes a balance between the stability of batch gradient descent and the speed of stochastic gradient descent by computing gradients on small subsets. Full batch gradient descent is computationally expensive with 10 million samples. Pure stochastic (one sample) updates are noisy and unstable. Second-order methods with full Hessian are computationally prohibitive at this scale.
</details>

---

**Question 25**

A company wants to understand how large language models process input text. In the transformer architecture, which mechanism allows the model to weigh the relevance of different parts of the input when generating each output token?

A) Batch normalization
B) Dropout regularization
C) Self-attention mechanism
D) Pooling layers

<details>
<summary>Show Answer</summary>
Correct Answer: C) Self-attention mechanism

**Explanation:**
The self-attention mechanism in transformers computes relevance scores between all positions in the input sequence, allowing the model to focus on the most relevant parts when processing each token. Batch normalization normalizes activations for training stability. Dropout is a regularization technique. Pooling layers reduce spatial dimensions in CNNs.
</details>

---

**Question 26**

A team is evaluating different foundation models for their text generation application. They need a model that can handle multiple languages and produce high-quality creative content. Which characteristic of foundation models makes this possible without training from scratch?

A) Foundation models are pre-trained on massive diverse datasets and can be adapted to many tasks
B) Foundation models are small models designed for single tasks
C) Foundation models only work with English language data
D) Foundation models require task-specific architectures for each use case

<details>
<summary>Show Answer</summary>
Correct Answer: A) Foundation models are pre-trained on massive diverse datasets and can be adapted to many tasks

**Explanation:**
Foundation models are trained on massive, diverse datasets spanning multiple languages and domains, giving them broad capabilities that can be adapted to specific tasks without training from scratch. They are typically very large (not small), multilingual (not English-only), and use general architectures like transformers that handle multiple tasks.
</details>

---

**Question 27**

A developer is using a large language model and wants to get accurate answers about recent company policies without any examples in the prompt. They simply ask the question directly. Which prompting technique does this describe?

A) Few-shot prompting
B) Chain-of-thought prompting
C) Zero-shot prompting
D) Retrieval-augmented generation

<details>
<summary>Show Answer</summary>
Correct Answer: C) Zero-shot prompting

**Explanation:**
Zero-shot prompting involves giving the model a task or question without providing any examples, relying on the model's pre-trained knowledge to generate a response. Few-shot provides examples in the prompt. Chain-of-thought asks the model to reason step by step. RAG retrieves external documents to augment the prompt.
</details>

---

**Question 28**

A data scientist is configuring an LLM for a creative writing application. They want the model to generate diverse and unexpected text rather than always choosing the most probable next token. Which parameter should they increase?

A) Temperature
B) Stop sequences
C) Maximum token limit
D) Top-k with k=1

<details>
<summary>Show Answer</summary>
Correct Answer: A) Temperature

**Explanation:**
Increasing temperature makes the probability distribution over tokens more uniform, allowing the model to select less probable tokens more frequently, resulting in more diverse and creative output. Maximum token limit only controls output length. Stop sequences define where to end generation. Top-k=1 (greedy decoding) always selects the most probable token, reducing diversity.
</details>

---

**Question 29**

A company is experiencing issues with their LLM-powered chatbot generating factually incorrect but confident-sounding responses about their product specifications. What is this phenomenon called?

A) Hallucination
B) Catastrophic forgetting
C) Model drift
D) Mode collapse

<details>
<summary>Show Answer</summary>
Correct Answer: A) Hallucination

**Explanation:**
Hallucination refers to LLMs generating plausible-sounding but factually incorrect information with high confidence. Model drift occurs when real-world data distributions change over time. Catastrophic forgetting happens when fine-tuning causes a model to lose previously learned knowledge. Mode collapse is a GAN training issue where the generator produces limited output variety.
</details>

---

**Question 30**

A team wants to use Amazon Bedrock to access foundation models. Which statements accurately describe Amazon Bedrock's capabilities? (Select TWO)

A) It requires customers to manage the underlying infrastructure and GPU instances
B) It provides serverless access to foundation models from multiple providers through a unified API
C) It only supports models built by Amazon
D) It allows customization of foundation models with proprietary data without managing infrastructure
E) It requires deploying models to customer-owned EC2 instances

<details>
<summary>Show Answer</summary>
Correct Answers: B) It provides serverless access to foundation models from multiple providers through a unified API and D) It allows customization of foundation models with proprietary data without managing infrastructure

**Explanation:**
Amazon Bedrock is a fully managed, serverless service providing access to foundation models from Amazon (Titan), Anthropic (Claude), Meta (Llama), and others through a single API. It also supports model customization with proprietary data without infrastructure management. Customers don't manage GPU instances or deploy to EC2.
</details>

---

**Question 31**

A developer wants to improve their LLM's performance on complex reasoning tasks. They modify their prompt to include the instruction "Let's think through this step by step" before the question. Which prompting technique is this?

A) Few-shot prompting
B) Zero-shot prompting
C) Chain-of-thought prompting
D) Instruction tuning

<details>
<summary>Show Answer</summary>
Correct Answer: C) Chain-of-thought prompting

**Explanation:**
Chain-of-thought prompting encourages the model to break down complex problems into intermediate reasoning steps, often triggered by phrases like "let's think step by step." This improves performance on math, logic, and multi-step reasoning tasks. Few-shot provides examples. Zero-shot gives no examples or reasoning guidance. Instruction tuning is a training technique, not a prompting method.
</details>

---

**Question 32**

A machine learning engineer needs to convert raw text into numerical representations that capture semantic meaning for use in a natural language processing model. Which technique transforms words into dense vector representations where similar words have similar vectors?

A) One-hot encoding
B) Word embeddings (Word2Vec/GloVe)
C) Bag of words with TF-IDF
D) ASCII character encoding

<details>
<summary>Show Answer</summary>
Correct Answer: B) Word embeddings (Word2Vec/GloVe)

**Explanation:**
Word embeddings like Word2Vec and GloVe create dense vector representations where semantically similar words are mapped to nearby points in the vector space. One-hot encoding creates sparse, high-dimensional vectors without semantic relationships. TF-IDF captures term frequency but not semantic similarity. ASCII encoding has no linguistic meaning.
</details>

---

**Question 33**

A company has a pre-trained foundation model and wants to adapt it to their specific domain (medical literature) while keeping computational costs low. They have a small labeled dataset of 5,000 medical documents. Which approach is MOST cost-effective?

A) Pre-training a new model from scratch on medical data
B) Training a traditional rule-based system instead
C) Using only zero-shot prompting without any adaptation
D) Fine-tuning the foundation model on the medical dataset

<details>
<summary>Show Answer</summary>
Correct Answer: D) Fine-tuning the foundation model on the medical dataset

**Explanation:**
Fine-tuning adapts a pre-trained model to a specific domain using a relatively small labeled dataset, leveraging the model's existing knowledge while learning domain-specific patterns cost-effectively. Pre-training from scratch requires massive data and compute. Zero-shot prompting alone may not capture domain-specific nuances. Rule-based systems cannot handle the complexity of medical language.
</details>

---

**Question 34**

A team is building an LLM application and needs to control the randomness of text generation. They want the model to consider only the top 90% cumulative probability of tokens at each step. Which parameter controls this behavior?

A) Temperature
B) Top-p (nucleus sampling)
C) Maximum sequence length
D) Frequency penalty

<details>
<summary>Show Answer</summary>
Correct Answer: B) Top-p (nucleus sampling)

**Explanation:**
Top-p (nucleus sampling) filters the token vocabulary to the smallest set whose cumulative probability exceeds the threshold p (0.9 in this case), then samples from this reduced set. Temperature scales the entire probability distribution but doesn't set a cumulative threshold. Maximum sequence length controls output length. Frequency penalty reduces repetition.
</details>

---

**Question 35**

A company wants to improve an existing LLM's ability to follow specific instructions and align with human preferences. Which training technique uses human feedback to optimize the model's responses after initial pre-training?

A) Transfer learning from a computer vision model
B) Reinforcement Learning from Human Feedback (RLHF)
C) Unsupervised pre-training with next-token prediction
D) Data augmentation with synthetic examples

<details>
<summary>Show Answer</summary>
Correct Answer: B) Reinforcement Learning from Human Feedback (RLHF)

**Explanation:**
RLHF is a post-training technique that uses human preference data to train a reward model, which then guides the LLM to generate responses that align with human expectations. Transfer learning from vision models isn't relevant to instruction following. Pre-training with next-token prediction is the initial training phase. Data augmentation doesn't incorporate human preferences.
</details>

---

**Question 36**

A developer is working with a tokenizer for a large language model. They notice that the word "unhappiness" is split into ["un", "happi", "ness"]. What is the purpose of this subword tokenization approach?

A) To increase the vocabulary size to include every possible word
B) To make the text longer for more training data
C) To handle out-of-vocabulary words by breaking them into known subword units
D) To remove stop words from the input

<details>
<summary>Show Answer</summary>
Correct Answer: C) To handle out-of-vocabulary words by breaking them into known subword units

**Explanation:**
Subword tokenization (like BPE or WordPiece) breaks unknown or rare words into smaller known units, allowing the model to handle any word including novel compounds and morphological variants. It actually reduces vocabulary size compared to word-level tokenization. It doesn't aim to increase text length or remove stop words.
</details>

---

**Question 37**

A team is selecting a foundation model on Amazon Bedrock for their customer service chatbot. The chatbot needs to provide accurate, factual responses and minimize creative embellishment. Which configuration approach is MOST appropriate?

A) Set temperature to maximum (1.0) for diverse responses
B) Use a large top-p value (0.99) to maximize vocabulary usage
C) Disable all safety guardrails for unrestricted output
D) Set a low temperature (close to 0) for deterministic, focused responses

<details>
<summary>Show Answer</summary>
Correct Answer: D) Set a low temperature (close to 0) for deterministic, focused responses

**Explanation:**
A low temperature makes the model more deterministic by sharpening the probability distribution, causing it to select the most likely (and typically most factual) tokens. High temperature increases randomness and creativity. A high top-p allows too many unlikely tokens. Disabling guardrails is a safety concern unrelated to factual accuracy.
</details>

---

**Question 38**

A company is deciding between using a pre-trained foundation model directly versus fine-tuning it for their specific task. Which factors should they consider when deciding to fine-tune? (Select TWO)

A) They have a large domain-specific labeled dataset that differs significantly from the model's pre-training data
B) They need the model to work immediately without any additional training time or cost
C) The pre-trained model's zero-shot performance already meets their accuracy requirements
D) They need the model to learn specialized terminology and response patterns for their industry
E) They want to minimize all computational costs and deployment time

<details>
<summary>Show Answer</summary>
Correct Answers: A) They have a large domain-specific labeled dataset that differs significantly from the model's pre-training data and D) They need the model to learn specialized terminology and response patterns for their industry

**Explanation:**
Fine-tuning is most beneficial when domain-specific data differs from pre-training data and when specialized terminology or response patterns are needed. If the model already meets requirements with zero-shot performance, fine-tuning is unnecessary. Fine-tuning requires additional time and cost, so it's not chosen when immediate deployment or cost minimization is the priority.
</details>

---

**Question 39**

A machine learning engineer is comparing different LLM architectures. Which statement BEST describes the difference between encoder-only, decoder-only, and encoder-decoder transformer models?

A) Encoder-only models generate text, decoder-only models classify text, encoder-decoder models do both
B) Encoder-only models are best for understanding tasks (classification), decoder-only for generation, and encoder-decoder for sequence-to-sequence tasks like translation
C) All three architectures perform identically on all tasks
D) Encoder-only models use attention while decoder-only models use recurrence

<details>
<summary>Show Answer</summary>
Correct Answer: B) Encoder-only models are best for understanding tasks (classification), decoder-only for generation, and encoder-decoder for sequence-to-sequence tasks like translation

**Explanation:**
Encoder-only models (like BERT) excel at understanding and classification by processing bidirectional context. Decoder-only models (like GPT) are optimized for text generation with autoregressive (left-to-right) processing. Encoder-decoder models (like T5) handle tasks requiring both input understanding and output generation, like translation or summarization. All three use attention mechanisms.
</details>

---

**Question 40**

A developer notices that their LLM application sometimes generates text that contradicts information provided earlier in the same conversation. Which limitation of transformer-based models contributes to this issue?

A) Transformers cannot handle natural language at all
B) The model's inability to process any text input
C) Finite context window limiting how much prior conversation the model can reference
D) The model requires images as input to function

<details>
<summary>Show Answer</summary>
Correct Answer: C) Finite context window limiting how much prior conversation the model can reference

**Explanation:**
Transformers have a fixed context window (e.g., 4K, 8K, or 128K tokens), and information beyond this window is lost. In long conversations, earlier context may fall outside the window, causing inconsistencies. The other options are incorrect as transformers are specifically designed to process natural language text effectively.
</details>

---

**Question 41**

A startup is building a generative AI application and wants to use Amazon Bedrock. They are evaluating foundation models from different providers. Which model families are available through Amazon Bedrock? (Select TWO)

A) OpenAI GPT-4 and GPT-3.5
B) Anthropic Claude models
C) Google PaLM exclusively
D) Amazon Titan models
E) Apple Foundation models

<details>
<summary>Show Answer</summary>
Correct Answers: B) Anthropic Claude models and D) Amazon Titan models

**Explanation:**
Amazon Bedrock provides access to multiple foundation model families including Anthropic Claude, Amazon Titan, Meta Llama, Mistral, Cohere, and Stability AI. OpenAI models are not available through Bedrock (they use their own API). Google PaLM and Apple models are not offered through Bedrock.
</details>

---

**Question 42**

A data scientist is preparing a prompt that includes three examples of the desired input-output format before asking the model to complete a new task. Which prompting technique is being used?

A) Zero-shot prompting
B) Few-shot prompting
C) Chain-of-thought prompting
D) Instruction tuning

<details>
<summary>Show Answer</summary>
Correct Answer: B) Few-shot prompting

**Explanation:**
Few-shot prompting provides a small number of input-output examples within the prompt to demonstrate the desired behavior or format before presenting the actual task. Zero-shot provides no examples. Chain-of-thought focuses on reasoning steps rather than input-output examples. Instruction tuning is a model training technique, not a prompting strategy.
</details>

---

**Question 43**

A company wants to make their pre-trained LLM better at following specific formatting instructions and refusing harmful requests. Which post-training technique specifically addresses instruction following and alignment?

A) Continued pre-training with more web data
B) Instruction tuning with curated prompt-response pairs
C) Reducing the model's parameter count
D) Increasing the tokenizer's vocabulary size

<details>
<summary>Show Answer</summary>
Correct Answer: B) Instruction tuning with curated prompt-response pairs

**Explanation:**
Instruction tuning fine-tunes a model on carefully curated datasets of instructions paired with desired responses, teaching the model to follow formatting requirements, answer questions helpfully, and refuse harmful requests. Continued pre-training adds general knowledge but not instruction-following ability. Reducing parameters or changing tokenizer vocabulary don't improve alignment.
</details>

---

**Question 44**

A team is working with a generative AI model and wants to understand how the model processes input text internally. In the transformer architecture, what role do positional encodings serve?

A) They determine the model's output language
B) They provide information about the order/position of tokens in the sequence since attention is position-agnostic
C) They encrypt the input for security purposes
D) They compress the input to reduce memory usage

<details>
<summary>Show Answer</summary>
Correct Answer: B) They provide information about the order/position of tokens in the sequence since attention is position-agnostic

**Explanation:**
Self-attention mechanisms are inherently permutation-invariant (they don't inherently know token order), so positional encodings are added to provide sequence position information. Without them, the model would treat "the cat sat on the mat" and "mat the on sat cat the" identically. They don't determine output language, provide encryption, or compress input.
</details>

---

**Question 45**

A company is building a customer support system using generative AI. They want to prevent the model from generating responses about competitor products or making financial promises. Which Amazon Bedrock feature is MOST appropriate for implementing these content restrictions?

A) Amazon Bedrock Knowledge Bases
B) Amazon Bedrock Agents
C) Amazon Bedrock Model Evaluation
D) Amazon Bedrock Guardrails

<details>
<summary>Show Answer</summary>
Correct Answer: D) Amazon Bedrock Guardrails

**Explanation:**
Bedrock Guardrails allows configuration of content filters, denied topics, and word filters to prevent models from generating specific types of content or discussing restricted topics. Knowledge Bases connect models to external data sources. Agents enable multi-step task execution. Model Evaluation assesses model performance on benchmarks.
</details>

---

**Question 46**

A developer is designing a prompt for an LLM to extract structured data from unstructured text. Which prompt engineering best practice would MOST improve extraction accuracy?

A) Making the prompt as short as possible with no context
B) Asking the model to be creative in its response format
C) Providing a clear output schema/format specification with examples of the expected JSON structure
D) Using maximum temperature for diverse interpretations

<details>
<summary>Show Answer</summary>
Correct Answer: C) Providing a clear output schema/format specification with examples of the expected JSON structure

**Explanation:**
For structured data extraction, providing explicit output format specifications with examples ensures the model understands exactly what structure to produce. Short prompts without context lead to ambiguous outputs. Encouraging creativity produces inconsistent formats. High temperature introduces randomness that harms extraction precision.
</details>

---

**Question 47**

A machine learning team is training a large language model from scratch. During the pre-training phase, which objective is MOST commonly used for decoder-only models like GPT?

A) Masked language modeling (predicting randomly masked tokens)
B) Named entity recognition
C) Image classification
D) Next-token prediction (causal language modeling)

<details>
<summary>Show Answer</summary>
Correct Answer: D) Next-token prediction (causal language modeling)

**Explanation:**
Decoder-only models like GPT are pre-trained with causal language modeling, where the model predicts the next token given all previous tokens in a left-to-right fashion. Masked language modeling (predicting masked tokens using bidirectional context) is used for encoder-only models like BERT. Image classification and NER are downstream tasks, not pre-training objectives.
</details>

---

**Question 48**

A company wants to reduce hallucinations in their generative AI application that answers questions about their internal documentation. Which approach would MOST effectively reduce hallucinations while maintaining response quality?

A) Retrieval-Augmented Generation (RAG) that grounds responses in retrieved documents
B) Increasing the temperature parameter to explore more diverse responses
C) Removing all system prompts to give the model more freedom
D) Using a smaller model with fewer parameters

<details>
<summary>Show Answer</summary>
Correct Answer: A) Retrieval-Augmented Generation (RAG) that grounds responses in retrieved documents

**Explanation:**
RAG reduces hallucinations by retrieving relevant documents and including them in the context, allowing the model to generate responses grounded in factual source material. Increasing temperature would increase randomness and potentially more hallucinations. Removing system prompts reduces control. Smaller models may hallucinate more due to less learned knowledge.
</details>

---

**Question 49**

A developer is working with Amazon Bedrock and wants to understand model pricing. How does Amazon Bedrock typically charge for foundation model usage?

A) A fixed monthly subscription regardless of usage
B) Per input/output token processed, with on-demand and provisioned throughput options
C) Only based on the number of API calls made, regardless of prompt length
D) Free tier only with no paid option

<details>
<summary>Show Answer</summary>
Correct Answer: B) Per input/output token processed, with on-demand and provisioned throughput options

**Explanation:**
Amazon Bedrock charges based on tokens processed (input and output tokens), with on-demand pricing for variable workloads and provisioned throughput for predictable, high-volume usage at committed rates. It's not a flat subscription, not purely per-call regardless of size, and while there may be free tier for experimentation, paid usage is token-based.
</details>

---

**Question 50**

A team is evaluating whether to use a generative AI model or a traditional ML model for their task. Which use case is BEST suited for a generative AI foundation model rather than a traditional supervised learning approach?

A) Generating natural language summaries of long documents with varied topics
B) Predicting a single numeric value from tabular data with clear features
C) Binary classification on structured data with millions of labeled examples
D) Time-series forecasting with well-defined numerical inputs

<details>
<summary>Show Answer</summary>
Correct Answer: A) Generating natural language summaries of long documents with varied topics

**Explanation:**
Generative AI models excel at open-ended natural language tasks like summarization across varied topics where the output is creative text. Traditional ML models are often more efficient and appropriate for structured prediction tasks (numeric regression, binary classification on tabular data, time-series forecasting) where inputs and outputs are well-defined.
</details>

---

**Question 51**

A company has fine-tuned a foundation model and wants to prevent it from losing the general capabilities it learned during pre-training while adapting to their specific domain. What is this phenomenon of losing previously learned knowledge called?

A) Overfitting
B) Catastrophic forgetting
C) Underfitting
D) Gradient vanishing

<details>
<summary>Show Answer</summary>
Correct Answer: B) Catastrophic forgetting

**Explanation:**
Catastrophic forgetting occurs when fine-tuning on new data causes the model to lose knowledge acquired during pre-training or earlier training stages. Overfitting is memorizing training data rather than generalizing. Underfitting is failing to capture patterns. Gradient vanishing is a training difficulty in deep networks where gradients become too small.
</details>

---

**Question 52**

A developer is building a multi-turn conversational AI system. They need the model to maintain context from previous messages in the conversation. Which approach enables the model to reference earlier parts of the dialogue?

A) Training a new model for each conversation turn
B) Including the conversation history in the prompt context window
C) Using a separate model for each message
D) Resetting the model's weights after each response

<details>
<summary>Show Answer</summary>
Correct Answer: B) Including the conversation history in the prompt context window

**Explanation:**
Since LLMs are stateless (they don't retain information between API calls), conversation history must be passed in the prompt context window for each turn to maintain coherence. Training a new model per turn is impractical. Using separate models fragments context. Resetting weights would destroy all learned knowledge.
</details>

---

**Question 53**

A team is using prompt engineering to improve their LLM application. They want to assign the model a specific persona and set of behavioral guidelines that persist across all user interactions. Where should they place these instructions?

A) In the system prompt/message
B) In the user message of each turn
C) In the model's tokenizer configuration
D) In the API authentication headers

<details>
<summary>Show Answer</summary>
Correct Answer: A) In the system prompt/message

**Explanation:**
The system prompt/message is designed for persistent instructions, persona definitions, and behavioral guidelines that apply across all interactions. User messages contain the actual queries. The tokenizer configuration handles text-to-token conversion, not behavioral instructions. Authentication headers handle security, not model behavior.
</details>

---

**Question 54**

A company wants to build a question-answering system that can respond accurately about their internal knowledge base of 50,000 documents. They want to minimize hallucinations and keep information current without retraining the model. Which Amazon Bedrock feature should they use?

A) Amazon Bedrock Model Evaluation
B) Amazon Bedrock Guardrails
C) Amazon Bedrock Knowledge Bases with RAG
D) Amazon Bedrock Custom Model Import

<details>
<summary>Show Answer</summary>
Correct Answer: C) Amazon Bedrock Knowledge Bases with RAG

**Explanation:**
Bedrock Knowledge Bases implements RAG by automatically chunking, embedding, and indexing documents into a vector store, then retrieving relevant context for each query. This grounds responses in actual documents, reducing hallucinations and keeping information current without retraining. Model Evaluation benchmarks models. Guardrails filter content. Custom Model Import brings external models to Bedrock.
</details>

---

**Question 55**

A development team is building an AI assistant that needs to autonomously perform multi-step tasks like booking travel, including searching for flights, comparing prices, and making reservations through external APIs. Which Amazon Bedrock capability enables this?

A) Amazon Bedrock Agents
B) Amazon Bedrock Knowledge Bases
C) Amazon Bedrock Guardrails
D) Amazon Bedrock Model Evaluation

<details>
<summary>Show Answer</summary>
Correct Answer: A) Amazon Bedrock Agents

**Explanation:**
Bedrock Agents enable foundation models to autonomously plan and execute multi-step tasks by connecting to external APIs and data sources through action groups. They can break down complex requests, call APIs, and orchestrate workflows. Knowledge Bases provide document retrieval. Guardrails filter content. Model Evaluation assesses model quality.
</details>

---

**Question 56**

A company is implementing RAG and needs to store document embeddings for fast similarity search. Which type of database is specifically designed for storing and querying high-dimensional vector embeddings?

A) Vector database (Amazon OpenSearch Serverless with vector engine)
B) Key-value store (Amazon DynamoDB)
C) Relational database (Amazon RDS)
D) Graph database (Amazon Neptune)

<details>
<summary>Show Answer</summary>
Correct Answer: A) Vector database (Amazon OpenSearch Serverless with vector engine)

**Explanation:**
Vector databases are optimized for storing high-dimensional embeddings and performing efficient similarity searches using algorithms like approximate nearest neighbor (ANN). Relational databases handle structured data with SQL queries. Key-value stores are for simple lookups. Graph databases model relationships between entities, not vector similarity.
</details>

---

**Question 57**

A software development team wants to use AI to help developers write code faster, get code suggestions inline, and generate code from natural language comments. Which AWS service is designed for this purpose?

A) Amazon Q Developer (formerly CodeWhisperer)
B) Amazon CodeGuru
C) AWS CloudFormation
D) Amazon SageMaker Autopilot

<details>
<summary>Show Answer</summary>
Correct Answer: A) Amazon Q Developer (formerly CodeWhisperer)

**Explanation:**
Amazon Q Developer (formerly CodeWhisperer) is an AI-powered coding companion that provides real-time code suggestions, generates code from natural language comments, and assists with code completion within IDEs. CodeGuru provides code reviews and performance recommendations. CloudFormation is for infrastructure as code. SageMaker Autopilot automates ML model building.
</details>

---

**Question 58**

A company wants to fine-tune a foundation model in Amazon Bedrock using their proprietary customer interaction data. Which requirement must they meet for the training data?

A) Training data must be publicly available on the internet
B) Training data must be stored in Amazon S3 in the supported format (JSONL with prompt-completion pairs)
C) Training data must be stored in Amazon DynamoDB
D) Training data must be at least 1 TB in size

<details>
<summary>Show Answer</summary>
Correct Answer: B) Training data must be stored in Amazon S3 in the supported format (JSONL with prompt-completion pairs)

**Explanation:**
Bedrock fine-tuning requires training data stored in Amazon S3 in specific formats like JSONL with prompt-completion pairs. The data doesn't need to be public - private proprietary data is the typical use case. DynamoDB is not a supported source for fine-tuning data. There's no minimum 1 TB requirement; fine-tuning works with relatively small datasets.
</details>

---

**Question 59**

A company is building a generative AI application using Amazon Bedrock Knowledge Bases. They need their documents chunked appropriately for retrieval. Which chunking strategy would work BEST for technical documentation with clear section boundaries?

A) Fixed-size chunking with 50-character chunks regardless of content
B) Random chunking with overlapping segments of varying sizes
C) No chunking - using entire documents as single retrievable units
D) Hierarchical chunking that respects document structure (sections and paragraphs)

<details>
<summary>Show Answer</summary>
Correct Answer: D) Hierarchical chunking that respects document structure (sections and paragraphs)

**Explanation:**
Hierarchical chunking preserves semantic coherence by following document structure, keeping related content together within sections and paragraphs. Very small fixed-size chunks may split important context. Using entire documents as single units returns too much irrelevant content and may exceed context windows. Random chunking disregards content structure.
</details>

---

**Question 60**

A company is using Amazon Q to help employees find information across their enterprise systems. Which statement BEST describes Amazon Q's primary capability?

A) It is a vector database for storing embeddings
B) It is a generative AI-powered assistant that connects to enterprise data sources to provide contextual answers and complete tasks
C) It is a model training platform for building custom LLMs
D) It is a data labeling tool for supervised learning

<details>
<summary>Show Answer</summary>
Correct Answer: B) It is a generative AI-powered assistant that connects to enterprise data sources to provide contextual answers and complete tasks

**Explanation:**
Amazon Q is an enterprise generative AI assistant that integrates with various data sources (wikis, documents, ticketing systems) to provide contextual answers, generate content, and automate tasks within enterprise workflows. It's not a vector database, model training platform, or data labeling tool.
</details>

---

**Question 61**

A team wants to build a no-code generative AI application for rapid prototyping and experimentation with foundation models. Which AWS tool allows business users to create AI-powered applications without writing code?

A) PartyRock (Amazon Bedrock Playground)
B) Amazon SageMaker Studio
C) AWS CloudFormation
D) Amazon EMR

<details>
<summary>Show Answer</summary>
Correct Answer: A) PartyRock (Amazon Bedrock Playground)

**Explanation:**
PartyRock is a no-code playground built on Amazon Bedrock that allows anyone to create, share, and experiment with generative AI applications without writing code or needing an AWS account. SageMaker Studio requires coding expertise. CloudFormation is for infrastructure provisioning. EMR is for big data processing.
</details>

---

**Question 62**

A developer is implementing a RAG system and needs to decide how to generate embeddings for their documents. Which consideration is MOST important when selecting an embedding model?

A) The embedding model must be the same model used for text generation
B) The embedding dimensions should match the vector database configuration, and the model should be trained on similar domain data
C) Embeddings should always be exactly 2 dimensions for visualization
D) The embedding model should only support English language text

<details>
<summary>Show Answer</summary>
Correct Answer: B) The embedding dimensions should match the vector database configuration, and the model should be trained on similar domain data

**Explanation:**
The embedding model's output dimensions must be compatible with the vector database index configuration, and domain-relevant training improves semantic similarity accuracy. The embedding and generation models are typically different. 2D embeddings lose too much information for retrieval. Multilingual support may be needed depending on the use case.
</details>

---

**Question 63**

A company is using Amazon Bedrock Agents and needs their agent to access current inventory data from their database when answering customer questions. How should the agent be configured to access this external data?

A) Configure action groups with Lambda functions that query the inventory database
B) The agent should be trained on all possible inventory data combinations
C) Hard-code all inventory levels into the system prompt
D) Use a larger foundation model that has memorized the inventory data

<details>
<summary>Show Answer</summary>
Correct Answer: A) Configure action groups with Lambda functions that query the inventory database

**Explanation:**
Bedrock Agents use action groups backed by Lambda functions to interact with external systems and databases in real-time. This allows dynamic data access without retraining. Pre-training on inventory data creates stale information. Hard-coding in prompts is impractical for changing data. No model memorizes specific business data.
</details>

---

**Question 64**

A team is building a multi-modal AI application that needs to analyze both images and text to generate descriptions of products from photographs. Which capability of foundation models enables this?

A) Models that only process text input but generate image descriptions from metadata
B) Multi-modal foundation models that accept both image and text inputs and generate text outputs
C) Separate models that must be trained independently for each modality
D) Models that convert all images to text before processing

<details>
<summary>Show Answer</summary>
Correct Answer: B) Multi-modal foundation models that accept both image and text inputs and generate text outputs

**Explanation:**
Multi-modal foundation models (like Claude 3, GPT-4V) can process multiple input types simultaneously, understanding visual content and generating text descriptions. They don't simply extract metadata from images. Modern multi-modal models process modalities jointly rather than requiring separate models. They analyze image pixels directly, not text conversions.
</details>

---

**Question 65**

A company wants to customize a foundation model's behavior for their specific use case without the full cost of fine-tuning. They want to add specific knowledge and adjust the response style using only prompt engineering. Which techniques should they combine? (Select TWO)

A) System prompts with detailed persona and behavioral instructions
B) Modifying the model's neural network weights directly
C) Few-shot examples demonstrating the desired input-output format
D) Changing the model's tokenizer vocabulary
E) Reducing the model's context window size

<details>
<summary>Show Answer</summary>
Correct Answers: A) System prompts with detailed persona and behavioral instructions and C) Few-shot examples demonstrating the desired input-output format

**Explanation:**
System prompts define persistent behavior guidelines and persona, while few-shot examples demonstrate the specific format and style expected. Together they customize model behavior without modifying weights, which is what makes them prompt engineering (not fine-tuning). Modifying weights or tokenizer requires training. Reducing context window limits capability.
</details>

---

**Question 66**

A developer is implementing conversation memory for their chatbot built on Amazon Bedrock. The application needs to maintain context across multiple user interactions within a session. Which approach is MOST appropriate?

A) Use a separate model for each conversation turn
B) Retrain the model after each user message
C) Store the entire conversation history and pass it with each new request within the context window
D) Store only the first message and discard all subsequent context

<details>
<summary>Show Answer</summary>
Correct Answer: C) Store the entire conversation history and pass it with each new request within the context window

**Explanation:**
Since LLMs are stateless, conversation memory is implemented by storing the chat history and including it in each subsequent API request within the model's context window. This allows the model to reference prior turns. Retraining per message is impractical. Separate models fragment context. Discarding history eliminates the ability to reference previous exchanges.
</details>

---

**Question 67**

A company has deployed a RAG application but finds that retrieved documents sometimes don't contain the answer to the user's question, leading to low-quality responses. Which improvement would MOST help address this retrieval quality issue?

A) Increasing the temperature of the generation model
B) Removing the retrieval step entirely and relying on the model's training knowledge
C) Using a smaller embedding model with fewer dimensions
D) Improving the chunking strategy and adding metadata filtering to refine retrieval results

<details>
<summary>Show Answer</summary>
Correct Answer: D) Improving the chunking strategy and adding metadata filtering to refine retrieval results

**Explanation:**
Better chunking preserves semantic context, and metadata filtering narrows retrieval to relevant document subsets, both improving retrieval quality. Higher temperature affects generation randomness, not retrieval. Smaller embeddings may lose important semantic information. Removing retrieval eliminates the RAG benefit and increases hallucination risk.
</details>

---

**Question 68**

A data scientist is using Amazon Bedrock to evaluate different foundation models for a summarization task. They want to objectively compare model outputs across multiple dimensions. Which Amazon Bedrock feature supports automated and human model evaluation?

A) Amazon Bedrock Model Evaluation
B) Amazon Bedrock Knowledge Bases
C) Amazon Bedrock Guardrails
D) Amazon Bedrock Provisioned Throughput

<details>
<summary>Show Answer</summary>
Correct Answer: A) Amazon Bedrock Model Evaluation

**Explanation:**
Bedrock Model Evaluation enables both automatic evaluation (using metrics like accuracy, robustness, toxicity) and human evaluation workflows to compare foundation model outputs for specific use cases. Guardrails filter content. Knowledge Bases implement RAG. Provisioned Throughput reserves model capacity for consistent performance.
</details>

---

**Question 69**

A team is building a document processing pipeline using generative AI. They need to extract structured information (names, dates, amounts) from unstructured contracts. Which approach combines the strengths of foundation models with structured output requirements?

A) Prompting a foundation model with explicit output schema instructions and validation
B) Using regular expressions only for all extraction
C) Manual human review of every document
D) Using only keyword matching without AI

<details>
<summary>Show Answer</summary>
Correct Answer: A) Prompting a foundation model with explicit output schema instructions and validation

**Explanation:**
Foundation models can understand natural language context in contracts and extract information into structured formats when given explicit schema instructions, combining AI understanding with structured output. Regex alone can't handle natural language variability. Manual review doesn't scale. Keyword matching misses contextual information.
</details>

---

**Question 70**

A company wants to use Amazon Bedrock to generate images from text descriptions for their marketing materials. Which foundation model family available through Bedrock is specifically designed for text-to-image generation?

A) Anthropic Claude
B) Stability AI (Stable Diffusion)
C) Amazon Titan Text
D) Cohere Command

<details>
<summary>Show Answer</summary>
Correct Answer: B) Stability AI (Stable Diffusion)

**Explanation:**
Stability AI's Stable Diffusion models, available through Amazon Bedrock, are specifically designed for text-to-image generation. Anthropic Claude is a text/multimodal model for conversation and analysis. Amazon Titan Text generates text. Cohere Command is for text generation and understanding.
</details>

---

**Question 71**

A developer wants to implement a safeguard that prevents their Bedrock-powered application from responding to requests about topics unrelated to their business (e.g., political opinions, medical advice). Which Bedrock Guardrails feature addresses this?

A) Content filters for harmful content categories
B) Word-level filters for profanity
C) PII detection and redaction
D) Denied topic policies that block specified off-topic subjects

<details>
<summary>Show Answer</summary>
Correct Answer: D) Denied topic policies that block specified off-topic subjects

**Explanation:**
Denied topic policies in Bedrock Guardrails allow you to define specific topics the model should refuse to discuss, keeping conversations focused on relevant business subjects. Content filters handle harmful content categories (hate, violence). PII detection handles personal data. Word filters block specific terms, not topic areas.
</details>

---

**Question 72**

A company is building a customer-facing AI application with Amazon Bedrock. They need to ensure responses don't contain any personally identifiable information (PII) like phone numbers or email addresses. Which Bedrock Guardrails capability should they configure?

A) Topic filtering policies
B) Custom word lists
C) Content filters for hate speech
D) Sensitive information filters with PII detection and redaction

<details>
<summary>Show Answer</summary>
Correct Answer: D) Sensitive information filters with PII detection and redaction

**Explanation:**
Bedrock Guardrails' sensitive information filters can detect and redact PII types such as phone numbers, email addresses, SSNs, and other personal data from both inputs and outputs. Topic filtering blocks subjects. Content filters handle harmful categories. Word lists block specific terms but aren't intelligent about PII patterns.
</details>

---

**Question 73**

A team is using Amazon Bedrock Knowledge Bases for their RAG application. They want to improve retrieval accuracy by using semantic search. What underlying technology enables semantic search to find conceptually related documents even when exact keywords don't match?

A) SQL database queries with LIKE operators
B) Simple string matching algorithms
C) Vector embeddings that represent semantic meaning in mathematical space
D) File system directory structure

<details>
<summary>Show Answer</summary>
Correct Answer: C) Vector embeddings that represent semantic meaning in mathematical space

**Explanation:**
Semantic search uses vector embeddings to represent text meaning as mathematical vectors in high-dimensional space, where conceptually similar content has vectors close together regardless of exact wording. SQL LIKE operators and string matching only find literal text matches. File system structure has no semantic understanding.
</details>

---

**Question 74**

A developer is implementing a Bedrock Agent that needs to decide between multiple action groups based on user intent. The agent must determine whether to search a knowledge base, call an API, or ask for clarification. What enables this decision-making capability?

A) Hard-coded if-else rules in the application
B) User manually selecting which action to take each time
C) A separate classification model that must be trained first
D) The foundation model's reasoning capabilities combined with action group descriptions and instructions

<details>
<summary>Show Answer</summary>
Correct Answer: D) The foundation model's reasoning capabilities combined with action group descriptions and instructions

**Explanation:**
Bedrock Agents leverage the underlying foundation model's reasoning ability to interpret user intent and select appropriate action groups based on their descriptions and the agent's instructions. This is orchestrated by the model, not hard-coded rules. No separate classification model is needed. Users don't manually select actions.
</details>

---

**Question 75**

A company wants to use generative AI to analyze their existing codebase, identify bugs, and suggest improvements. Which AWS service provides AI-powered code analysis and security scanning integrated into the development workflow?

A) Amazon Q Developer
B) AWS CloudTrail
C) Amazon Kinesis
D) AWS Config

<details>
<summary>Show Answer</summary>
Correct Answer: A) Amazon Q Developer

**Explanation:**
Amazon Q Developer provides AI-powered code analysis, security vulnerability scanning, bug detection, and improvement suggestions integrated into IDEs and CI/CD workflows. CloudTrail logs API activity. Kinesis processes streaming data. AWS Config tracks resource configurations.
</details>

---

**Question 76**

A team has built a RAG application that retrieves relevant documents but sometimes generates responses that don't properly synthesize the retrieved information. Which approach would MOST improve the generation quality given already-relevant retrieved documents?

A) Retrieving more documents regardless of relevance
B) Using a smaller context window
C) Optimizing the generation prompt with clear instructions on how to use retrieved context and cite sources
D) Removing the system prompt

<details>
<summary>Show Answer</summary>
Correct Answer: C) Optimizing the generation prompt with clear instructions on how to use retrieved context and cite sources

**Explanation:**
When retrieval quality is good but generation quality is poor, the issue is in how the model uses the context. Clear prompt instructions on synthesizing retrieved information and citing sources improve generation quality. More irrelevant documents add noise. Smaller context windows limit available information. Removing system prompts reduces control over response formatting.
</details>

---

**Question 77**

A developer needs to configure inference parameters for a text generation model on Amazon Bedrock. They want to limit the response length to prevent excessive token usage. Which parameter controls the maximum number of tokens the model will generate?

A) Temperature
B) Max tokens (maximum generation length)
C) Top-p
D) Stop sequences

<details>
<summary>Show Answer</summary>
Correct Answer: B) Max tokens (maximum generation length)

**Explanation:**
The max tokens parameter directly limits how many tokens the model will generate in its response, controlling output length and token costs. Temperature controls randomness. Top-p filters token probabilities. Stop sequences terminate generation at specific strings but don't set a hard length limit.
</details>

---

**Question 78**

A company is deploying a Bedrock-powered application that needs to handle high traffic with consistent low-latency responses. They want guaranteed throughput rather than shared on-demand capacity. Which Bedrock pricing option should they choose?

A) On-demand pricing with pay-per-token
B) Free tier with rate limiting
C) Spot instances for foundation models
D) Provisioned Throughput with reserved model capacity

<details>
<summary>Show Answer</summary>
Correct Answer: D) Provisioned Throughput with reserved model capacity

**Explanation:**
Provisioned Throughput reserves dedicated model capacity ensuring consistent performance and guaranteed throughput for high-traffic applications. On-demand pricing is pay-per-use but shares capacity and may have variable latency under load. There are no spot instances for Bedrock models. Free tier has significant limitations.
</details>

---

**Question 79**

A team is building a RAG application and needs to decide on a vector database solution that integrates natively with Amazon Bedrock Knowledge Bases. Which options are supported as vector stores? (Select TWO)

A) Amazon DynamoDB
B) Amazon OpenSearch Serverless
C) Amazon Redshift Serverless
D) Pinecone
E) Amazon RDS for MySQL

<details>
<summary>Show Answer</summary>
Correct Answers: B) Amazon OpenSearch Serverless and D) Pinecone

**Explanation:**
Amazon Bedrock Knowledge Bases supports multiple vector store options including Amazon OpenSearch Serverless, Pinecone, Redis Enterprise Cloud, and Amazon Aurora PostgreSQL with pgvector. DynamoDB is a key-value store without vector search. Redshift is for analytics. Standard RDS MySQL doesn't support vector operations natively.
</details>

---

**Question 80**

A developer is building a text summarization application and needs to handle documents that exceed the foundation model's context window. Which technique allows processing documents longer than the model's maximum input length?

A) Chunking the document and using iterative/hierarchical summarization (map-reduce approach)
B) Simply truncating the document to fit the context window
C) Increasing the temperature to process more text
D) Switching to a model with infinite context length

<details>
<summary>Show Answer</summary>
Correct Answer: A) Chunking the document and using iterative/hierarchical summarization (map-reduce approach)

**Explanation:**
The map-reduce approach splits long documents into chunks that fit the context window, summarizes each chunk separately, then combines the summaries for a final summary. Truncation loses information. Temperature doesn't affect context capacity. No current model has truly infinite context length.
</details>

---

**Question 81**

A company is using Amazon Q Business to help employees find information. They need to ensure that employees can only access answers derived from documents they have permission to view. Which feature enables this access control?

A) Document-level access control lists (ACLs) that respect existing enterprise permissions
B) Setting the model temperature to zero
C) Deploying a separate Q instance for each employee
D) Using content filters to block all responses

<details>
<summary>Show Answer</summary>
Correct Answer: A) Document-level access control lists (ACLs) that respect existing enterprise permissions

**Explanation:**
Amazon Q Business integrates with enterprise identity providers and respects document-level ACLs, ensuring users only receive answers from documents they're authorized to access. Temperature settings don't affect access control. Separate instances per employee is impractical and expensive. Blocking all responses defeats the purpose.
</details>

---

**Question 82**

A team is fine-tuning a foundation model on Amazon Bedrock and wants to evaluate whether the fine-tuned model outperforms the base model on their specific task. Which evaluation approach provides the MOST comprehensive comparison?

A) Comparing only the training loss between models
B) Comparing the models' pre-training dataset sizes
C) Checking which model has more parameters
D) Running both models on a held-out test set and comparing task-specific metrics plus human evaluation

<details>
<summary>Show Answer</summary>
Correct Answer: D) Running both models on a held-out test set and comparing task-specific metrics plus human evaluation

**Explanation:**
Comprehensive evaluation requires testing on unseen data with task-relevant metrics (accuracy, ROUGE, BLEU) combined with human evaluation for quality aspects that automated metrics may miss. Training loss alone doesn't measure real-world performance. Parameter count doesn't determine task-specific quality. Pre-training dataset size is irrelevant to fine-tuned performance comparison.
</details>

---

**Question 83**

A developer wants to create an application that can search through company meeting transcripts and answer questions about past discussions. Which combination of Amazon Bedrock features would create this application with minimal custom development? (Select TWO)

A) Amazon Bedrock Knowledge Bases to index and retrieve relevant transcript passages
B) Amazon Bedrock Custom Model Import to train a model on transcripts
C) A foundation model (like Claude) to generate answers based on retrieved context
D) Amazon Bedrock Provisioned Throughput to train the model
E) Amazon Bedrock Guardrails to generate the answers

<details>
<summary>Show Answer</summary>
Correct Answers: A) Amazon Bedrock Knowledge Bases to index and retrieve relevant transcript passages and C) A foundation model (like Claude) to generate answers based on retrieved context

**Explanation:**
Knowledge Bases handles document ingestion, chunking, embedding, and retrieval of relevant transcript passages. A foundation model then generates natural language answers from the retrieved context. This is standard RAG architecture. Custom Model Import is for bringing external models. Provisioned Throughput is for capacity, not training. Guardrails filter content but don't generate answers.
</details>

---

**Question 84**

A company is considering using parameter-efficient fine-tuning (PEFT) techniques like LoRA instead of full fine-tuning for their foundation model. Which advantage does PEFT provide over full fine-tuning?

A) PEFT always produces better model accuracy than full fine-tuning
B) PEFT eliminates the need for any training data
C) PEFT requires more training data than full fine-tuning
D) PEFT reduces computational cost and storage by training only a small number of additional parameters while freezing most of the original model

<details>
<summary>Show Answer</summary>
Correct Answer: D) PEFT reduces computational cost and storage by training only a small number of additional parameters while freezing most of the original model

**Explanation:**
PEFT techniques like LoRA add small trainable matrices while keeping the original model frozen, dramatically reducing compute, memory, and storage requirements. Full fine-tuning can still achieve better accuracy in some cases, so PEFT doesn't always outperform it. PEFT doesn't require more data, and it still requires some training data.
</details>

---

**Question 85**

A team is deploying a generative AI application and wants to implement content moderation that scans both user inputs and model outputs for harmful content. They need to filter hate speech, violence, and sexual content. Which approach provides the MOST integrated solution on AWS?

A) Building a custom classification model from scratch for each content category
B) Manually reviewing all inputs and outputs before displaying them
C) Configuring Amazon Bedrock Guardrails with content filter policies for specific harm categories
D) Blocking all requests that contain more than 100 words

<details>
<summary>Show Answer</summary>
Correct Answer: C) Configuring Amazon Bedrock Guardrails with content filter policies for specific harm categories

**Explanation:**
Bedrock Guardrails provides built-in content filters that can be configured for specific harm categories (hate, insults, sexual, violence, misconduct) with adjustable strength levels, applied to both inputs and outputs. Building custom models is costly and complex. Manual review doesn't scale. Word count limits don't identify harmful content.
</details>

---

**Question 86**

A developer is working with Amazon Bedrock and needs to maintain a persistent conversation with context. They are using the Converse API. How does the API handle conversation state?

A) The API automatically stores all conversation history server-side indefinitely
B) Each API call automatically includes the previous 100 messages from a session database
C) Conversation state is stored in the model's weights permanently
D) The developer must pass the full message history array with each API call since the service is stateless

<details>
<summary>Show Answer</summary>
Correct Answer: D) The developer must pass the full message history array with each API call since the service is stateless

**Explanation:**
The Bedrock Converse API is stateless - it doesn't store conversation history between calls. Developers must maintain and pass the full message array (conversation turns) with each request to provide context. The service doesn't store history server-side, model weights don't change at inference time, and there's no automatic session database.
</details>

---

**Question 87**

A company wants to deploy a generative AI solution that answers questions about their product catalog. They need the solution to be production-ready with minimal development effort. Which approach provides the fastest path to production while maintaining accuracy?

A) Training a custom LLM from scratch on product data
B) Hiring a team to manually write answers for every possible question
C) Using Amazon Bedrock Knowledge Bases with their product documentation as the data source
D) Using a general-purpose search engine without AI

<details>
<summary>Show Answer</summary>
Correct Answer: C) Using Amazon Bedrock Knowledge Bases with their product documentation as the data source

**Explanation:**
Bedrock Knowledge Bases provides a managed RAG solution that ingests product documentation, creates embeddings, and enables accurate Q&A with minimal development effort. Training from scratch requires massive resources and time. Manual answer writing doesn't scale. A search engine without AI can't generate natural language answers.
</details>

---

**Question 88**

A company has deployed a loan approval ML model and discovers it disproportionately denies applications from certain demographic groups, even when applicants have similar financial profiles. What is this type of issue called in responsible AI?

A) Model drift
B) Feature leakage
C) Underfitting
D) Algorithmic bias leading to disparate impact

<details>
<summary>Show Answer</summary>
Correct Answer: D) Algorithmic bias leading to disparate impact

**Explanation:**
Disparate impact occurs when a model's decisions disproportionately affect protected demographic groups negatively, even without explicit discriminatory intent. This is a form of algorithmic bias. Model drift refers to performance degradation over time. Underfitting is when models are too simple. Feature leakage is when test data information leaks into training.
</details>

---

**Question 89**

A healthcare company is using an ML model to assist doctors in diagnosing diseases. They need to explain to patients why the model made a specific recommendation. Which tool in the AWS ecosystem helps generate explanations for individual model predictions?

A) Amazon SageMaker Clarify
B) Amazon SageMaker Model Monitor
C) Amazon SageMaker Data Wrangler
D) Amazon SageMaker Autopilot

<details>
<summary>Show Answer</summary>
Correct Answer: A) Amazon SageMaker Clarify

**Explanation:**
SageMaker Clarify provides model explainability through SHAP values and feature attribution, showing which factors influenced specific predictions. It also detects bias in data and models. Model Monitor tracks data quality and drift. Data Wrangler prepares data. Autopilot automates model building but doesn't focus on explanations.
</details>

---

**Question 90**

A financial services company wants to ensure their AI credit scoring model treats all applicants fairly. They need to measure whether the model's approval rates are equal across different demographic groups. Which fairness metric specifically measures this?

A) Root Mean Squared Error
B) AUC-ROC
C) Demographic parity (statistical parity)
D) Perplexity

<details>
<summary>Show Answer</summary>
Correct Answer: C) Demographic parity (statistical parity)

**Explanation:**
Demographic parity measures whether the positive prediction rate (e.g., loan approval rate) is equal across different demographic groups. RMSE measures regression error. AUC-ROC measures overall model discrimination ability. Perplexity evaluates language model quality. None of these other metrics directly assess fairness across groups.
</details>

---

**Question 91**

A company is deploying an AI system for hiring recommendations. To maintain accountability and transparency, their legal team requires documentation of the model's intended use, limitations, evaluation results, and ethical considerations. What type of document serves this purpose?

A) API documentation
B) Service level agreement
C) User manual
D) Model card

<details>
<summary>Show Answer</summary>
Correct Answer: D) Model card

**Explanation:**
Model cards are standardized documents that describe a model's intended use cases, limitations, evaluation metrics, training data characteristics, ethical considerations, and potential biases. They promote transparency and informed decision-making. API documentation covers technical interfaces. User manuals guide end users. SLAs define service guarantees.
</details>

---

**Question 92**

A team has deployed an AI content moderation system that makes automated decisions about removing user posts. Some users have complained about incorrect removals. Which responsible AI principle suggests that affected users should have a mechanism to challenge and appeal automated decisions?

A) Feature engineering
B) Gradient descent optimization
C) Human-in-the-loop and contestability
D) Data augmentation

<details>
<summary>Show Answer</summary>
Correct Answer: C) Human-in-the-loop and contestability

**Explanation:**
Human-in-the-loop ensures humans can review, override, and appeal automated decisions, particularly for high-stakes cases. Contestability gives affected individuals the ability to challenge AI decisions. Feature engineering is a data preparation technique. Gradient descent is an optimization algorithm. Data augmentation increases training data variety.
</details>

---

**Question 93**

A data scientist wants to understand why their image classification model misclassifies certain images. They need a technique that highlights which regions of the input image most influenced the model's prediction. Which explainability method provides visual explanations for image models?

A) Confusion matrix
B) One-hot encoding visualization
C) LIME (Local Interpretable Model-agnostic Explanations) with image superpixels
D) ROC curve analysis

<details>
<summary>Show Answer</summary>
Correct Answer: C) LIME (Local Interpretable Model-agnostic Explanations) with image superpixels

**Explanation:**
LIME for images perturbs superpixels (regions) of the input and observes changes in prediction, creating visual explanations showing which image regions most influenced the classification. One-hot encoding is a feature representation method. Confusion matrices show aggregate performance. ROC curves measure threshold trade-offs, none of which explain individual image predictions.
</details>

---

**Question 94**

A company is building an AI-powered resume screening tool. During testing, they discover the model penalizes resumes that mention women's colleges or women's sports leagues. Which steps should they take to address this bias? (Select TWO)

A) Deploy the model immediately since it has high overall accuracy
B) Audit training data for historical hiring biases and remove or rebalance biased examples
C) Ignore the issue since the model wasn't explicitly programmed to be biased
D) Implement bias detection using SageMaker Clarify and retrain with debiased data
E) Add more biased data to make the bias consistent

<details>
<summary>Show Answer</summary>
Correct Answers: B) Audit training data for historical hiring biases and remove or rebalance biased examples and D) Implement bias detection using SageMaker Clarify and retrain with debiased data

**Explanation:**
Addressing bias requires both identifying the source (auditing training data for historical biases) and implementing systematic detection (SageMaker Clarify) followed by remediation. High accuracy doesn't excuse discriminatory outcomes. Bias doesn't require explicit programming - it often comes from historical data patterns. Adding more biased data worsens the problem.
</details>

---

**Question 95**

A company is developing an AI system that makes medical treatment recommendations. Which responsible AI principle requires that patients and doctors understand how and why the system arrived at its recommendation?

A) Scalability
B) Transparency and explainability
C) Cost optimization
D) Data compression

<details>
<summary>Show Answer</summary>
Correct Answer: B) Transparency and explainability

**Explanation:**
Transparency requires that AI systems' decision-making processes be understandable to stakeholders, especially in high-stakes domains like healthcare. Explainability provides the mechanisms to understand specific decisions. Scalability, cost optimization, and data compression are technical concerns unrelated to responsible AI principles.
</details>

---

**Question 96**

A team is using Amazon SageMaker Clarify to evaluate their model for bias. Which types of bias can SageMaker Clarify detect? (Select TWO)

A) Pre-training bias in the training dataset (before model training)
B) Hardware manufacturing bias in GPU chips
C) Post-training bias in model predictions (after model training)
D) Network latency bias in API responses
E) Storage bias in S3 bucket configurations

<details>
<summary>Show Answer</summary>
Correct Answers: A) Pre-training bias in the training dataset (before model training) and C) Post-training bias in model predictions (after model training)

**Explanation:**
SageMaker Clarify detects pre-training bias (imbalances in training data before model training) and post-training bias (unfair predictions after the model is trained). It analyzes data distributions and model outputs across groups. Hardware, network, and storage biases are infrastructure concepts unrelated to ML fairness.
</details>

---

**Question 97**

A company is designing an AI-powered customer service chatbot for a diverse global audience. Which inclusive design principle should guide the development of this system?

A) Designing only for the majority demographic to maximize efficiency
B) Testing with diverse user groups and ensuring equitable performance across languages, accents, and cultural contexts
C) Using only English language training data since it's the most common business language
D) Optimizing exclusively for response speed regardless of accuracy across demographics

<details>
<summary>Show Answer</summary>
Correct Answer: B) Testing with diverse user groups and ensuring equitable performance across languages, accents, and cultural contexts

**Explanation:**
Inclusive design requires considering diverse users from the start, testing with representative populations, and ensuring equitable performance regardless of language, culture, or ability. Designing for only the majority excludes significant populations. English-only ignores global users. Speed without equitable accuracy creates disparate service quality.
</details>

---

**Question 98**

A data scientist is using SHAP values to explain their model's predictions. A customer's loan application was denied, and the SHAP analysis shows that "employment_length" had the highest negative contribution. What does this tell the team?

A) The employment_length feature should be removed from the model entirely
B) SHAP values indicate the feature is not important to the model
C) The model is completely broken and should be retrained
D) The customer's short employment length was the primary factor pushing the prediction toward denial

<details>
<summary>Show Answer</summary>
Correct Answer: D) The customer's short employment length was the primary factor pushing the prediction toward denial

**Explanation:**
SHAP values show how each feature contributes to a specific prediction relative to the baseline. A high negative SHAP value for employment_length means this feature strongly pushed the prediction toward denial for this customer. It doesn't mean the feature should be removed (it may be legitimately predictive) or that the model is broken.
</details>

---

**Question 99**

A company is deploying a facial recognition system and is concerned about disparate performance across different skin tones and ethnicities. Which responsible AI practice should they implement BEFORE deployment?

A) Deploy first and address complaints as they arise
B) Focus solely on overall accuracy without subgroup analysis
C) Only test with synthetic data generated by AI
D) Evaluate model performance across demographic subgroups and ensure equitable accuracy rates

<details>
<summary>Show Answer</summary>
Correct Answer: D) Evaluate model performance across demographic subgroups and ensure equitable accuracy rates

**Explanation:**
Pre-deployment evaluation across demographic subgroups (disaggregated evaluation) identifies performance disparities before they cause harm. Deploying first and waiting for complaints causes real-world harm. Synthetic data may not represent real demographic diversity. Overall accuracy can mask significant performance gaps between subgroups.
</details>

---

**Question 100**

A team has deployed an AI system that autonomously makes decisions affecting people's lives (insurance claims, bail decisions). Which governance framework principle requires that there always be a designated person or entity responsible for the AI system's outcomes?

A) Accountability
B) Feature importance
C) Gradient optimization
D) Tokenization

<details>
<summary>Show Answer</summary>
Correct Answer: A) Accountability

**Explanation:**
Accountability in AI governance requires clear designation of who is responsible for the AI system's decisions and their impacts. It ensures that humans cannot abdicate responsibility by attributing decisions solely to an algorithm. Feature importance, gradient optimization, and tokenization are technical ML concepts unrelated to governance principles.
</details>

---

**Question 101**

A company wants to implement responsible AI practices for their generative AI application. They need to prevent the model from generating harmful, biased, or inappropriate content in production. Which layered approach provides the MOST comprehensive protection?

A) Relying solely on the model's built-in training alignment
B) Only implementing output filtering and ignoring input validation
C) Combining model alignment, input/output guardrails, content filtering, and human review for edge cases
D) Asking users to self-moderate their interactions

<details>
<summary>Show Answer</summary>
Correct Answer: C) Combining model alignment, input/output guardrails, content filtering, and human review for edge cases

**Explanation:**
A defense-in-depth approach layers multiple safeguards: model alignment during training, runtime guardrails for both inputs and outputs, content filtering rules, and human review for challenging cases. No single layer is sufficient alone. Relying only on training alignment misses adversarial prompts. Output-only filtering misses harmful inputs. User self-moderation is unreliable.
</details>

---

**Question 102**

A machine learning team wants to document their model's limitations and appropriate use cases to prevent misuse. According to responsible AI best practices, which information should be included in their model documentation? (Select TWO)

A) The exact salary of each team member who built the model
B) Known limitations, failure modes, and populations where the model may not perform well
C) Intended use cases and explicitly out-of-scope applications
D) Competitors' proprietary model architectures
E) Personal information of the training data subjects

<details>
<summary>Show Answer</summary>
Correct Answers: B) Known limitations, failure modes, and populations where the model may not perform well and C) Intended use cases and explicitly out-of-scope applications

**Explanation:**
Responsible model documentation should clearly state known limitations and failure modes so users understand risks, and define intended vs. out-of-scope use cases to prevent misuse. Team salaries are private HR information. Competitors' architectures are proprietary. Including personal data of training subjects would violate privacy.
</details>

---

**Question 103**

A company is developing an AI system for automated content generation. They want to ensure users can always distinguish between AI-generated content and human-created content. Which responsible AI principle does this represent?

A) Cost efficiency
B) Model compression
C) Transparency through AI content disclosure and watermarking
D) Distributed computing

<details>
<summary>Show Answer</summary>
Correct Answer: C) Transparency through AI content disclosure and watermarking

**Explanation:**
Transparency in generative AI includes disclosing when content is AI-generated, potentially through watermarking or explicit labeling, so users can make informed judgments about the content's origin and reliability. Cost efficiency, model compression, and distributed computing are technical implementation concerns unrelated to responsible AI disclosure.
</details>

---

**Question 104**

A healthcare AI company is implementing responsible AI governance. Their model assists in diagnosing rare diseases, but the team acknowledges the model has a 15% error rate for certain rare conditions. Which responsible AI practice should guide their deployment decision?

A) Implement human-in-the-loop oversight where clinicians validate AI suggestions before acting, and clearly communicate the model's limitations
B) Deploy without disclosure since 85% accuracy is sufficient
C) Remove the model from all medical use cases entirely
D) Only deploy in regions where medical regulations don't apply

<details>
<summary>Show Answer</summary>
Correct Answer: A) Implement human-in-the-loop oversight where clinicians validate AI suggestions before acting, and clearly communicate the model's limitations

**Explanation:**
For high-stakes medical decisions with known error rates, human-in-the-loop ensures qualified professionals validate AI recommendations before patient action, while communicating limitations enables informed use. Deploying without disclosure is irresponsible. Complete removal may deny patients a useful assistive tool. Avoiding regulations is unethical.
</details>

---

**Question 105**

A company is deploying an Amazon SageMaker training job that processes sensitive patient health data. They need to ensure the training data is encrypted both at rest and in transit. Which AWS services and features should they use? (Select TWO)

A) AWS KMS for managing encryption keys used by SageMaker to encrypt data at rest
B) Storing data in unencrypted public S3 buckets
C) TLS/SSL encryption for data in transit between S3 and the training instance
D) Disabling VPC configuration for easier network access
E) Using HTTP instead of HTTPS for faster data transfer

<details>
<summary>Show Answer</summary>
Correct Answers: A) AWS KMS for managing encryption keys used by SageMaker to encrypt data at rest and C) TLS/SSL encryption for data in transit between S3 and the training instance

**Explanation:**
AWS KMS provides managed encryption keys that SageMaker uses to encrypt training data, model artifacts, and volumes at rest. TLS/SSL secures data in transit between services. Unencrypted public buckets expose sensitive data. Disabling VPC removes network isolation. HTTP without encryption exposes data during transfer.
</details>

---

**Question 106**

A company wants to ensure their Amazon SageMaker notebook instances and training jobs are isolated within their own private network and cannot be accessed from the public internet. Which AWS networking feature enables this isolation?

A) Amazon CloudFront distribution
B) Amazon Route 53 public hosted zone
C) Amazon VPC (Virtual Private Cloud) with private subnets
D) AWS Global Accelerator

<details>
<summary>Show Answer</summary>
Correct Answer: C) Amazon VPC (Virtual Private Cloud) with private subnets

**Explanation:**
Deploying SageMaker resources within a VPC using private subnets ensures network isolation from the public internet. Security groups and NACLs provide additional access control. CloudFront is a CDN for content delivery. Route 53 manages DNS. Global Accelerator optimizes network performance but doesn't provide isolation.
</details>

---

**Question 107**

A security team needs to audit all API calls made to Amazon Bedrock in their AWS account, including who made the call, when it was made, and from which IP address. Which AWS service provides this audit trail?

A) Amazon CloudWatch Metrics
B) AWS Trusted Advisor
C) Amazon Inspector
D) AWS CloudTrail

<details>
<summary>Show Answer</summary>
Correct Answer: D) AWS CloudTrail

**Explanation:**
AWS CloudTrail records all AWS API calls including those to Amazon Bedrock, capturing the identity of the caller, timestamp, source IP, request parameters, and response. CloudWatch Metrics provides operational metrics. Inspector assesses security vulnerabilities. Trusted Advisor provides best practice recommendations.
</details>

---

**Question 108**

A company is using Amazon Bedrock and needs to control which IAM users and roles can invoke specific foundation models. Which AWS mechanism provides this fine-grained access control?

A) Amazon Bedrock Guardrails
B) AWS WAF rules
C) Amazon VPC security groups
D) IAM policies with Bedrock-specific actions and resource ARNs

<details>
<summary>Show Answer</summary>
Correct Answer: D) IAM policies with Bedrock-specific actions and resource ARNs

**Explanation:**
IAM policies allow fine-grained access control specifying which users/roles can perform which Bedrock actions (like InvokeModel) on which specific model resources (using ARNs). Bedrock Guardrails filter content, not access. VPC security groups control network traffic, not service permissions. WAF protects web applications from exploits.
</details>

---

**Question 109**

A healthcare organization is building an AI application on AWS that processes protected health information (PHI). Which compliance framework must they ensure their AWS services configuration adheres to?

A) HIPAA (Health Insurance Portability and Accountability Act)
B) PCI DSS only
C) SOX (Sarbanes-Oxley) only
D) FISMA only

<details>
<summary>Show Answer</summary>
Correct Answer: A) HIPAA (Health Insurance Portability and Accountability Act)

**Explanation:**
HIPAA governs the protection of protected health information (PHI) and requires specific safeguards for healthcare data. AWS offers HIPAA-eligible services and Business Associate Agreements (BAAs). PCI DSS covers payment card data. SOX covers financial reporting. FISMA covers federal government information systems.
</details>

---

**Question 110**

A company operating in Europe is using Amazon Bedrock and must ensure that their data is processed and stored only within the EU to comply with data sovereignty requirements. Which AWS capability helps address this?

A) Using AWS Global Accelerator to route traffic worldwide
B) Using CloudFront to cache data globally
C) Enabling cross-region replication to all regions
D) Choosing an AWS Region located within the EU for Bedrock resources

<details>
<summary>Show Answer</summary>
Correct Answer: D) Choosing an AWS Region located within the EU for Bedrock resources

**Explanation:**
AWS Regions are physically isolated locations, and selecting an EU Region ensures data processing and storage remain within EU boundaries for data residency compliance. CloudFront global caching, cross-region replication, and Global Accelerator all distribute data beyond the EU, violating sovereignty requirements.
</details>

---

**Question 111**

A security engineer needs to establish a private connection between their VPC and Amazon SageMaker endpoints without traffic traversing the public internet. Which AWS service creates this private connectivity?

A) AWS PrivateLink (VPC Endpoints)
B) AWS Direct Connect
C) Internet Gateway
D) NAT Gateway

<details>
<summary>Show Answer</summary>
Correct Answer: A) AWS PrivateLink (VPC Endpoints)

**Explanation:**
AWS PrivateLink creates private connections between VPCs and AWS services through VPC endpoints, ensuring traffic stays within the AWS network without traversing the public internet. Direct Connect connects on-premises to AWS. Internet Gateways provide public internet access. NAT Gateways allow outbound internet access from private subnets.
</details>

---

**Question 112**

A company wants to detect sensitive data like credit card numbers and personal identifiers in their S3 data lake before using it for ML training. Which AWS service automatically discovers, classifies, and protects sensitive data at scale?

A) Amazon GuardDuty
B) Amazon Macie
C) AWS Config
D) Amazon Detective

<details>
<summary>Show Answer</summary>
Correct Answer: B) Amazon Macie

**Explanation:**
Amazon Macie uses machine learning to automatically discover, classify, and protect sensitive data (PII, financial data, credentials) stored in Amazon S3. GuardDuty detects threats and suspicious activity. AWS Config tracks resource configurations. Detective investigates security findings. None of these others specialize in sensitive data discovery.
</details>

---

**Question 113**

A company is using both Amazon Bedrock and Amazon SageMaker. Under the AWS Shared Responsibility Model, which security responsibilities belong to the CUSTOMER? (Select TWO)

A) Physical security of AWS data centers
B) Configuring IAM policies to control access to AI services
C) Patching the underlying hypervisor and hardware
D) Encrypting sensitive training data and managing encryption keys
E) Maintaining the global AWS network infrastructure

<details>
<summary>Show Answer</summary>
Correct Answers: B) Configuring IAM policies to control access to AI services and D) Encrypting sensitive training data and managing encryption keys

**Explanation:**
Under the Shared Responsibility Model, customers are responsible for security "in" the cloud: IAM configuration, data encryption, access management, and application security. AWS is responsible for security "of" the cloud: physical data center security, hypervisor patching, and global network infrastructure maintenance.
</details>

---

**Question 114**

A security team wants to prevent prompt injection attacks where malicious users try to manipulate their Bedrock-powered application into ignoring system instructions. Which combination of defenses is MOST effective?

A) Only increasing the model's temperature setting
B) Input validation, Amazon Bedrock Guardrails with denied topics, and robust system prompts with clear boundaries
C) Removing all system prompts so there's nothing to override
D) Allowing all user inputs without any filtering

<details>
<summary>Show Answer</summary>
Correct Answer: B) Input validation, Amazon Bedrock Guardrails with denied topics, and robust system prompts with clear boundaries

**Explanation:**
Defending against prompt injection requires multiple layers: validating and sanitizing inputs, using Bedrock Guardrails to filter dangerous patterns, and designing robust system prompts that are difficult to override. Temperature settings don't prevent injection. Removing system prompts removes desired behavior controls. No filtering allows all attacks through.
</details>

---

**Question 115**

A company processes data subject to GDPR and needs to implement the "right to be forgotten" for their ML models trained on personal data. Which challenge does this present for machine learning systems?

A) It's impossible to comply with GDPR when using ML
B) They may need to retrain models after removing specific individual's data, or use techniques like machine unlearning
C) GDPR doesn't apply to machine learning models
D) Simply deleting the S3 training files is always sufficient compliance

<details>
<summary>Show Answer</summary>
Correct Answer: B) They may need to retrain models after removing specific individual's data, or use techniques like machine unlearning

**Explanation:**
The right to erasure under GDPR can require removing an individual's influence from trained models, potentially necessitating model retraining or machine unlearning techniques. It's not impossible to comply, but it requires careful planning. GDPR does apply to ML systems processing personal data. Deleting source files doesn't remove learned patterns from model weights.
</details>

---

**Question 116**

A company wants to log and monitor all interactions with their Amazon Bedrock application for compliance and security analysis. Which approach provides comprehensive logging of model invocations including prompts and responses?

A) Checking the model's training logs
B) Only monitoring CPU utilization of the service
C) Relying solely on AWS billing reports
D) Amazon Bedrock model invocation logging to S3 and CloudWatch Logs

<details>
<summary>Show Answer</summary>
Correct Answer: D) Amazon Bedrock model invocation logging to S3 and CloudWatch Logs

**Explanation:**
Bedrock model invocation logging captures full request and response data (including prompts and completions) and sends them to S3 and/or CloudWatch Logs for compliance auditing. CPU utilization is an infrastructure metric. Billing reports show costs, not content. Training logs are from model development, not runtime invocations.
</details>

---

**Question 117**

A security architect is designing the network architecture for their SageMaker deployment. They need to ensure that training instances can download packages from the internet for dependencies while keeping the model endpoint completely isolated. Which architecture achieves this?

A) Use a VPC with NAT Gateway for training instances' internet access and VPC endpoints for endpoint isolation
B) Place all resources in public subnets with unrestricted security groups
C) Disable all networking for both training and endpoints
D) Use the same security group for all resources with all ports open

<details>
<summary>Show Answer</summary>
Correct Answer: A) Use a VPC with NAT Gateway for training instances' internet access and VPC endpoints for endpoint isolation

**Explanation:**
A NAT Gateway allows training instances in private subnets to access the internet for dependencies without being directly accessible. VPC endpoints keep inference traffic private. Public subnets with open security groups expose everything. Disabling networking prevents all operations. Open security groups violate least-privilege principles.
</details>

---

**Question 118**

A company has multiple AWS accounts and wants to centrally manage which foundation models their teams can access through Amazon Bedrock. Which approach provides centralized governance across accounts?

A) AWS Organizations with Service Control Policies (SCPs) restricting Bedrock model access
B) Letting each team manage their own permissions independently
C) Using a single shared AWS account for all teams
D) Disabling IAM entirely and using only root credentials

<details>
<summary>Show Answer</summary>
Correct Answer: A) AWS Organizations with Service Control Policies (SCPs) restricting Bedrock model access

**Explanation:**
AWS Organizations with SCPs provides centralized governance by defining permission boundaries across all member accounts, allowing administrators to restrict which Bedrock models can be accessed organization-wide. Independent management lacks central control. A single shared account creates security risks. Disabling IAM or using root credentials violates security best practices.
</details>

---

**Question 119**

A development team is using Amazon Bedrock in production and wants to be alerted when the model's response patterns change significantly or when unusual usage patterns emerge that might indicate a security breach. Which monitoring approach is MOST appropriate?

A) Checking logs manually once per year
B) Relying on end users to report issues
C) Only monitoring the monthly AWS bill
D) Setting up Amazon CloudWatch alarms on Bedrock metrics combined with CloudTrail anomaly detection

<details>
<summary>Show Answer</summary>
Correct Answer: D) Setting up Amazon CloudWatch alarms on Bedrock metrics combined with CloudTrail anomaly detection

**Explanation:**
CloudWatch alarms can trigger on Bedrock operational metrics (invocation counts, latency, errors) while CloudTrail monitors for unusual API call patterns indicating potential security issues. Manual yearly checks miss real-time threats. Bill monitoring is too delayed for security. Relying on users misses backend attacks.
</details>

---

**Question 120**

A company is building an AI application that processes customer data from multiple countries. Their compliance team requires that they can demonstrate exactly what data was used to train or fine-tune their models, how it was processed, and where it is stored at any point in time. Which combination of AWS capabilities supports this data governance requirement? (Select TWO)

A) Amazon S3 versioning and object lock for immutable training data records
B) Deleting all logs after model training completes
C) SageMaker ML Lineage Tracking for end-to-end data and model provenance
D) Using untagged resources without any naming conventions
E) Disabling AWS CloudTrail to reduce storage costs

<details>
<summary>Show Answer</summary>
Correct Answers: A) Amazon S3 versioning and object lock for immutable training data records and C) SageMaker ML Lineage Tracking for end-to-end data and model provenance

**Explanation:**
S3 versioning with object lock creates immutable records of training data at each point in time. SageMaker ML Lineage Tracking automatically records the relationships between datasets, processing steps, training jobs, and models for full provenance. Deleting logs destroys audit evidence. Untagged resources make tracking impossible. Disabling CloudTrail eliminates API audit trails.
</details>

