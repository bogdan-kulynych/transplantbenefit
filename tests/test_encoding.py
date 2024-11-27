import pytest

import numpy as np
from transplantbenefit import encoder


# I thought I would go insane.
@pytest.mark.parametrize(
    "primary_disease,encoded_vec",
    [
        (1, [0, 0, 0, 0, 0, 0, 0, 0]),
        (2, [1, 0, 0, 0, 0, 0, 0, 0]),
        (3, [0, 0, 0, 0, 0, 0, 0, 0]),
        (4, [0, 1, 0, 0, 0, 0, 0, 0]),
    ],
)
def test_disease_encoding(primary_disease, encoded_vec):
    assert list(encoder.make_rdisease_vec(primary_disease, 0, 0, 0)) == encoded_vec
