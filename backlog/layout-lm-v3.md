# LayoutLMv3: Pre-training for Document AI with Unified Text and Image Masking

[Paper link](https://arxiv.org/pdf/2204.08387.pdf)
[Github](https://github.com/microsoft/unilm/tree/master/layoutlmv3)
[hf-hub](https://huggingface.co/models?other=layoutlmv3)
[example 1](https://huggingface.co/spaces/Theivaprakasham/layoutlmv3_invoice)
[example 2](https://huggingface.co/spaces/rajistics/receipt_extractor)
[example 3](https://huggingface.co/spaces/oussama/LyoutLMv3_invoice)
[example 4](https://huggingface.co/spaces/Theivaprakasham/layoutlmv3_sroie)

## Preliminaries/Refreshers 

* How do transformers work?
* What is masked language modelling?
* How are positions handled in transformers?
* How could a transformer be extended to function multimodal (e.g. have text and image inputs)

## Introduction

* How do Patch, Grid and Region vary from each other?
* What is masked image modelling? How does it relate to masked language modelling?
* What are the disadvantages of the other multimodal approaches for Document AI?
* What are the 4 contributions mentioned in the paper?

## LayoutLMv3

* What embeddings exists in LayoutLMv3?
* What is the difference between word-level positions and segment-level positions and which is used?
* How are the patches taken as input?
* (Optional) What are semantic 1D relative position and spatial 2D relative position as bias terms?
* What is the general architecture LayoutLMv3 is using? (encoder, decoder or encoder-decoder)
* Is the Masked Language Modelling task the same as described in the bert paper? If not how does it diviate?
* (Optional) What is an Image tokenizer and how is it used in Masked Image Modelling?
* How does the Word-Patch Alignment work? Why is it important?

## Experiments

* Is there something surprising in the choice of hyperparameters?
* How does the "CogView"-based attention computation change results? What is the impact of the $-max()$ and what is the impact of α?
* What could be the reason that only 11m of all 42m pages were used for pretraining?
* What models are used for initializing
* What are the 4 datasets used for evaluation on text-centric tasks? Are there examples accessible on the internet?
* How does LayoutLMv3 compare to other models?
* How does LayoutLMv3 perform on image-only tasks?
* What are the findings of the ablation studies?

## Related Work
* What other work exists and how does it roughly work?
* What are their ideas for future work?

## Discussion

* What do you think of LayoutLMv3?
* Have you tried out any of the example spaces? If so, any interesting findings?
* How easy is it to use LayoutLMv3? (via transformers)
* If you had access to TPU's (e.g. [TPU reasearch Cloud](https://sites.research.google/trc/about/)) and could design another pretraining. What would you care about/try out?
* How many stars does their Github have?
* Which reference do you find most interesting?