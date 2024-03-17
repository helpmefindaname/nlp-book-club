# Making Monolingual Sentence Embeddings Multilingual using Knowledge Distillation

[Paper link](https://aclanthology.org/2020.emnlp-main.365.pdf)
[Github link](https://github.com/UKPLab/sentence-transformers/blob/master/examples/training/multilingual/README.md)
[HF link](https://huggingface.co/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2)

## Preliminaries/Refreshers

* What components of the Transformer is usually used for an embedding model?
* Why are embeddings for sentence-similarity or neural search harder to train than just using unsupervised pretraining?

## Introduction

* What is multilingual knowledge distillation?
* What architecture & pre-trained model is their approach tested on?

## Training

* Looking at **Figure 1** how does the knowledge distillation work?

## Training Data

* What does parallel data refer to?
* What corpuses for parallel data are used?
* Looking at **Table 5** how large is the training data?
* What Bias benchmarks are evaluated? How do they perform?

## Experiments

* What models were choosen as baselines?
* What benchmark is for Multilingual Semantic Textual Similarity used?
* How is the Bitext Retrieval evaluation set up?
* How is the Tatoeba similarity search set up?
* What is the conclusion of the target language training?
* What is meant with Language Bias? What is proposed to have little language bias?


## Conclusion & Discussion

* What do you think of the Paper?
* Have you tried out the released embeddings somewhere?
* How many stars does their github repo have?
* What references do you find most interesting?