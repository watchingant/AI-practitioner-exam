# Beginner Training: Generative AI Inference Parameters

**Category:** inference-time sampling parameters, also called **decoding** or **generation** parameters.  
**Key examples:** temperature, top-p, top-k, maximum tokens, stop sequences, and repetition penalties.

## Learning goal

Learn what these settings control, how they relate to one another, and how to choose them for common generative-AI tasks. This guide is especially useful for the AWS Certified AI Practitioner exam and Amazon Bedrock concepts.

## 1. Where do temperature and top-p fit?

Large language models generate text one **token** at a time. A token is a small unit of text—often a word, part of a word, punctuation, or whitespace.

At each step, the model assigns probabilities to possible next tokens. For the prompt:

```text
“The capital of France is …”
```

the model might consider:

| Possible next token | Example probability |
| --- | --- |
| Paris | 96% |
| Lyon | 2% |
| Marseille | 1% |
| something else | 1% |

**Inference parameters** control how the model chooses from those possible next tokens and when it stops. They influence the style and bounds of an answer, but they do **not** retrain the model or change its learned knowledge.

```text
Prompt + trained model + inference parameters → generated response
```

## 2. The two main randomness controls

### Temperature

**Temperature** changes how strongly the model favors its most likely next token.

- **Lower temperature:** more predictable and repeatable; favors high-probability tokens.
- **Higher temperature:** more varied and surprising; gives lower-probability tokens more chance.

Example use:

| Task | Typical direction |
| --- | --- |
| Extract a field from a document | Lower temperature |
| Summarize a policy | Lower temperature |
| Draft marketing ideas | Higher temperature |
| Brainstorm story concepts | Higher temperature |

A lower temperature does not guarantee that an answer is true; it only makes the model’s selection process less random.

### Top-p (nucleus sampling)

**Top-p** limits the candidate tokens to the smallest group whose combined probability reaches a chosen threshold. It is also called **nucleus sampling**.

Suppose the candidates have these probabilities:

| Token | Probability | Running total |
| --- | ---: | ---: |
| horses | 70% | 70% |
| zebras | 20% | 90% |
| unicorns | 10% | 100% |

- With **top-p = 0.70**, only `horses` is considered.
- With **top-p = 0.90**, `horses` and `zebras` are considered.
- With **top-p = 1.00**, all candidates remain available.

So a **lower top-p** narrows the options to more likely tokens; a **higher top-p** allows a broader range of possible tokens.

## 3. Temperature versus top-p

Both settings influence randomness and diversity, but they work differently:

| Parameter | What it changes | Lower value | Higher value |
| --- | --- | --- | --- |
| **Temperature** | The relative probabilities among choices | More strongly favors likely choices | Makes lower-probability choices more competitive |
| **Top-p** | Which cumulative-probability group is eligible | Keeps a smaller, highly likely candidate set | Keeps a larger candidate set |

Think of it this way:

- **Temperature** reshapes the odds.
- **Top-p** limits the pool of eligible choices.

### Practical rule

Start by adjusting **one randomness control at a time**. Many providers recommend using temperature or top-p as the primary control, and some models do not let you set both together. For example, certain Claude models on Amazon Bedrock support either `temperature` or `top_p`, but not both in the same request. Always check the selected model’s documentation and allowed ranges.

## 4. Other common inference parameters

### Top-k

**Top-k** keeps exactly the `k` most likely next-token candidates.

- `top-k = 1` means the model considers only the single most likely next token.
- `top-k = 50` means it considers the 50 most likely candidates.

Unlike top-p, top-k uses a fixed number of choices rather than a probability threshold.

### Maximum tokens / response length

**Maximum tokens** sets an upper limit on how many tokens the model can generate.

Use it to:

- keep answers concise;
- control cost and latency;
- prevent unnecessarily long outputs;
- match a requested format.

It is a limit, not a command to produce exactly that many tokens. A model can stop earlier.

### Stop sequences

A **stop sequence** is a character sequence that tells the model to stop generating if it appears.

Example: set `###` as a stop sequence for a response that must end before the next section marker.

Stop sequences help enforce output boundaries. They are not a substitute for clear prompting or output validation.

### Repetition and presence penalties

Some models provide controls that discourage repeated tokens or encourage introducing new topics.

| Control | General purpose |
| --- | --- |
| **Frequency penalty** | Discourages repeatedly using tokens that have already appeared often |
| **Presence penalty** | Discourages returning to concepts that have appeared at all |
| **Repetition penalty** | A model-specific way to reduce repeated output |

Names, meanings, and valid values vary by model. Use these only when repetition is a real observed problem; they can also make answers less focused.

### Seed (when available)

A **seed** initializes the random selection process. With the same model, prompt, settings, and environment, using the same seed may help reproduce an output for testing. It is helpful for experiments, but it is not supported by every model and does not guarantee permanence across model changes.

## 5. Parameter groups at a glance

| Group | Parameters | Main question answered |
| --- | --- | --- |
| **Randomness / diversity** | Temperature, top-p, top-k | How predictable or varied should the wording be? |
| **Length / boundaries** | Maximum tokens, minimum tokens, stop sequences | How long should the answer be and where must it end? |
| **Repetition / novelty** | Frequency, presence, repetition penalties | Should repeated terms or topics be discouraged? |
| **Reproducibility** | Seed | Do I need more repeatable test outputs? |

These are all **inference parameters**: controls applied while generating an answer from a trained foundation model.

## 6. Choosing settings by use case

| Use case | Main goal | Suggested approach |
| --- | --- | --- |
| Retrieval-augmented Q&A (RAG) | Faithful answer based on provided documents | Lower randomness; a practical token limit; cite or validate sources |
| Data extraction | Structured, consistent fields | Lower randomness; strict output format; stop sequence or schema where supported |
| Customer-support draft | Clear and consistent language | Low to moderate randomness; set an appropriate response length |
| Creative writing | Variety and originality | Higher randomness; allow more output length |
| Idea generation | Diverse alternatives | Moderate to higher randomness; request multiple distinct options |
| Classification via prompt | Stable label selection | Lower randomness; constrain the allowed labels and validate output |

### Important caution

Turning randomness down makes wording more consistent, but it does not eliminate hallucinations, bias, prompt-injection risks, or the need for evaluation. Reliability also depends on the prompt, model, context, retrieval quality, safeguards, and human review where appropriate.

## 7. A simple tuning process

1. Define success first: accuracy, format compliance, creativity, brevity, or another measurable outcome.
2. Create a small, representative set of test prompts.
3. Start with the model’s default settings or a low-randomness baseline for factual tasks.
4. Change one parameter at a time.
5. Compare results for quality, consistency, latency, and cost.
6. Select settings based on the task—not on a single impressive example.
7. Re-test when you change models, prompts, data, or model versions.

## 8. Amazon Bedrock context

Amazon Bedrock describes these as **inference parameters**. Its common controls include temperature, top-p, top-k, response length or maximum tokens, and stop sequences. Exact parameters, defaults, and valid ranges vary by foundation model and API.

For the AWS AI Practitioner exam, know the trade-off:

- Choose **lower randomness** for more predictable, repeatable output.
- Choose **higher randomness** when variety and creativity are more valuable.
- Use **maximum tokens** and **stop sequences** to control answer length and boundaries.
- Check each model’s supported controls rather than assuming every setting works identically everywhere.

AWS references: [Inference parameters](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-parameters.html) and [Amazon Bedrock text inference configuration](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_TextInferenceConfig.html).

## 9. Practice questions

### Question 1

A company needs consistent summaries of internal policies. Which direction is most appropriate?

**Answer:** Use a lower temperature (and generally a lower-diversity configuration). This favors more predictable wording, though the team should still evaluate factual accuracy.

### Question 2

What does top-p control?

A. The size of the training dataset  
B. The cumulative-probability pool of candidate next tokens  
C. The number of hidden layers in a neural network  
D. The number of users who can call a model

**Answer: B.**

### Question 3

A team wants to ensure a model response does not continue into a second template section. What control is most relevant?

**Answer:** A stop sequence.

### Question 4

Which statement is true?

A. Higher temperature guarantees more accurate answers.  
B. Lower top-p increases the pool of eligible next tokens.  
C. Maximum tokens limits output length.  
D. Inference parameters retrain the model’s weights.

**Answer: C.**

### Question 5

A developer changes temperature and notices no expected effect. What is a good next check?

**Answer:** Verify that the selected model supports that parameter, confirm the allowed range and request syntax, and check whether another randomness parameter is mutually exclusive.

## Quick self-check

1. Temperature and top-p are both ______-time controls, not training controls.  
2. Top-p is also called ______ sampling.  
3. A lower temperature generally makes output more ______.  
4. A ______ sequence ends generation when the specified text is produced.  
5. Maximum tokens primarily controls response ______.

**Answers:** 1. inference; 2. nucleus; 3. predictable; 4. stop; 5. length.

## Takeaway

Temperature and top-p belong to the **inference-parameter** category. They control how a generative model selects its next tokens: temperature changes the distribution of choices, while top-p limits the candidate pool by cumulative probability. Combine them thoughtfully with length limits and stop sequences, then evaluate the resulting behavior against the actual business task.
