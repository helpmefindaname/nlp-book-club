# LiLT: A Simple yet Effective Language-Independent Layout Transformer for Structured Document Understanding

[Paper link](https://arxiv.org/pdf/2202.13669.pdf)
[Github repo](https://github.com/jpWang/LiLT)
[Lilt-roberta-en](https://huggingface.co/SCUT-DLVCLab/lilt-roberta-en-base)
[Lilt-only-base](https://onedrive.live.com/?cid=59456af9b1877e17&id=59456AF9B1877E17%21124&authkey=%21AEIRbCmcWKjhoSM)


## Preliminaries/Refreshers 

* What are the FUNSD and XFUNSD datasets?
* How does a Transformer work?
* What are multimodal Layout Transformer?
* How can multimodal Layout Transformer be used in Flair (master)?

## Introduction

* What techniques and learning tasks are proposed in this paper?
* What are the main contribution points of this paper?

## LILT

* How does the TextEmbedding compare to the text embedding of Bert/Roberta/etc.?
* How does the LayoutEmbedding compare to Multimodal Transformers we do already know?
* Looking at **Figure 2**, how does the BiACM work?
* Why are the text->layout-interactions detached when pretraining? Why not when finetuning?

## Pretraining Tasks

* How does the Masked-Visual Language Modeling?
* How does the Key Point Location work?
* How does the Cross-Modal Alignment Identification work?
* What considerations were done on the optimization strategy?

## Experiments

* What pretrained models are used for bases?
* What are the hyperparameters for the Lilt-Transformer?
* Looking at **Table 1** what are the experiments in the ablation study?
* What is the slow down ratio exactly?
* Looking at **Table 2** how does LILT compare to other models on the FUNSD dataset?
* Looking at **Table 3** how does LILT compare to other models on the CORD dataset?
* Looking at **Table 4** how does LILT compare to other models on the chineese EPHOIE dataset?
* Looking at **Table 5** how does LILT compare to other models on the RVL-CDIP dataset?
* Looking at **Table 6** how does LILT trained on english only documents compare to other models on the multilingual XFUNSD?
* Looking at **Table 7** how does LILT trained on FUNSD perform zeroshot on XFUNSD?

## Conclusions, Implications and final thoughts

* What do you think of the paper?
* Do you think the experiments were sufficient? Would you like to see different experiments as well?
* What references sound interesting to you?
* How many stars does their Github repo have?
* How easy or hard is it to create a LILT model out of Gelectra, RobertaXLM, or CamenBERT?
