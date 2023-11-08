# Vision Transformers Need Registers

[Paper link](https://arxiv.org/abs/2309.16588)
[Open source implementation](https://github.com/kyegomez/Vit-RGTS)

## Preliminaries/Refreshers

* What are Vision Image Transformers?
* Are ViTs Encoder, Decoder or Encoder-Decoder models?

## Introduction

* What is the *DINO* algorithm? Why is it relevant?
* What is *DINOv2*?
* How do *DINO* and *DINOv2* differ in their feature representation?
* What information is found in the tokens with signification higher norm of the feature embeddings?
* What is the proposal of this paper?

## Problem Formulation

* What are the claims & analyses of the following statements:
    * `Artifacts are high-norm outlier tokens`
    * `Outliers appear during the training of large models`
    * `High-norm tokens appear where patch information is redundant`
    * `High-norm tokens hold little local information`
    * `Artifacts hold global information`
* What fix is proposed to fix dense prediction tasks and those artefacts?

## Experiments

* What models are used for experimentation?
* How will the efects be evaluated?
* How was decided how many registers work the best?
* Looking at **Table 3**, how do the register tokens impact Unsupervised Object Discovery?
* Looking at **Fig. 9**, how does the qualitative evaluation of registers show?


## Related Work

* What related work exists on feature extraction with pretrained models?
* What related work exists on additional tokens in transformers?

## Discussion

* What do you think of the Register tokens?
* Can you think of possible uses of Register tokens in NLP or other domains?
* What references do you find most interesting?
