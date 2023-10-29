# Efficient Streaming Language Models with Attention Sinks

[Paper link](https://arxiv.org/abs/2309.17453)
[Github link](https://github.com/mit-han-lab/streaming-llm)

## Preliminaries/Refreshers

* What are LLMs using Transformers?
* What LLMs do you have experience with?
* What is the problem with the quadratic Complexity?

## Introduction

* What is the issue with infinite-length inputs?
* What approaches exist for handling infinite-length inputs as shown in **Figure 1**?
* What insight is presented in **Figure 2** to explain why previous attempts didn't work out so great? 

## Related Work

* What is the concept of *Length extrapoation*?
* What is the concept of *Context Window Extension*?
* How is the utilization of Long Text in LLMs improved?
* In which of the 3 categories does *StreamingLLM* fall into?

## StreamingLLM

* Looking at **Figure 3** when does the perplexity explode for different types of attention?
* Why do LLMs break when removing the initial token?
    * Which 2 possibilities are explained by the authors?
    * Looking at **Table 1** which explanation is more likely? 
* What is the concept of an Attention Sink?
* How does the Rolling KV Cache with Attention Sinks work?
* How are the position ids handled for relative distances?
* What is approached to pre-train LLMs to be aware of an *Attention Sink*?
* What is the "Zero Sink"?
* Looking at **Table 3** how do the 3 methods perform on a 160m LM?

## Experiments

* What LLMs are used for experiments?
* What is the experiment setup for Long texts?
* Looking at **Figure 3** and **Figure 5** what are the results of the experiment?
* What are the results of pretraining with a sink token?
* What are the results on QA with Instruction-tuned models with sink tokens?
* How does StreamingLLM impact the performance and memory?

## Discussion

* What do you think of StreamingLLM?
* Can you think of similar uses for other transformer models?
* How manny stars does their github repo have?
* What references do you find most interesting?
