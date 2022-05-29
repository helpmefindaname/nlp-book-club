# Learning Strides in Convolutional Neural Networks

[Paper link](https://arxiv.org/pdf/2202.01653.pdf)

## Prerequisites

* What are strides in Convolutional Neural Networks?
* Why can a standard implementation of strides not be learned?
* What relationship does the [Fourier Transformation](https://en.wikipedia.org/wiki/Fourier_transform) have to convolutions?

## Intro

* Why is down sampling important in Convolutional Neural Networks?
* What are the main promises of this paper?

## Methods

* Read through the notations carefully, this point for everyone to ask for questions about the notation during the meeting, so we can prevent misunderstandings upfront.
* What are the advantages and what are the disadvantages of downsampling in CNN's?
* What do Spatial and Spectral refer to?
* What can Spectral Pooling do what Spatial Pooling cannot? What important property does Spectral Pooling still not provide?
* What is the motivation of DiffStride (and therefore this Paper)?
* Looking at Figure 1: how does DiffStride work? which part of *w* is differentiable?
* What does it mee to have a Stride of 1.5?
* How can DiffStride be integrated into ResNets?
* How can Memory Cost and Computation Cost be regularized with DiffStride?
* How could the regularization be adopted if kernel sizes or channel counts would change over layers?

## Experiments

* How do the experiments run?
* Why do Strided Convolutions and Spectral Striding not achieve the same accuracy in audio tasks?
* What behaviours does DiffStride show that might justify increased accuracy on the audio tasks?
* How do different initial strides impact DiffStride? How does it impact the other methods?
* What can we see in the distribution of learned strides? is there something notable?
* To which value was the parameter R set in the experiments? Were there any experiments towards it?
* Do you think the experimentation was sufficient? Would you have liked to see different experiments or found something missing?

## Limitations

* Reading about *Regularizing the complexity* they describe how rounding the strides and using strided convolution can have extreme differences in accuracy. What could that mean?
* What limitation is mentioned towards computational costs?

## Final part

* What do you think of the paper?
* Could you see yourself using DiffStride in future projects?
* What references sound interesting to you?
* How manny stars does their Github repo have?

