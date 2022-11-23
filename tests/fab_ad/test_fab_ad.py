# test_AD.py
# Created at 2:15 PM 11/22/22 by Saket Joshi
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
    x = FabTensor(value=3, identifier='x')
    assert x.derivative == 1.0


def test_fabtensor_repr():
    x = FabTensor(value=3, derivative=0, identifier='x')
    assert repr(x) == "value: 3 derivative: [0] name: x"


def test_fabtensor_str():
    x = FabTensor(value=3, derivative=0, identifier='x')
    assert str(x) == "value: 3 derivative: [0] name: x"


def test_fabtensor_equal():
    x = FabTensor(value=3, derivative=0, identifier='x')
    y = FabTensor(value=3, derivative=-1, identifier='y')
    assert x == y
    assert x == 3


def test_fabtensor_not_equal():
    x = FabTensor(value=3, derivative=0, identifier='x')
    y = FabTensor(value=4, derivative=0, identifier='x')
    assert x != y
    assert x != 4


def test_fabtensor_inequalities():
    x = FabTensor(value=3, derivative=0, identifier='x')
    y = FabTensor(value=4, derivative=0, identifier='x')
    assert x < y
    assert x < 4
    assert x <= y
    assert x <= 4
    assert y > x
    assert y > 3
    assert y >= x
    assert y >= 3


def test_fabtensor_len():
    x = FabTensor(value=3, derivative=[1, 0], identifier='x')
    z = len(x)
    assert z == 2


def test_fabtensor_neg():
    x = FabTensor(value=3, derivative=1, identifier='x')
    z = -x
    print(f"z: {z}")
    assert z.value == -3
    assert z.derivative[0] == -1

def test_fabtensor_add():
    x = FabTensor(value=3, derivative=0, identifier='x')
    y = FabTensor(value=-4, derivative=1, identifier='y')
    z = x + y
    assert z.value == -1
    assert z.derivative == 1
    assert z.identifier == 'x + y'

    z = x + 5
    assert z.value == 8
    assert z.derivative == x.derivative
    assert z.identifier == 'x + 5'


def test_fabtensor_radd():
    x = FabTensor(value=3, derivative=0, identifier='x')
    y = FabTensor(value=-4, derivative=1, identifier='y')
    z = 1 + x
    assert z.value == 4
    assert z.derivative == 0
    assert z.identifier == '1 + x'

    z = 5 + x
    assert z.value == 8
    assert z.derivative == x.derivative
    assert z.identifier == '5 + x'


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

    z = x - 5
    assert z.value == -2
    assert z.derivative == x.derivative
    assert z.identifier == 'x - 5'


def test_fabtensor_rsub():
    x = FabTensor(value=3, derivative=0, identifier='x')
    y = FabTensor(value=-4, derivative=1, identifier='y')
    z = 1 - x
    assert z.value == -2
    assert z.derivative == 0
    assert z.identifier == '-x + 1'

    z = 5 - x
    assert z.value == 2
    assert z.derivative == -1 * x.derivative
    assert z.identifier == '-x + 5'


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
    assert z.identifier == 'x'

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
    assert z.identifier == 'x * 1 / y'

def test_fabtensor_rtruedeiv():
    x = FabTensor(value=3, derivative=0, identifier='x')
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
    assert x.identifier == 'x * 1 / y'


def test_fabtensor_pow():
    x = FabTensor(value=3, derivative=[1, 0], identifier='x')
    y = FabTensor(value=4, derivative=[0, 1], identifier='y')
    z = x ** y
    assert z.value == 81
    print(z)
    assert z.directional_derivative(seed_vector=[1, 0]) == 108.0
    assert z.directional_derivative(seed_vector=[0, 1]) == 88.9875953821169
    assert z.identifier == 'x^y'


def test_fabtensor_rpow():
    x = FabTensor(value=3, derivative=0, identifier='x')
    y = FabTensor(value=-4, derivative=1, identifier='y')
    z = 1 ** x
    assert z.value == 1
    assert z.derivative == 0
    assert z.identifier == '1^x'


def test_fabtensor_directional_derivative():
    x = FabTensor(value=3, derivative=[1, 0], identifier='x')
    y = FabTensor(value=-4, derivative=[0, 1], identifier='y')
    z = x * y
    assert z.directional_derivative(seed_vector=[1, 0]) == -4
    assert z.directional_derivative(seed_vector=[0, 1]) == 3


if __name__ == "__main__":
    pass
