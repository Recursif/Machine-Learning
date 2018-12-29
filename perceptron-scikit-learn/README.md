
# Perceptron

The Perceptron is a basic Machine-learning algorithm, that train with labelled datas input and permit to classified unlabeled datas after it's been trained.

For each data as input Xn, the algo associates at each features fi
of this data a weigth wi (for the first training data input those weigth are set to zero
or can take a random value) and the algo computed the linear combination of the features
by the weight.

Then come de binary classification, if this result is below a certain threshold
the class predicted is 1 else the class is 0.

For the training if the result predicted by the model is equal to the real class then there no update on weigth,
but if they are different the weigth are updated according to a learning rate that we've chosed.

We train n-iter times the Perceptron with the trainin set to help him converge.


# Disavantages

The percepton only converge if the datas can seperates linearly.
Else we use another technique the Logistic regression.
