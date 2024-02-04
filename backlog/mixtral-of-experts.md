# Mixtral of Experts

[Paper link](https://arxiv.org/pdf/2401.04088.pdf)
[HF link](https://huggingface.co/mistralai/Mixtral-8x7B-v0.1)

## Preliminaries/Refreshers

* What are LLMs using Transformers?
* What LLMs do you have experience with?
* How do open source-like models compare to closed ones like (Chat-)GPT 3.5 or (Chat-)GPT 4?
* How is the performance of LLMs as they grow in parameters?
* What Organisation is Mistral?

## Introduction

* Based on the name, about how many parameters does Mixtral 8x7B have?
* On a high level, how does their sparse mixture of experts implementation work?
* What are the benefits of using sparse mixture of experts?
* On what data was Mixtral pretrained?
* What models are on pair with Mixtral? How do the models compare in size?
* Besides publishing the weights, what other open source contribution do the authors give?

## Architectural details

* Looking at **Table 1** what are the hyperparameters of Mixtral?
* Looking at **Figure 1** how does a mixture of experts layer work?
* What is the concept to make the Mixture of experts sparse?
* What layer will be replaced by the sparse Mixture of experts?
* What is a SwiGLU block?

## Results

* What tasks and what benchmarks per tasks were used to compare Mixtral and Llama?
* Looking at **Figure 2** and **Table 2** how does Mixtral compare to Llama?
* Looking at **Table 3** how does Mixtral compare to GPT 3.5?
* Looking at **Table 4** how does Mixtral perform on other languages?
* What Bias benchmarks are evaluated? How do they perform?

## Instruction Fine-Tuning

* How were the Instructions Fine-tuned?
* What is Direct Preference Optimization?
* What is the MT-Bench and what is the LMSys benchmark?
a
## Routing analysis

* What layers were selected for analysis?
* What can you tell about the distribution by looking at **Figure 7**?
* How is **Table 5** to understand?
* What does **Figure 8** visualize?


## Conclusion & Discussion

* What do you think of Mixtral?
* Have you tried out Mixtral somewhere?
* Do you know of OOS libraries you can use to run Mixtral?
* What references do you find most interesting?