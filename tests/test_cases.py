import numpy as np
import pytest

from transplantbenefit import cases
from transplantbenefit import encoder
from transplantbenefit import core

import pprint


def test_default_case():
    case = cases.make_default_case()
    encoded = encoder.encode(case)
    X = encoded.values

    predictor = core.TBSPredictor()

    need = predictor.predict_need(X)[0]
    utility = predictor.predict_utility(X)[0]
    assert need == pytest.approx(1387, abs=1)
    assert utility == pytest.approx(1596, abs=1)
