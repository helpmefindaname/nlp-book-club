# Illustrating Reinforcement Learning from Human Feedback (RLHF)

[Huggingface blog post](https://huggingface.co/blog/rlhf)

## Preliminaries/Refreshers 
* How do (autoregressive) language models work? How are they trained?
* Why are autoregressive language models interesting?
* What kind of metrics are BLEU and ROUGE, what are they usually used for? 
* What are the basics of Reinforcement learning? What do policy, action space, ovservation space and reward function mean? 

## Intro

* What are the shortcomings of Cross Entropy, BLEU and ROUGE?
* What is the basic idea of using Reinforcement Learning=

## Pretraining language models

* What are the sizes of the example models from: OpenAI, Anthropic and DeepMind?
* What is meant by augmented data? How does it differ from RLHF?

## Reward model training

* What is a scalar reward and why is it crucial for RLHF?
* How does the reward modeling work?
* What kind of rating will be annotated by human annotators?
* How will the final reward be calculated?

## Fine-tunining with RL

* On a high level, how does the Proximal Policy Optimizatino (PPO) work?
* Why are some parameters frozen? Which parameters do you think are frozen?
* How is the scalar for "preferability" calculated?
* What is the idea behind the KL-divergence as part of the RL policy?


## Open-source tools for RLHF 

* How many open source tools were mentioned in the article. From their descriptions, which sounds like the most fitting for usage?
* Using the dataset explorer we can look at the dataset created by Anthropic: Looking at the first example in the training set, do you agree with the chosen value?

## What’s next for RLHF?

* Which of the mentioned limitations are applicable to basically all ML models?
* What limitations are specific to the RLHF solution?


## Final part

* Which of the further readings sounds interesting to you?
* What do you think of RLHF?
* Have you tried out ChatGPT? If yes, how was it?
* Have you heard of this [Open source alternative](https://www.youtube.com/watch?v=64Izfm24FKA)?

