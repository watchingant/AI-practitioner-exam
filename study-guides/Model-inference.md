

# Beginner's Learning Guide: LLM Generation & Sampling Parameters

## 1. Start With the Big Picture

First understand the distinction between **training** and **inference**.

```text
TRAINING
Data
  ↓
Neural Network
  ↓
Learn parameters
  ↓
Trained LLM


INFERENCE
Prompt
  ↓
Trained LLM
  ↓
Probability distribution
  ↓
Decoding / Sampling
  ↓
Selected token
  ↓
Next token
  ↓
Repeat
  ↓
Generated response
```

**Temperature and top-p primarily affect the last part:** how the model selects tokens during generation.

---

# 2. Learn What an LLM Actually Outputs

This is the most important concept before learning temperature.

Suppose you give an LLM:

> "The sky is"

The model doesn't simply think:

> "The answer is blue."

Instead, it produces probabilities for possible next tokens:

```text
blue      → 0.70
cloudy    → 0.10
gray      → 0.08
falling   → 0.02
green     → 0.01
...
```

The model produces a **probability distribution**.

The generation system then has to decide:

> **Which token should I actually output?**

That's where **decoding and sampling** come in.

---

# 3. Learn Tokens

Before sampling, understand **tokens**.

LLMs don't necessarily process one word at a time.

For example:

```text
"Artificial intelligence"
```

might be represented approximately as:

```text
"Artificial"
" intelligence"
```

while another word might be split into multiple tokens.

The model generates **one token at a time**.

Conceptually:

```text
Prompt
  ↓
Token 1
  ↓
Token 2
  ↓
Token 3
  ↓
Token 4
  ↓
...
```

This is called **autoregressive generation** when each generated token is used as context for predicting the next.

---

# 4. Learn Logits

This is the next level.

Before probabilities are produced, the model generates **logits**.

Very roughly:

```text
Neural network
      ↓
   Logits
      ↓
  Softmax
      ↓
Probabilities
```

For example:

```text
Token       Logit
-----------------
blue         5.2
cloudy       3.1
gray         2.7
green        0.5
```

The logits are converted into probabilities using **softmax**.

You don't need to memorize the mathematics initially, but eventually you should understand:

> **Logits → probability distribution → decoding/sampling → selected token**

---

# 5. Learn Greedy Decoding

The simplest decoding strategy is **greedy decoding**.

The model simply chooses the token with the highest probability.

```text
blue      → 70%  ← SELECT
cloudy    → 10%
gray       → 8%
green      → 1%
```

So:

```text
"The sky is blue"
```

### Advantage

Predictable and simple.

### Disadvantage

It can produce repetitive or less interesting text.

---

# 6. Learn Temperature

Now you're ready for **temperature**.

Temperature controls how **sharp or flat the probability distribution becomes** before sampling.

### Low temperature

Makes the model more conservative.

```text
blue      → 95%
cloudy     → 3%
gray       → 1%
other      → 1%
```

The model strongly favors the most likely answer.

### High temperature

Makes the distribution more spread out.

```text
blue      → 45%
cloudy    → 25%
gray      → 15%
green      → 5%
other     → 10%
```

Less likely tokens become more competitive.

### Intuition

```text
Low temperature
      ↓
More predictable
More deterministic
Less variation


High temperature
      ↓
More random
More diverse
More variation
```

A useful mental model:

> **Temperature controls how willing the model is to consider lower-probability choices.**

---

# 7. Learn Top-p

**Top-p** is also called **nucleus sampling**.

Instead of changing the entire probability distribution, top-p dynamically selects the smallest group of tokens whose combined probability reaches a specified threshold.

Suppose:

```text
Token       Probability
-----------------------
A             0.50
B             0.25
C             0.15
D             0.05
E             0.03
F             0.02
```

If:

```text
top-p = 0.90
```

the system might keep:

```text
A + B + C = 0.90
```

and discard the remaining candidates.

Then sampling occurs among:

```text
A
B
C
```

### Low top-p

Smaller candidate pool:

```text
Top-p = 0.50

A
```

### Higher top-p

Larger candidate pool:

```text
Top-p = 0.90

A
B
C
```

### Intuition

> **Top-p controls how much of the probability distribution is allowed to participate in sampling.**

---

# 8. Temperature vs. Top-p

This distinction is extremely important.

| Parameter       | Controls                                          |
| --------------- | ------------------------------------------------- |
| **Temperature** | How sharply probabilities are distributed         |
| **Top-p**       | How many candidate tokens are considered          |
| **Top-k**       | The maximum number of candidate tokens considered |

Think of it like this:

```text
Temperature
     ↓
"How adventurous should the distribution be?"

Top-p
     ↓
"How much of the probability distribution should I consider?"

Top-k
     ↓
"How many candidate tokens should I consider?"
```

---

# 9. Learn Top-k

**Top-k sampling** keeps only the `k` most probable tokens.

Example:

```text
Token       Probability
-----------------------
A             0.50
B             0.25
C             0.15
D             0.05
E             0.03
F             0.02
```

With:

```text
top-k = 3
```

only:

```text
A
B
C
```

are considered.

Unlike top-p, the number of candidates is fixed.

```text
Top-k = fixed number of tokens
Top-p = probability-based number of tokens
```

---

# 10. Learn Deterministic vs. Stochastic Generation

This is another fundamental concept.

### Deterministic

Given the same prompt and settings, you generally get the same output.

Example:

```text
Greedy decoding
```

### Stochastic

The model samples from probabilities, so multiple outputs are possible.

```text
Prompt
  ↓
Probability distribution
  ↓
Random sampling
  ↓
Output A

Same prompt
  ↓
Probability distribution
  ↓
Random sampling
  ↓
Output B
```

This is why you can sometimes ask the same model the same question and get different wording.

---

# 11. Learn Random Seeds

A **random seed** controls the starting point of a pseudo-random number generator.

If an API exposes a seed, using the same:

```text
Prompt
+
Model
+
Parameters
+
Seed
```

can make generation more reproducible.

Conceptually:

```text
Same prompt
+
Same settings
+
Same seed
        ↓
More reproducible output
```

However, exact reproducibility can depend on the model, provider, infrastructure, and other implementation details.

---

# 12. Learn Max Tokens / Max Output Tokens

This parameter controls how much output the model can generate.

For example:

```text
max output tokens = 100
```

means the model can generate up to approximately 100 tokens.

Important distinction:

```text
Input tokens
+
Output tokens
=
Context / usage
```

Different APIs use different names and limits, so always check the particular model's documentation.

---

# 13. Learn Stop Sequences

A **stop sequence** tells the generation system:

> "Stop generating when you reach this sequence."

For example:

```text
stop = "\n\n"
```

The model may stop when it generates that sequence.

This can be useful when generating structured content.

Example:

```text
Question
Answer
```

You might configure generation to stop after the answer reaches a particular delimiter.

---

# 14. Learn Frequency and Presence Penalties

These parameters appear in some LLM APIs.

### Frequency penalty

Penalizes tokens based on how frequently they have already appeared.

Intuition:

> "Don't keep repeating the same words."

### Presence penalty

Penalizes tokens simply because they have already appeared.

Intuition:

> "Encourage the model to introduce new vocabulary/topics."

These are related but not identical.

```text
Frequency penalty
       ↓
How often has this appeared?

Presence penalty
       ↓
Has this appeared at all?
```

Not every model/provider exposes these controls, and their exact behavior can vary.

---

# 15. Learn Repetition

One reason sampling parameters matter is **repetition**.

A model can sometimes produce:

```text
The answer is...
The answer is...
The answer is...
The answer is...
```

Generation controls can influence this behavior.

But don't assume:

> "Higher temperature = less repetition."

That's not universally true.

Generation behavior depends on the model, decoding strategy, prompt, and other parameters.

---

# 16. Learn the Concept of Entropy

Once you're comfortable with probability distributions, learn **entropy**.

Entropy measures uncertainty in a probability distribution.

Imagine:

### Very certain

```text
A = 99%
B = 1%
```

Low entropy.

### Very uncertain

```text
A = 25%
B = 25%
C = 25%
D = 25%
```

Higher entropy.

Temperature changes the distribution's sharpness and therefore affects its entropy.

This gives you a deeper mathematical understanding of why temperature changes generation behavior.

---

# 17. Learn Softmax

To really understand temperature, learn the **softmax function**.

A simplified form is:

$$
P_i = \frac{e^{z_i/T}}{\sum_j e^{z_j/T}}
$$

Where:

* (z_i) = logit for token (i)
* (T) = temperature
* (P_i) = resulting probability

### When T is low

The differences between logits become more pronounced.

```text
High confidence in top choices
```

### When T is high

The distribution becomes flatter.

```text
More probability spread across choices
```

This is the mathematical foundation behind temperature.

---

# 18. Learn the Full Generation Pipeline

At this point, you can put everything together:

```text
                    Prompt
                      ↓
                   Tokenize
                      ↓
                Input Tokens
                      ↓
                  LLM Model
                      ↓
                    Logits
                      ↓
               Temperature
                      ↓
                Probabilities
                      ↓
             Top-k / Top-p
                      ↓
                  Sampling
                      ↓
              Selected Token
                      ↓
        Add token to the context
                      ↓
               Predict next token
                      ↓
                   Repeat
                      ↓
                Final Output
```

This is the core conceptual pipeline you want to understand.

---

# 19. Learn Decoding Strategies

Now broaden your knowledge beyond temperature and top-p.

Study these:

### Greedy decoding

```text
Choose highest probability token
```

### Beam search

Maintains multiple candidate sequences and searches for a high-probability sequence.

Common in some sequence-generation tasks, though less central to modern conversational LLM sampling.

### Temperature sampling

Samples according to a temperature-adjusted probability distribution.

### Top-k sampling

Restricts sampling to the top `k` tokens.

### Top-p / nucleus sampling

Restricts sampling to the smallest probability mass whose cumulative probability reaches `p`.

---

# 20. Understand That These Parameters Are Not "Intelligence Controls"

This is an important misconception to avoid.

Increasing temperature does **not** make the model:

* smarter
* more knowledgeable
* better at reasoning
* more intelligent

It primarily changes **how the model samples from its learned probability distribution**.

Think:

```text
Model knowledge
       ≠
Sampling behavior
```

Temperature changes the latter.

---

# 21. Understand Why Settings Depend on the Task

Different tasks may benefit from different generation behavior.

### Deterministic extraction

You might want:

```text
Low randomness
```

Example:

```text
Extract:
Name
Date
Invoice number
```

You want consistent results.

### Creative writing

You may want:

```text
More variation
```

### Brainstorming

You may want:

```text
More diverse possibilities
```

### Structured output

You generally want:

```text
Predictability + constraint
```

The best settings depend on the task and the model.

---

# 22. A Beginner Experiment

You can learn this much faster by experimenting.

Use the same prompt repeatedly:

> "Give me five creative names for a coffee shop."

Try:

```text
Temperature = low
Top-p = high/default
```

Then:

```text
Temperature = medium
Top-p = high/default
```

Then:

```text
Temperature = high
Top-p = high/default
```

Compare the outputs.

Then experiment with top-p while keeping temperature fixed.

Record:

```text
Prompt
Temperature
Top-p
Output
```

You'll start to develop an intuition for the parameters.

---

# 23. Recommended Learning Order

Don't try to learn all of this at once.

Follow this progression:

```text
LEVEL 1 — Fundamentals
        ↓
Tokens
Logits
Probabilities
Next-token prediction
        ↓

LEVEL 2 — Basic Decoding
        ↓
Greedy decoding
Sampling
Deterministic vs stochastic generation
        ↓

LEVEL 3 — Core Parameters
        ↓
Temperature
Top-k
Top-p
        ↓

LEVEL 4 — Generation Controls
        ↓
Max output tokens
Stop sequences
Seeds
Frequency penalties
Presence penalties
        ↓

LEVEL 5 — Mathematics
        ↓
Softmax
Temperature equation
Probability distributions
Entropy
        ↓

LEVEL 6 — Advanced Decoding
        ↓
Beam search
Nucleus sampling
Contrastive decoding
Speculative decoding
Constrained decoding
        ↓

LEVEL 7 — Production LLMs
        ↓
Prompt + sampling configuration
Structured output
Latency
Cost
Reproducibility
Evaluation
Safety
```

---

# 24. The Core Vocabulary

You should eventually be comfortable with these terms:

| Term                         | Meaning                                               |
| ---------------------------- | ----------------------------------------------------- |
| **Token**                    | Basic unit of text processed/generated by an LLM      |
| **Logit**                    | Raw score assigned to a possible next token           |
| **Probability**              | Model's estimated likelihood of a token               |
| **Softmax**                  | Converts logits into a probability distribution       |
| **Sampling**                 | Selecting a token according to probabilities          |
| **Decoding**                 | Process of converting model probabilities into output |
| **Temperature**              | Controls probability distribution sharpness           |
| **Top-k**                    | Limits sampling to the k most probable tokens         |
| **Top-p**                    | Limits sampling to a probability mass p               |
| **Nucleus sampling**         | Another name for top-p sampling                       |
| **Greedy decoding**          | Always selects the highest-probability token          |
| **Beam search**              | Searches multiple candidate sequences                 |
| **Seed**                     | Controls pseudo-random sampling for reproducibility   |
| **Max output tokens**        | Limits generated output length                        |
| **Stop sequence**            | Tells generation when to stop                         |
| **Frequency penalty**        | Penalizes repeated tokens based on frequency          |
| **Presence penalty**         | Penalizes tokens that have already appeared           |
| **Entropy**                  | Measures uncertainty in a probability distribution    |
| **Deterministic generation** | Same conditions produce the same/similar output       |
| **Stochastic generation**    | Random sampling can produce different outputs         |

---

# 25. The Mental Model to Remember

If you remember only one diagram, remember this:

```text
                   LLM
                    ↓
              "What's next?"
                    ↓
                  Logits
                    ↓
              Probability
              Distribution
                    ↓
          +---------+---------+
          |                   |
     Temperature          Top-p / Top-k
          |                   |
          +---------+---------+
                    ↓
                 Sampling
                    ↓
              Selected Token
                    ↓
             "What's next?"
                    ↓
                  Repeat
                    ↓
              Final Response
```

And remember the distinction:

```text
TEMPERATURE
"What does the probability distribution
look like?"

TOP-P
"How much of the probability distribution
do I allow into the candidate pool?"

TOP-K
"How many of the highest-probability tokens
do I allow?"
```

---

# 26. Your Learning Roadmap

If your goal is to become comfortable with LLMs, I'd study this category in this order:

### Beginner

* [ ] What is an LLM?
* [ ] What is a token?
* [ ] How does next-token prediction work?
* [ ] What are logits?
* [ ] What are probabilities?
* [ ] What is sampling?
* [ ] What is decoding?

### Core Sampling

* [ ] Temperature
* [ ] Top-k
* [ ] Top-p
* [ ] Greedy decoding
* [ ] Deterministic vs. stochastic generation
* [ ] Random seeds

### Generation Controls

* [ ] Max output tokens
* [ ] Stop sequences
* [ ] Frequency penalties
* [ ] Presence penalties

### Mathematics

* [ ] Softmax
* [ ] Probability distributions
* [ ] Entropy
* [ ] Temperature mathematically
* [ ] Cumulative probability

### Advanced

* [ ] Beam search
* [ ] Nucleus sampling
* [ ] Constrained decoding
* [ ] Contrastive decoding
* [ ] Speculative decoding

### Production

* [ ] Choosing parameters for different tasks
* [ ] Reproducibility
* [ ] Latency
* [ ] Token costs
* [ ] Evaluation
* [ ] Structured generation
* [ ] Model-specific parameter behavior

---

## Final Takeaway

**Temperature and top-p are not types of AI models.**

They are **inference-time generation/sampling parameters** that influence how a trained model selects its next token.

The most important conceptual chain is:

> **Prompt → Tokens → Model → Logits → Probabilities → Sampling/Decoding → Next Token → Repeat**

Once you understand that pipeline, **temperature, top-p, top-k, greedy decoding, seeds, and the other generation parameters become much easier to understand.**

