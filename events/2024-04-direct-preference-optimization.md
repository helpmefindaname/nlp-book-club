# Direct Preference Optimization: Your Language Model is Secretly a Reward Model

[Paper link](https://arxiv.org/pdf/2305.18290.pdf)

## Preliminaries/Refreshers

* What is the concept of Reinforcement Learning with Human Feedback?
* Why is it important to LLMs to be "Instruction Tuned"?
* How does Reinforcement Learning work on a high level?
* Why is Reinforcement Learning considered hard?

## Introduction & Preliminaries

* What property is important to have in a AI-System trained on the Internet according to the Authors? 
* How does the Reward Modelling Phase work?
* How does the RL Fine-Tuning Phase work?

## Direct Preference Optimization

* How does **Equation 4** relate to **Equation 3**?
* Why is the normalization constant $Z(x)$ still in existing in **Equation 5** but not in **Equation 6**?
* Looking at **Equation 7** how does the training work?
* Looking ath the Gradient, what does DPO essentially do?
* How is the reference model initialized?
* Why is it not necessary to fit a explicit reward model?


## Theoretical Analysis
* Why are language models secretly also reward models?
* What was said on the instability of Actor-Critic Algorithms?

## Experiments

* What tasks & datasets were used for evaluations?
* How well can DPO optimzie the RLHF objective?
* Can DPO scale to real preference datasets?
* Can DPO generalize to a new input distribution?
* How do GPT4's judgements compare with human judgements?

## Conclusion & Discussion

* What do you think of the Paper?
* Have you trained a model with DPO? Can you think of cases where you would consider it at work?
* What references do you find most interesting?