import numpy as np
import pandas as pd

from sklearn.base import BaseEstimator

from transplantbenefit.params import param_store

CANCER_INDICATOR = 0


class BaseTBSModel(BaseEstimator):
    """
    Implements a Cox survival model for the need and utility of a transplant.
    """

    def predict_need(self, X):
        X = np.delete(X, CANCER_INDICATOR, axis=1)
        return np.sum(
            self.m1_surv.values
            ** np.exp(np.sum(self.m1_beta.values * (X - self.m1_mean.values)))
        )

    def predict_utility(self, X):
        X = np.delete(X, CANCER_INDICATOR, axis=1)
        return np.sum(
            self.m2_surv.values
            ** np.exp(np.sum(self.m2_beta.values * (X - self.m2_mean.values)))
        )

    def predict(self, X):
        return self.predict_utility(X) - self.predict_need(X)

    def fit(self, X, y):
        raise ValueError("Fitting not supported for this estimator.")


class TBSCancerModel(BaseTBSModel):

    def __init__(self):
        self.m1_mean = param_store.betas["m1_cancer_mean"]
        self.m2_mean = param_store.betas["m2_cancer_mean"]
        self.m1_beta = param_store.betas["m1_cancer_beta"]
        self.m2_beta = param_store.betas["m2_cancer_beta"]
        self.m1_surv = param_store.surv_cancer["m1_surv"]
        self.m2_surv = param_store.surv_cancer["m2_surv"]


class TBSNonCancerModel(BaseTBSModel):
    def __init__(self):
        self.m1_mean = param_store.betas["m1_noncancer_mean"]
        self.m2_mean = param_store.betas["m2_noncancer_mean"]
        self.m1_beta = param_store.betas["m1_noncancer_beta"]
        self.m2_beta = param_store.betas["m2_noncancer_beta"]
        self.m1_surv = param_store.surv_noncancer["m1_surv"]
        self.m2_surv = param_store.surv_noncancer["m2_surv"]


class TBSPredictor:
    """
    TBS benefit predictor.

    Adaptively chooses cancer or non-cancer model.
    """

    def __init__(self):
        self.cancer_model = TBSCancerModel()
        self.noncancer_model = TBSNonCancerModel()

    def _apply_to_groups(self, X, cancer_method, noncancer_method):
        X = np.asarray(X)
        cancer_mask = X[:, CANCER_INDICATOR].astype(bool)
        predictions = np.zeros(len(X))
        if cancer_mask.any():
            predictions[cancer_mask] = cancer_method(X[cancer_mask])
        if (~cancer_mask).any():
            predictions[~cancer_mask] = noncancer_method(X[~cancer_mask])
        return predictions

    def predict_need(self, X):
        return self._apply_to_groups(
            X, self.cancer_model.predict_need, self.noncancer_model.predict_need
        )

    def predict_utility(self, X):
        return self._apply_to_groups(
            X, self.cancer_model.predict_utility, self.noncancer_model.predict_utility
        )

    def predict(self, X):
        return self._apply_to_groups(
            X, self.cancer_model.predict, self.noncancer_model.predict
        )
