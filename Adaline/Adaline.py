#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

class Adaline(object):
    """ADAptative LInear NEuron

    Parameters
    -----------
    eta : float
        Learning rate (between 0.0 and 1.0).
    n_iter : int
        Passes over the training set.

    Attributes
    ----------
    w_ : 1d-array
        Weight after fitting.
    cost_ : list
        Cost in every epoch.
    """
    def __init__(self, eta=0.01, n_iter=50):
        self.eta = eta
        self.n_iter = n_iter

    def fit(self, X, y):
        """Fit training data.

        Parameters
        -----------
        X = {array-like}, shape = [n_features, n_samples]
            Training Vector,
            where n_samples is number of samples
            and n_features the number of features.
        y = {array_like}, shape = [n_samples]

        Returns
        --------
        self : object
        """
        self.w_ = np.zeros(X.shape[1] + 1)
        self.cost_ = []

        for i in range(self.n_iter):
            output = self.net_input(X)
            errors = (y - output)
            self.w_[1:] = self.eta * X.T.dot(errors)
            self.w_[0] = self.eta * errors.sum()
            cost = (errors**2).sum() / 2.0
            self.cost_.append(cost)
        return self

    def net_input(self, X):
        """Calcul net input."""
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def activation(self, X):
        """Compute linear activation."""
        return self.net_input(X)

    def predict(self, X):
        """Return the class label after unit step."""
        return np.where(self.activation(X) >= 0.0, 1, -1)
