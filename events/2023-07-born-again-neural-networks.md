# Born-Again Neural Networks

[Paper link](https://arxiv.org/pdf/1805.04770.pdf)


## Preliminaries/Refreshers 

* What is knowledge Distillation?
* What are the usual application of knowledge Distillation?

## Introduction

* What variation of Knowledge Distillation is proposed? How does it differ from the usual compression KD?
* What is the *dark knowledge* term?
* What is the second term?
* What is meant by "weak masters can still improve performance of students"?

## Born Again Networks

* What is the goal of Born Again Networks?
* What is the Sequence of Teaching Selves Born-Again Networks Ensemble?
* What does Hinton suggest as the reason, why Knowledge distillation works?
* How does the knowledge distillation affect the gradients?
* Which two experiments are conducted to test if the success of dark knowledge is performing importance weighting?
* How do they test BANs stability for Variations on Computer vision applications?


## Experiments

* What resnet based experiments are run?
* How is BAN without Dark Knowledge tested?
* How are variations of Resnet tested?
* How are language models tested on the Penn tree Bank corpus?


## Results

* Looking at **Table 1** what is the impact of BAN for ResNets with the same architecture on CIFAR-10?
* Looking at **Table 2**:
  * how does only using the teacher prediction (BAN) compare to using the teacher predictions + the labels (BAN+L)?
  * would you assume that knowledge distillation is only performing importance weighting?
  * what is the difference between *BAN* and *BAN-1*?
  * how do the predictions change by using ensembles?
* Looking at **Table 3** how does using a Wide or Dense Resnets differ when using a Wide teacher?
* Looking at **Table 6** how does BAN work for language modeling?


## Conclusions, Implications and final thoughts

* What do you think of the paper?
* What references sound interesting to you?
* How many stars does their Github repo have?