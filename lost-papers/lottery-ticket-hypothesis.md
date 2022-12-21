# The Lottery Ticket Hypothesis for Pre-trained BERT Networks

[Paper link](https://arxiv.org/pdf/2007.12223.pdf)
[Github link](https://github.com/VITA-Group/BERT-Tickets)

## Preliminaries/Refreshers 

* How does Pruning work? What is the difference between structured pruning and unstructured pruning? 
* What is Iterative Movement Pruning?
* What is Magnitude block Pruning?
* What does "over-parameterization" mean in terms of deep learning?
* How many parameters do Bert-base and Bert-large have?
* What is the GLUE benchmark?   

# Introduction

* What is the Lottery Ticket Hypothesis? Why is it interesting?
* What questions arise with Lottery Tickets in terms of Transfer learning?
* What findings are presented in this paper?

## Definitions

* What does the term "Network" refer to?
* What is a subnetwork? When is a Subnetwork considered to be Matching?
* What is a **Winning Ticket**? How does it differ from a matching subnetwork?
* What is a **universal subnetwork**?

## The Existence of Matching Subnetworks in BERT

* What are the 4 claims the Authors evaluate from prior work?
* Are there winning tickets? Looking at **Table 2** which sparsities could be achieved?
* Are IMP winning tickets sparser than randomly pruned or initialized subnetworks? Looking at **Table 2** what drops of accuracy are reached? What do randomly
shuffled pre-trained weights refer to?
* Does rewinding improve performance? What does rewinding mean? Looking at **Table 3** How does the rewinding percentage affect accuracies?
* Do IMP subnetworks match the performance of standard pruning? 

## Transfer Learning for BERT Winning Tickets

* What are the new research questions in this paper?
* Are winning tickets for a source task *S* also winning tickets for other target tasks *T*? Looking at **Figure 3** which task is clearly the best?
* Are there patterns in subnetwork transferability?
* Does initializing to pretrained weights lead to better transfer? Looking at **Figure 4** how does the Rewind percentage impact the transferability?

## Conclusions, Implications and final thoughts

* What is the main contribution of this paper?
* What do you think of the paper?
* What references sound interesting to you?
* How many stars does their Github repo have?
* Did they publish the models the trained?