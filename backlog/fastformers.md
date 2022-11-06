# FastFormers: Highly Efficient Transformer Models
for Natural Language Understanding

[Paper link](https://arxiv.org/pdf/2010.13382.pdf)
[Github link](https://github.com/microsoft/fastformers)


## Preliminaries/Refreshers 

* How long does the prediction of the sentence "I like you. I love you" take on your computer (cpu) (and if possible gpu) for the following models:
  * [distilbert-base-uncased-finetuned-sst-2-english](distilbert-base-uncased-finetuned-sst-2-english)
  * [doyoungkim/bert-base-uncased-finetuned-sst2](https://huggingface.co/doyoungkim/bert-base-uncased-finetuned-sst2)
  * [siebert/sentiment-roberta-large-english](https://huggingface.co/siebert/sentiment-roberta-large-english)
* What Metrics besides the task-performance exist and why are they important to look at too?
* What is Quantization, Pruning and Knowledge Distillation?

## Introduction

* What are the 3 methods that are mainly utilized?
* What package is utilized for graph fusion?
* How is the energy efficency computed?

## Knowledge distillation

* What is the difference between task-specific and task-agnostic distillation?
* What teacher models are used?
* What student models are used for task-specific distillation?
* Why are results bad if the parent and the teacher have different model types?

## Structured Pruning

* Why is Structured Pruning used and not unstructured Pruning?
* What strategies are used for Structured Pruning?
* What are the MultiRC and ReCoRD tasks?
* What gains could be achieved?

## Low Precision Inference

* Why are 8bit quantized matrix multiplications on the CPU so much faster than 32-bit floats? How big is the speedup?
* Why is the GPU using 16 bit-flaots instead of 8-bit? What speedup could be achieved?

## Runtime Optimization

* How does Multi-processing optimization work?
* Looking at **Table 2** Which setup achieves the best speedup?
* How is the Computational graph optimized?

## Results
* What are dynamic sequence lengths?
* Looking at **Table 3** what brings the biggest speed-up?
* How would you assume the implementation cost of the methods of **Table 3**?
* Looking at **Table 4** How do the Speed ups and Engergy Savings look for the Systems provided?

## Conclusions, Implications and final thoughts

* What do you think of the paper?
* What references sound interesting to you?
* How many stars does their Github repo have?
* What is the sustainlp conference?
* How can [experiment impact tracker](https://github.com/Breakend/experiment-impact-tracker) be used for work?