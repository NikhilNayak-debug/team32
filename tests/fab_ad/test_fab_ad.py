# 
# test_AD.py
# Created at 2:15 PM 11/22/22 by Saket Joshi
#
# This test file contains all the test cases for fab_ad.py

import sys
import os

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src/fab_ad')))

from fab_ad import FabTensor


def test_fabtensor_sanity():
    x = FabTensor(value=3, derivative=0, identifier='x')
    y = FabTensor(value=-4, derivative=1, identifier='y')
    z = x ** 2 + y ** 2
    assert z.value == 25
    assert z.derivative == -8
    assert z.identifier == 'x^2 + y^2'


def test_fabtensor_len():
    x = FabTensor(value=3, derivative=[1, 0], identifier='x')
    y = FabTensor(value=-4, derivative=[0, 1], identifier='y')
    z = len(x)
    assert z == 2


def test_fabtensor_neg():
    x = FabTensor(value=3, derivative=0, identifier='x')
    y = FabTensor(value=-4, derivative=1, identifier='y')
    z = -x * y
    assert z.value == 12
    assert z.derivative == 4
    assert z.identifier == '-x * y'

def test_fabtensor_add():
    x = FabTensor(value=3, derivative=0, identifier='x')
    y = FabTensor(value=-4, derivative=1, identifier='y')
    z = x + y
    assert z.value == -1
    assert z.derivative == 1
    assert z.identifier == 'x + y'

def test_fabtensor_radd():
    x = FabTensor(value=3, derivative=0, identifier='x')
    y = FabTensor(value=-4, derivative=1, identifier='y')
    z = 1 + x
    assert z.value == 4
    assert z.derivative == 0
    assert z.identifier == '1 + x'
def test_fabtensor_iadd():
    x = FabTensor(value=3, derivative=0, identifier='x')
    y = FabTensor(value=-4, derivative=1, identifier='y')
    x += y
    assert x.value == -1
    assert x.derivative == 1
    assert x.identifier == 'x + y'

def test_fabtensor_sub():
    x = FabTensor(value=3, derivative=0, identifier='x')
    y = FabTensor(value=-4, derivative=1, identifier='y')
    z = x - y
    assert z.value == 7
    assert z.derivative == -1
    assert z.identifier == 'x - y'

def test_fabtensor_rsub():
    x = FabTensor(value=3, derivative=0, identifier='x')
    y = FabTensor(value=-4, derivative=1, identifier='y')
    z = 1 - x
    assert z.value == -2
    assert z.derivative == 0
    assert z.identifier == '1 - x'

def test_fabtensor_isub():
    x = FabTensor(value=3, derivative=0, identifier='x')
    y = FabTensor(value=-4, derivative=1, identifier='y')
    x -= y
    assert x.value == 7
    assert x.derivative == -1
    assert x.identifier == 'x - y'

def test_fabtensor_mul():
    x = FabTensor(value=3, derivative=0, identifier='x')
    y = FabTensor(value=-4, derivative=1, identifier='y')
    z = x * y
    assert z.value == -12
    assert z.derivative == 3
    assert z.identifier == 'x * y'

def test_fabtensor_rmul():
    x = FabTensor(value=3, derivative=0, identifier='x')
    y = FabTensor(value=-4, derivative=1, identifier='y')
    z = 1 * x
    assert z.value == 3
    assert z.derivative == 0
    assert z.identifier == '1 * x'

def test_fabtensor_imul():
    x = FabTensor(value=3, derivative=0, identifier='x')
    y = FabTensor(value=-4, derivative=1, identifier='y')
    x *= y
    assert x.value == -12
    assert x.derivative == 3
    assert x.identifier == 'x * y'

def test_fabtensor_truediv():
    x = FabTensor(value=3, derivative=0, identifier='x')
    y = FabTensor(value=-4, derivative=1, identifier='y')
    z = x / y
    assert z.value == -0.75
    assert z.derivative == -0.1875
    assert z.identifier == 'x * y^-1'

def test_fabtensor_rtruedeiv():
    x = FabTensor(value=3, derivative=0, identifier='x')
    y = FabTensor(value=-4, derivative=1, identifier='y')
    z = 1 / x
    assert z.value == 0.3333333333333333
    assert z.derivative == 0
    assert z.identifier == '1 / x'

def test_fabtensor_itruediv():
    x = FabTensor(value=3, derivative=0, identifier='x')
    y = FabTensor(value=-4, derivative=1, identifier='y')
    x /= y
    assert x.value == -0.75
    assert x.derivative == -0.1875
    assert x.identifier == 'x * y^-1'
def test_fabtensor_pow():
    x = FabTensor(value=3, derivative=0, identifier='x')
    y = FabTensor(value=-4, derivative=1, identifier='y')
    z = x ** y
    assert z.value == 0.012345679012345678
    assert z.derivative == -0.0002469135802469136
    assert z.identifier == 'x^y'

def test_fabtensor_ipow():
    x = FabTensor(value=3, derivative=0, identifier='x')
    y = FabTensor(value=-4, derivative=1, identifier='y')
    x **= y
    assert x.value == 0.000244140625
    assert x.derivative == -0.000244140625
    assert x.identifier == 'x^y'

def test_fabtensor_rpow():
    x = FabTensor(value=3, derivative=0, identifier='x')
    y = FabTensor(value=-4, derivative=1, identifier='y')
    z = 1 ** x
    assert z.value == 1
    assert z.derivative == 0
    assert z.identifier == '1^x'

def test_fabtensor_directional_derivative():
    x = FabTensor(value=3, derivative=0, identifier='x')
    y = FabTensor(value=-4, derivative=1, identifier='y')
    z = x * y
    assert z.directional_derivative(1) == -4
    assert z.directional_derivative(-1) == 4
    assert z.directional_derivative(0) == 0

def test_fabtensor_sqrt():
    tensor = FabTensor(value=4, derivative=1, identifier='x')
    x = FabTensor(value=4, derivative=0, identifier='x')
    y = FabTensor(value=9, derivative=
    1, identifier='y')
    z = x.sqrt(tensor) + y.sqrt(tensor)
    assert pytest.approx(z.value, 0.01) == 4.0
    assert z.derivative == 0.5
    assert z.identifier == 'sqrt(x) + sqrt(x)'

def test_fabtensor_exp():
    tensor = FabTensor(value=4, derivative=1, identifier='x')
    x = FabTensor(value=4, derivative=0, identifier='x')
    y = FabTensor(value=9, derivative=1, identifier='y')
    z = x.exp(tensor) + y.exp(tensor)
    assert pytest.approx(z.value, 0.01) == 109.19630006628847
    assert z.derivative == 109.19630006628847
    assert z.identifier == 'e^(x) + e^(x)'

def test_fabtensor_log():
    tensor = FabTensor(value=4, derivative=1, identifier='x')
    x = FabTensor(value=4, derivative=0, identifier='x')
    y = FabTensor(value=9, derivative=1, identifier='y')
    z = x.log(tensor) + y.log(tensor)
    assert pytest.approx(z.value, 0.01) == 2.772588722239781
    assert z.derivative == 0.5
    assert z.identifier == 'log(x) + log(x)'

def test_fabtensor_sin():
    tensor = FabTensor(value=4, derivative=1, identifier='x')
    x = FabTensor(value=4, derivative=0, identifier='x')
    y = FabTensor(value=9, derivative=1, identifier='y')
    z = x.sin(tensor) + y.sin(tensor)
    assert pytest.approx(z.value, 0.01) == -1.5136049906158566
    assert z.derivative == -1.3072872417272239
    assert z.identifier == 'sin(x) + sin(x)'

def test_fabtensor_cos():
    tensor = FabTensor(value=4, derivative=1, identifier='x')
    x = FabTensor(value=4, derivative=0, identifier='x')
    y = FabTensor(value=9, derivative=1, identifier='y')
    z = x.cos(tensor) + y.cos(tensor)
    assert pytest.approx(z.value, 0.01) == -1.3072872417272239
    assert z.derivative == 1.5136049906158566
    assert z.identifier == 'cos(x) + cos(x)'

def test_fabtensor_tan():
    tensor = FabTensor(value=4, derivative=1, identifier='x')
    x = FabTensor(value=4, derivative=0, identifier='x')
    y = FabTensor(value=9, derivative=1, identifier='y')
    z = x.tan(tensor) + y.tan(tensor)
    assert z.value == 2.315642564699155
    assert z.derivative == 4.68110024372324
    assert z.identifier == 'tan(x) + tan(x)'

def test_fabtensor_asin():
    x = FabTensor(value=0.5, derivative=0, identifier='x')
    y = FabTensor(value=0.75, derivative=1, identifier='y')
    tensor = FabTensor(value=0.5, derivative=1, identifier='x')
    z = x.arcsin(tensor) + y.arcsin(tensor)
    assert pytest.approx(z.value, 0.01) == 1.0471975511965979
    assert z.derivative == 2.3094010767585034
    assert z.identifier == 'sin^-1(x) + sin^-1(x)'

def test_fabtensor_arccos():
    tensor = FabTensor(value=0.5, derivative=1, identifier='x')
    x = FabTensor(value=0.5, derivative=0, identifier='x')
    y = FabTensor(value=0.75, derivative=1, identifier='y')
    z = x.arccos(tensor) + y.arccos(tensor)
    assert pytest.approx(z.value, 0.01) == 1.047
    assert z.derivative == -2.3094010767585034
    assert z.identifier == 'cos^-1(x) + cos^-1(x)'

def test_fabtensor_arctan():
    tensor = FabTensor(value=0.5, derivative=1, identifier='x')
    x = FabTensor(value=0.5, derivative=0, identifier='x')
    y = FabTensor(value=0.75, derivative=1, identifier='y')
    z = x.arctan(tensor) + y.arctan(tensor)
    assert pytest.approx(z.value, 0.01) == 0.9272952180016123
    assert z.derivative == 1.6
    assert z.identifier == 'tan^-1(x) + tan^-1(x)'

if __name__ == "__main__":
    pass
