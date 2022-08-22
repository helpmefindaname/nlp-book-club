# Block Pruning For Faster Transformers

[Paper link](https://arxiv.org/abs/2109.04838)
[Github page](https://github.com/huggingface/nn_pruning)


## Introduction / General
* What is the difference between distillation, (unstructured) pruning and structured pruning? What is the purpose for each approach? 
* What category does Block Pruning fall into? 

## Related work / Background
* What are shortcomings of previous unstructured pruning techniques? 
* What are score-based and movement pruning approaches?

## Model
* When is the block movement pruning technique applied (i.e. during pre-training, fine-tuning or post fine-tuning) and how is it accomplished? 
* What is the dimension of a block and of the score matrix?
* What are the tradeoffs wrt. block size? 

## Experimental Setup & Experiments

* What were the main differences in the experiments / what are the main learnings?
* What is the ratio of linear layer parameters to transformer layer parameters for the BERT model? 
* What is the main hyperparameter?
* How is it possible that Block Pruning does not fully remove a component such as an attention head, even if the the block size on attention heads is chosen to be equal to the head size? 
* What is the difference between the Struct and Hybrid Filled pruning method? 
* How does a Hybrid-pruned BERT-large on SQuAD v1.1 perform compared to a BERT-base model? 
* What can be said in general about pruning effectiveness wrt. original model size? 
* Explain one of the findings of the ablation study.
* Checkout the number of parameters vs. speedup times (for example on the github page: https://github.com/huggingface/nn_pruning or in Table 4), (how) do they correlate? 


## Final part

* What do you think of the paper?
* What references sound interesting to you?
* How many stars does their Github repo have?
