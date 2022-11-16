# Long Expressive Memory for Sequence Modeling

[Paper link](https://openreview.net/forum?id=vwj6aUeocyf)

## Introduction

* what is the vanishing/exploding gradient problem?
* what is the general problem with long-term dependencies?
* how do the authors propose to solve this problem?

## Long Expressive Memory

* Looking at equation **(1)**: what is the input, what is the output and how can we interpret the derivative?
* What is the difference between equation **(2)** and equation **(1)**?
* What is the difference between equation **(3)** and equation **(2)**?

## Related Work

* How does the LEM specified by equation **(3)** compare to LSTMs?
* What is the difference between LEM and other ODE-based learning architectures?

## Analysis of LEM (optional)

* Prove that the hidden states are bound.
* Are the  long range dependencies analysed theoretically?

## Empirical Results

* What tasks are used for evaluating?
* What are the most interesting findings about the Very long adding problem?
* How is mnist considered to be a worthy experiment setup?
* How does LEM beat the state of the art in a Healthcare application?
* How does LEM compare to LSTM in Language modeling?
* Are there any experiments/comparisons you'd say are missing? 

## Discussion

* What do you think of LEM?
* Do you think will LEM replace LSTM's?
* How manny stars does their github repo have?
* What references do you find most interesting?
