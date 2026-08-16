# Beginner Training: Neural Networks

**For:** AWS Certified AI Practitioner (AIF-C01) preparation  
**Time:** about 20–30 minutes  
**Goal:** explain what neural networks are, how they learn, when to use them, and the high-level AWS context—without requiring advanced math or coding.

> Exam focus: AIF-C01 is a foundational exam. You should understand AI/ML concepts and choose appropriate use cases; AWS states that developing algorithms, hyperparameter tuning, and mathematical analysis are out of scope. [AWS exam guide](https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01.html)

## 1. What is a neural network?

A **neural network** is a machine-learning model that learns patterns from examples. It is made from connected units called **neurons** (or nodes), organized in layers.

It is loosely inspired by biological brains, but it is not a simulation of one. Think of it as a flexible pattern-recognition system.

### Simple example

Suppose we want to recognize whether a photo contains a dog. During training, the model sees many images labeled **dog** or **not dog**. It gradually learns visual patterns—such as shapes, textures, and combinations of features—that help it make a prediction for a new image.

## 2. The basic structure

```text
Input layer        Hidden layer(s)          Output layer

Image pixels  →   detect patterns      →   “dog”: 92%
                    combine patterns   →   “not dog”: 8%
```

- **Input layer:** receives data, such as image pixels, audio values, or words converted into numbers.
- **Hidden layers:** transform the input and learn increasingly useful patterns.
- **Output layer:** produces the prediction, such as a category, number, or probability.

A neural network with multiple hidden layers is commonly called a **deep neural network**. The field built around such networks is **deep learning**.

## 3. How does it learn?

Neural-network learning can be understood as a repeatable loop:

1. **Start with an example.** Give the network an input, such as a labeled photo.
2. **Make a prediction.** The network produces an initial answer.
3. **Measure the error.** Compare the prediction with the known correct answer.
4. **Adjust connections.** Slightly change internal values called **weights** to reduce future error.
5. **Repeat many times.** More examples and repetitions usually help the network recognize useful patterns.

The model does not memorize a simple rule written by a person. It adjusts its weights based on data to learn a mapping from inputs to outputs.

### Terms worth recognizing

| Term | Plain-language meaning |
| --- | --- |
| **Weight** | A number that controls how strongly one connection influences the next layer |
| **Activation function** | A rule that helps a neuron decide how much signal to pass onward |
| **Loss function** | A measure of how wrong the model’s prediction is |
| **Training** | Adjusting weights using training examples |
| **Inference** | Using a trained model to make a prediction on new data |
| **Epoch** | One full pass through the training dataset |

You do not need to calculate these values for the AI Practitioner exam, but you should understand their role.

## 4. Training versus inference

| Stage | What happens | Example |
| --- | --- | --- |
| **Training** | The model learns by adjusting weights using data and feedback | Teaching a photo model from labeled images |
| **Inference** | The trained model applies what it learned to new input | Identifying an object in a customer’s new photo |

Training can require substantial data and compute. Inference is the normal production activity: an application sends input to an already-trained model and receives a result.

## 5. Common neural-network use cases

Neural networks are especially useful when data is complex and unstructured.

| Data type | Example task |
| --- | --- |
| Images and video | Image classification, object detection, face comparison |
| Text | Translation, summarization, sentiment analysis, chat assistants |
| Audio | Speech recognition, speaker analysis |
| Time-series data | Demand forecasting, anomaly detection |
| Generative AI | Creating text, images, code, or audio from a prompt |

For simpler, structured problems—such as predicting a value from a small spreadsheet—other ML methods may be easier to train, explain, and operate.

## 6. Neural networks and generative AI

Many modern **foundation models** are very large neural networks trained on broad datasets. They learn patterns in text, images, code, or other data, then can be adapted or prompted for many tasks.

For example, a large language model predicts likely next tokens (small pieces of text). Repeating that prediction produces a response. This is why a model can generate fluent text, but it can also produce an answer that sounds plausible without being correct—a behavior often called a **hallucination**.

For exam questions, distinguish these ideas:

- A traditional classifier might label an image as “invoice” or “receipt.”
- A generative model can draft a summary of the invoice or answer questions about it.
- Neither result should be trusted blindly in a high-impact workflow; use validation, human review where appropriate, and responsible-AI practices.

## 7. Strengths and limitations

| Strengths | Limitations and risks |
| --- | --- |
| Learns complex, nonlinear patterns | Often needs lots of representative data |
| Works well with images, language, and audio | Can be costly to train or run |
| Can improve with additional quality data | Can reflect bias present in training data |
| Supports many generative-AI capabilities | May be difficult to explain in detail |
| Can automate repetitive prediction tasks | Can overfit: perform well on training data but poorly on new data |

### Two important quality concepts

- **Overfitting:** the model learns training examples too specifically and does not generalize well to new data.
- **Bias:** unfair or unrepresentative data can lead to uneven outcomes across groups or situations.

Good practice includes using representative data, separating training and test data, evaluating model quality, monitoring production behavior, and keeping humans involved when errors could cause meaningful harm.

## 8. AWS context for the exam

At a high level, AWS offers several ways to use AI and ML:

| Need | AWS approach |
| --- | --- |
| Add common AI capabilities without building a custom model | Use AWS AI services, such as Amazon Textract for document text and data extraction or Amazon Comprehend for NLP insights |
| Build, train, or deploy custom ML models | Use Amazon SageMaker AI |
| Build generative-AI applications with foundation models | Use Amazon Bedrock |

AWS describes Amazon SageMaker AI as a service for building, training, and deploying ML models, while Amazon Bedrock provides access to foundation models for generative-AI solutions. [AWS ML service decision guide](https://docs.aws.amazon.com/decision-guides/latest/machine-learning-on-aws-how-to-choose/guide.html)

For AIF-C01, focus on selecting the right high-level service or approach for a business problem—not on implementing the neural network yourself.

## 9. Exam-style practice

### Question 1

A company wants a model to identify damaged products in photos. It has thousands of photos labeled “damaged” and “not damaged.” Which description is most accurate?

**Answer:** This is supervised learning. A neural network may be suitable because the input is image data and labeled examples are available.

### Question 2

Which statement best distinguishes training from inference?

A. Training sends a prediction to an application; inference adjusts weights.  
B. Training adjusts a model using examples; inference applies the trained model to new input.  
C. Training only works with text; inference only works with images.  
D. They are two names for the same process.

**Answer: B.**

### Question 3

A team needs a chatbot that can summarize support tickets. Which approach is most relevant?

**Answer:** A generative-AI solution using a foundation model, which is typically a large neural network. Amazon Bedrock is an AWS service to consider.

### Question 4

A model performs extremely well on its training images but poorly on photos submitted by real customers. What is a likely issue?

**Answer:** Overfitting, a mismatch between training data and real-world data, or both.

### Question 5

Why should a team evaluate model results across realistic conditions and groups?

**Answer:** To identify weak performance, bias, and data gaps before those problems affect users.

## 10. Quick self-check

Complete these sentences:

1. A neural network learns by adjusting its ______ based on prediction error.  
2. Using a trained model on a new customer input is called ______.  
3. A model that memorizes training data but struggles with new data may be ______.  
4. A large neural network trained broadly for many generative-AI tasks is often a ______ model.

**Answers:** 1. weights; 2. inference; 3. overfitting; 4. foundation.

## Takeaway

Neural networks are layered ML models that learn complex patterns from data. For the AWS AI Practitioner exam, be ready to explain their basic learning loop, identify suitable use cases, distinguish training from inference, recognize limitations such as overfitting and bias, and connect business needs to the appropriate AWS AI/ML approach.

