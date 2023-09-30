# Nougat: Neural Optical Understanding for Academic Documents

[Paper link](https://arxiv.org/pdf/2308.13418.pdf)
[Github](https://github.com/facebookresearch/nougat)


## Preliminaries/Refreshers

* How does a typical OCR model work? Which components are there?
* What are common OCR libraries to use?
* How do Encoder-Decoder transformers architectures work?


## Introduction

* what is the issue with extracting text from PDFs?
* what is the issue with the usual OCR engines?
* what are the promised contributions of this paper?

## Related Work

* What different types of OCR exist? How do they differ?
* How do VDU models work?
* What solutions exist for parsing PDFs of scientific documents?

## Model

* What is the architecture of Nougat?
* What is used for the Encoder?
* What is used for the Decoder?
* How are the hyperparameters setup?
* What kind of data augmentation is used?

## Datasets

* What data sources were chosen?
* How were the pdfs processed?
* What is the approach for page splitting?
* How was the Ground truth created?

## Results & Evaluation

* What metrics were used for evaluation?
* What different text modalities were taken into account?
* How is mnist considered to be a worthy experiment setup?
* How does LEM beat the state of the art in a Healthcare application?
* How does LEM compare to LSTM in Language modeling?
* Are there any experiments/comparisons you'd say are missing? 
* What issues occoured with repetitions during the inference? How were they handled?

## Limitations & Future work

* What are the limitations of the Model?
* What idea do they ahve for future work?

## Discussion

* What do you think of Nougat?
* What do you think of the general approach of using Image-Encoder->Text-Decoder for DocumentTransformer?
* How manny stars does their github repo have?
* What references do you find most interesting?
