# test_AD.py
# Created at 2:15 PM 11/22/22 by Saket Joshi
# This test file contains all the test cases for fab_ad.py

import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src/fab_ad')))
from fab_ad import FabTensor
from fab_admath import *


def test_fabtensor_sqrt():
    x = FabTensor(value=4, derivative=[1, 0], identifier='x')
    y = FabTensor(value=9, derivative=[0, 1], identifier='y')
    z = sqrt(x) + sqrt(y)
    print(z)
    assert pytest.approx(z.value, 0.01) == 5.0
    assert z.directional_derivative(seed_vector=[1, 0]) == 0.25
    assert z.directional_derivative(seed_vector=[0, 1]) == 1 / 6
    assert z.identifier == 'sqrt(x) + sqrt(y)'


def test_fabtensor_exp():
    x = FabTensor(value=4, derivative=[1, 0], identifier='x')
    y = FabTensor(value=9, derivative=[0, 1], identifier='y')
    z = exp(x) + exp(y)
    assert pytest.approx(z.value, 0.01) == 8157.682077608529
    assert z.directional_derivative(seed_vector=[1, 0]) == 54.598150033144236
    assert z.directional_derivative(seed_vector=[0, 1]) == 8103.083927575384
    assert z.identifier == 'e^(x) + e^(y)'


def test_fabtensor_log():
    tensor = FabTensor(value=4, derivative=1, identifier='x')
    z = log(tensor) + log(tensor)
    assert pytest.approx(z.value, 0.01) == 2.772588722239781
    assert z.derivative == 0.5
    assert z.identifier == 'log(x) + log(x)'


def test_fabtensor_sin():
    tensor = FabTensor(value=4, derivative=1, identifier='x')
    x = FabTensor(value=4, derivative=0, identifier='x')
    y = FabTensor(value=9, derivative=1, identifier='y')
    z = sin(tensor) + sin(tensor)
    assert pytest.approx(z.value, 0.01) == -1.5136049906158566
    assert z.derivative == -1.3072872417272239
    assert z.identifier == 'sin(x) + sin(x)'


def test_fabtensor_cos():
    x = FabTensor(value=4, derivative=[1, 0], identifier='x')
    y = FabTensor(value=9, derivative=[0, 1], identifier='y')
    z = cos(x) + cos(y)
    assert pytest.approx(z.value, 0.01) == -1.5647738827482889
    assert pytest.approx(z.directional_derivative(seed_vector=[1, 0])) == 0.7568025
    assert pytest.approx(z.directional_derivative(seed_vector=[0, 1])) == -0.41211849
    assert z.identifier == 'cos(x) + cos(y)'


def test_fabtensor_tan():
    x = FabTensor(value=4, derivative=[1, 0], identifier='x')
    y = FabTensor(value=9, derivative=[0, 1], identifier='y')
    z = tan(x) + tan(y)
    assert pytest.approx(z.value, 0.0001) == 0.7055056229077676
    assert pytest.approx(z.directional_derivative(seed_vector=[1, 0]), 0.0001) == 2.34055012
    assert pytest.approx(z.directional_derivative(seed_vector=[0, 1]), 0.0001) == 1.20458946
    assert z.identifier == 'tan(x) + tan(y)'


def test_fabtensor_asin():
    x = FabTensor(value=0.5, derivative=[1, 0], identifier='x')
    y = FabTensor(value=0.5, derivative=[0, 1], identifier='y')
    z = arcsin(x) + arcsin(y)
    assert pytest.approx(z.value, 0.01) == 1.0471975511965979
    assert pytest.approx(z.directional_derivative(seed_vector=[1, 0]), 0.0001) == 1.15470054
    assert pytest.approx(z.directional_derivative(seed_vector=[0, 1]), 0.0001) == 1.15470054
    assert z.identifier == 'sin^-1(x) + sin^-1(y)'
    
    
def test_fabtensor_arccos():
    x = FabTensor(value=0.5 * (3 ** 0.5), derivative=[1, 0], identifier='x')
    y = FabTensor(value=0.5 * (3 ** 0.5), derivative=[0, 1], identifier='y')
    z = arccos(x) + arccos(y)
    assert pytest.approx(z.value, 0.01) == 1.0471975511965979 * 2
    assert pytest.approx(z.directional_derivative(seed_vector=[1, 0]), 0.0001) == -2
    assert pytest.approx(z.directional_derivative(seed_vector=[0, 1]), 0.0001) == -2
    assert z.identifier == 'cos^-1(x) + cos^-1(y)'


def test_fabtensor_arctan():
    x = FabTensor(value=3 ** -0.5, derivative=[1, 0], identifier='x')
    y = FabTensor(value=3 ** -0.5, derivative=[0, 1], identifier='y')
    z = arctan(x) + arctan(y)
    assert pytest.approx(z.value, 0.01) == 1.0471975511965976
    assert pytest.approx(z.directional_derivative(seed_vector=[1, 0]), 0.0001) == 0.75
    assert pytest.approx(z.directional_derivative(seed_vector=[0, 1]), 0.0001) == 0.75
    assert z.identifier == 'tan^-1(x) + tan^-1(y)'


if __name__ == "__main__":
    pass
