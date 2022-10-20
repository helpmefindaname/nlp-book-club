# SGD can converge to local maxima

[Paper](https://openreview.net/forum?id=9XhPLAjjRB)

**Notice:** this paper is highly theoretical and in my opinion hard to read, I recommend taking the time to look into it several attempts and not just look into it the day before.

# Intro

* What is SGD and why is it important?
* What are the reasons that SGD is hard to understand?
* What does `discrete-time` mean?
* What does `state-dependend noise` mean?
* What is the setting of this Paper?

## Related works

* What is the main strategy to escape saddle points?
* Why is mini batch noise relevant for training?
* What practical and theoretical foundation exists for Large Learning Rates?

## Warm-UP Example

* How does the Warm-UP example show the possibility of converging to a local maxima?
* What does this example tell us about using the norm of parameters for measuring the escape rate? (You can look at [big science tensorboard](https://huggingface.co/bigscience/tr11-176B-ml-logs/tensorboard) gradient norms, to see what they look like)

## Findings

* How can SGD converge to maxima when GD cannot?
* Why did prior work not find that case?
* What conclusions do the Authors provide for further research?

* Why can SGD escape saddle points arbitrarily slowly?
* What suggestions do the Authors provide towards escaping saddle points?

* How is the sharpness of a local minimum defined?
* How do they show that SGD may prefer sharper minima?
* Is a sharper minima bad per se?

* How is AMSGrad related to SGD?

## Discussion

* what is the conclusion of this paper?
* what were the most interesting findings?
* can we derive some learnings to use in future trainings?
* what references do you find most interesting?