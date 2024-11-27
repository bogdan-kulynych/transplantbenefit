import numpy as np
import pandas as pd

from sklearn.base import BaseEstimator

from params import param_store


class BaseTBSModel(BaseEstimator):
    """
    Implements two Cox survival models for the need and utility of a transplant.
    """

    def predict_need(self, X):
        return np.sum(self.m1_surv ** np.exp(np.sum(self.m1_beta * X)))

    def predict_utility(self, X):
        return np.sum(self.m2_surv ** np.exp(np.sum(self.m2_beta * X)))

    def predict(self, X):
        return self.predict_utility(X) - self.predict_need(X)

    def fit(self, X, y):
        raise ValueError("Fitting not supported for this estimator.")


class TBSCancerModel(BaseTBSModel):
    def __init__(self):
        self.m1_beta = param_store.betas["m1_cancer_beta"]
        self.m2_beta = param_store.betas["m2_cancer_beta"]
        self.m1_surv = param_store.surv_cancer["m1_surv"]
        self.m2_surv = param_store.surv_cancer["m2_surv"]


class TBSNonCancerModel(BaseTBSModel):
    def __init__(self):
        self.m1_beta = param_store.betas["m1_noncancer_beta"]
        self.m2_beta = param_store.betas["m2_noncancer_beta"]
        self.m1_surv = param_store.surv_noncancer["m1_surv"]
        self.m2_surv = param_store.surv_noncancer["m2_surv"]
