# OCR-free Document Understanding Transformer

[Paper link](https://arxiv.org/pdf/2111.15664.pdf)
[Github](https://github.com/clovaai/donut)
[HF-Hub](https://huggingface.co/naver-clova-ix/donut-base)

# Preliminaries

* How does an Encoder-Decoder Architecture work with Transformers?
* What tasks can be applied with an Encoder-Decoder Architecture? How do they work?
* How does a Document Understanding Pipeline usually look like?
* How can multi-modality be applied with Transformers?

## Introduction

* What are the critical problems with OCR-dependent approaches?
* What are their claims about the overall performance compared to OCR-approaches?
* What are the 4 highlighted contributions?

## Document Understanding Transformer

* How do earlier Vision-Document-Understanding attempts without OCR perform?
* How does the architecture of DONUT look like? What is the output?
* What model is used for the Encoder block?
* What model is used for the Decoder block?
* How is the output converted to the task specific outputs?
* How does the pretraining work?
* What corpus is used for pretraining?
* How is the syntetic training data generated?
* Looking at **figure 3**, how are the fine-tuning tasks designed?

## Experiments

* What tasks are used in the experiments?
* What metrics are used for the Document Information Extraction task?
* How are the layers reduced compared to the models used for each block?
* Looking at **Table 1**, **Table 2** and **Table 3**, how does Donut perform compared to other approaches?
* What further studies have been done by the authors?

## Related Work

* What other work exists and how does it roughly work?


## Conclusions

* What are the main points in the conclusion?


## Discussion

* What do you think of Donut?
* What possibilities do you see?
* Did they not mention something that could be considered important?
* Looking at their github, how hard does it look like to adjust their code for custom experiments?
* How many stars does their Github have?
* Which reference do you find most interesting?
