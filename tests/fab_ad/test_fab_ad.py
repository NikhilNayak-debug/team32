# 
# test_AD.py
# Created at 2:15 PM 11/22/22 by Saket Joshi
#
import pytest

from src.fab_ad.fab_ad import FabTensor


def test_fabtensor_sanity():
    x = FabTensor(value=3, derivative=0, identifier='x')
    y = FabTensor(value=-4, derivative=1, identifier='y')
    z = x ** 2 + y ** 2
    assert z.value == 25
    assert z.derivative == -8
    assert z.identifier == 'x^2 + y^2'


def test_log_on_string_type_returns_type_error():
    with pytest.raises(TypeError):
        FabTensor.log("hello")


if __name__ == "__main__":
    pass
