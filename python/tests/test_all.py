import pytest
import lavia


def test_sum_as_string():
    assert lavia.sum_as_string(1, 1) == "2"
