import pytest

import pandas as pd
import numpy as np
from transplantbenefit import encoder, cases


# I thought I would go insane.
@pytest.mark.parametrize(
    "primary_disease,encoded_vec",
    [
        ("1", [0, 0, 0, 0, 0, 0, 0, 0]),
        ("2", [1, 0, 0, 0, 0, 0, 0, 0]),
        ("3", [0, 0, 0, 0, 0, 0, 0, 0]),
        ("4", [0, 1, 0, 0, 0, 0, 0, 0]),
    ],
)
def test_disease_encoding(primary_disease, encoded_vec):
    assert list(encoder.make_rdisease_vec(primary_disease, "0", "0", 0)) == encoded_vec


# From R code.
encoded_default_case = pd.Series(
    {
        "RCANCER": False,
        "RAGE - MEAN(RAGE)": 52.0,
        "RAGE SQUARED - MEAN(RAGE SQUARED)": 2704.0,
        "RGENDER": 0.0,
        "RHCV": 0.0,
        "RDISEASE GROUP=2": 0.0,
        "RDISEASE GROUP=4": 0.0,
        "RDISEASE GROUP=5": 0.0,
        "RDISEASE GROUP=6": 0.0,
        "RDISEASE GROUP=7": 0.0,
        "RDISEASE GROUP=8": 0.0,
        "RDISEASE GROUP=9": 0.0,
        "RDISEASE GROUP=10": 0.0,
        "LN(RCREATININE) - MEAN(LN(RCREATININE))": 4.248495,
        "LN(RBILIRUBIN) - MEAN(LN(RBILIRUBIN))": 2.995732,
        "LN(RINR) - MEAN(LN(RINR))": 0.0,
        "RSODIUM - MEAN(RSODIUM)": 135.0,
        "RPOTASSIUM - MEAN(RPOTASSIUM)": 4.5,
        "RALBUMIN - MEAN(RALBUMIN)": 30.0,
        "RRENAL": 0.0,
        "RINPATIENT": 0.0,
        "RREGISTRATION YEAR=2007": 0.0,
        "RREGISTRATION YEAR=2008": 0.0,
        "RREGISTRATION YEAR=2009": 0.0,
        "RREGISTRATION YEAR=2010": 0.0,
        "RREGISTRATION YEAR=2011": 0.0,
        "RREGISTRATION YEAR=2012": 0.0,
        "LN(RBILIRUBIN)*RSODIUM - MEAN(LN(RBILIRUBIN)*RSODIUM)": 404.423857,
        "RDISEASE GROUP=2*LN(RBILIRUBIN)": 0.0,
        "RDISEASE GROUP=4*LN(RBILIRUBIN)": 0.0,
        "RDISEASE GROUP=5*LN(RBILIRUBIN)": 0.0,
        "RDISEASE GROUP=6*LN(RBILIRUBIN)": 0.0,
        "RDISEASE GROUP=7*LN(RBILIRUBIN)": 0.0,
        "RDISEASE GROUP=8*LN(RBILIRUBIN)": 0.0,
        "RDISEASE GROUP=9*LN(RBILIRUBIN)": 0.0,
        "RDISEASE GROUP=10*LN(RBILIRUBIN)": 0.0,
        "RAGE*LN(RCREATININE) - MEAN(RAGE*LN(RCREATININE))": 220.921753,
        "RPREVIOUS ABDOMINAL SURGERY": 0.0,
        "RENCEPHALOPATHY": 0.0,
        "RASCITES": 0.0,
        "LN(RWAITING TIME+1) - MEAN(LN(RWAITING TIME+1))": 3.433987,
        "RDIABETES": 0.0,
        "RDISEASE GROUP=2*RAGE": 0.0,
        "RDISEASE GROUP=4*RAGE": 0.0,
        "RDISEASE GROUP=5*RAGE": 0.0,
        "RDISEASE GROUP=6*RAGE": 0.0,
        "RDISEASE GROUP=7*RAGE": 0.0,
        "RDISEASE GROUP=8*RAGE": 0.0,
        "RDISEASE GROUP=9*RAGE": 0.0,
        "RDISEASE GROUP=10*RAGE": 0.0,
        "LN(RMAXIMUM AFP LEVEL+1) - MEAN(LN(RMAXIMUM AFP LEVEL+1))": 1.791759,
        "RMAXIMUM TUMOUR SIZE - MEAN(RMAXIMUM TUMOUR SIZE)": 1.0,
        "RTWO TUMOUR": 0.0,
        "RTHREE OR MORE TUMOURS": 0.0,
        "DAGE - MEAN(DAGE)": 52.0,
        "DCAUSE OF DEATH=2": 0.0,
        "DCAUSE OF DEATH=3": 0.0,
        "DCAUSE OF DEATH=4": 0.0,
        "DBMI - MEAN(DBMI)": 25.0,
        "DHISTORY OF DIABETES=2": 0.0,
        "DHISTORY OF DIABETES=9": 0.0,
        "DTYPE=2": 0.0,
        "RHCV*DHISTORY OF DIABETES=2": 0.0,
        "RHCV*DHISTORY OF DIABETES=9": 0.0,
        "RHCV*DAGE": 0.0,
        "DTYPE=2*RAGE": 0.0,
        "DTYPE=2*LN(RCREATININE)": 0.0,
        "RDISEASE GROUP=2*DTYPE=2": 0.0,
        "RDISEASE GROUP=4*DTYPE=2": 0.0,
        "RDISEASE GROUP=5*DTYPE=2": 0.0,
        "RDISEASE GROUP=6*DTYPE=2": 0.0,
        "RDISEASE GROUP=7*DTYPE=2": 0.0,
        "RDISEASE GROUP=8*DTYPE=2": 0.0,
        "RDISEASE GROUP=9*DTYPE=2": 0.0,
        "RDISEASE GROUP=10*DTYPE=2": 0.0,
        "BLOOD GROUP COMPATIBILITY": 0.0,
        "LIVER MEETS SPLIT CRITERIA": 0.0,
    }
)


def test_default_case_encoding():
    tol = 1e-6
    encoded_default_case_prime = encoder.encode(cases.make_default_case()).iloc[0]
    assert (
        np.linalg.norm(
            encoded_default_case_prime.astype(float)
            - encoded_default_case.values.astype(float),
            ord=np.inf,
        )
        < tol
    )
