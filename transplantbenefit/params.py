import pathlib
import pandas as pd


class ParameterStore:
    def __init__(self, param_dir=None):
        if param_dir is None:
            param_dir = pathlib.Path(__file__).parent
        self.betas = pd.read_csv(param_dir / "betas.csv", index_col=0)
        self.surv_cancer = pd.read_csv(param_dir / "surv_cancer.csv", index_col=0)
        self.surv_noncancer = pd.read_csv(param_dir / "surv_noncancer.csv", index_col=0)


# Singleton to hold the parameter vecs.
param_store = ParameterStore()