# Train large then compress later

[Paper link](https://arxiv.org/pdf/2002.11794.pdf)

## Prerequisites

* How large are the various transformer variants of popular models?
  List total number of parameters, parameters used in embedding matrix,
  parameters used in attention and parameters used in linear layers for:
  a) bert-base
  a) roberta-base, roberta-large
  b) xlm-roberta-base, xlm-roberta-large
  c) t5-small, t5-base, t5-large, t5-3b, t5-11b
  d) md5-base, mt5-large
* Explain each of the following compression/speed-up methods and how
  they differ. What kind of compression, inference speed and performance
  change can we expect for each?
  a) Unstructured pruning (e.g. Movement pruning)
  b) Structured pruning (columns/rows/attention heads)
  c) Quantization
  d) Distilation
  Can we combine these approaches? Or are they exclusive?
* What is "wall clock time", and why is it an important measure? What other
  types of measuring time when benchmarking computer programmes are there?
* Language models are often evaluated using "perplexity".
  a) What exactly is the meaning of perplexity? In what units is it specified?
  b) What are "good" of perplexity for English language text?
  c) Is perplexity defined only for causal language models or also for masked
     language models?

## Intro
* Typically larger models trained with more training data perform better on
down-stream tasks. For which kinds of tasks would you expect this to hold strongly
and for which tasks might this assertion fail?
* What do the authors mean when they say "train until convergence"? How would you
  measure when this point is reached?
* The authors scale roberta by number of layers (3, 6, 12, 18, 24 layers). And through
  the hidden size (256, 512, 768, 1024, 1536). How does this compare with the scaling
  of roberta-base and roberta-large?
* How many hours do each of the (3, 6, 12, 18, 24)-layer models take to reach MLM Validation
  Perplexity of 5?

## Experimental Setup
* What hardware did the authors use for their tests?
* How long did their trainings last?
* What is fairseq?


## Larger Models train faster
* How does scaling model width and depth play out?
* Batch size:
  a) What was the authors conclusion regarding batch sizes?
  b) How did they scale the learning rate when they changed the batch size?
  c) What is the motivation for larger batch sizes?
  d) What is the advantage of smaller batch sizes?
* In "Returns Diminish as Size Increases" the authors mention the largest
  models they experimented with become "increasingly compute-bound". What
  was limiting the model training speed, if not computational power, previously?

## Larger Models compress better

* Which levels of quantisation did the authors investigate?
* Which levels of pruning?
* Are (unstructured) pruning and quantisation a size only optimization or
  do they also improve prediction speed?
* How much accuracy do the largest models from Figure 6 lose when quantizing from
  32bit floats to 8bit? By what factor does model size decrease?
* How much accuracy do the largest models in Figure 6 lose when pruning 75%? By what
  factor does the model size increase?
* In the "Movement Pruning" paper, the authors showed an *increase* in accuracy after
  applying movement pruning, but here pruning seems to always be (slightly) negative for
  the accuracy. Why could movement pruning improve results but here they do not show
  this effect?


## Final part

* What do you think of the paper?
* Do you plan to test larger model sizes in the future?
* Have you used compression techniques already? Are you inspired to do so now?
* What references sound interesting to you?
* How manny stars does the FastFormers Github repo have, and should we discuss
  their paper next?

