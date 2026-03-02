

# OVERALL ROADMAP (FROM ZERO → GPT)

We divide learning into 6 stages.

---

# STAGE 1 — Pure Python + Math Thinking

Goal: Understand what a model actually is.

You create:

```
01_linear_model/
    main.py
```

You will learn:

* Variables
* Functions
* Loops
* Basic math
* What is a parameter
* What is prediction

You will manually create:

```
y = wx + b
```

Just math.

---

#  STAGE 2 — Build First Neural Network From Scratch (No PyTorch)

You create:

```
02_neural_network_from_scratch/
    main.py
```

You implement:

* Weights
* Forward pass
* Loss calculation
* Manual gradient update

Using only:

* Python
* Numpy

You learn:

* What is forward pass
* What is loss
* What is gradient
* What is optimization

This is critical.

---

# STAGE 3 — Use PyTorch for Simple Character Learning

Now introduce PyTorch.

Folder:

```
03_char_prediction/
    train.py
```

You train:

a → b
b → c
c → d

You understand:

* Tensors
* Embedding
* CrossEntropyLoss
* Backpropagation
* GPU usage

Now you understand “training”.

---

# STAGE 4 — Sequence Learning

Now instead of:

a → b

We train:

h e l l o → next letter

You learn:

* Sliding window
* Context
* Sequence prediction
* Why RNN was invented

You build:

Simple RNN text predictor.

Folder:

```
04_rnn_text_model/
```

Now you understand sequence modeling.

---

# STAGE 5 — Attention Mechanism

Now you learn:

Why RNN fails on long sentences.

You implement:

* Simple self-attention manually
* Dot product attention
* Attention weights visualization

Folder:

```
05_attention_from_scratch/
```

Now you understand the heart of transformers.

---

# STAGE 6 — Build Mini GPT

Now you combine:

* Embedding
* Positional encoding
* Multi-head attention
* Feed forward network
* Layer normalization

Now you build:

```
06_mini_gpt/
```

And you actually understand every line.

---