from __future__ import annotations

import os
import sys
import math
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from typing import Iterable, Union, Type
from numbers import Number

from constants import _ALLOWED_TYPES, _SPECIAL_FUNCTIONS


class FabTensor(object):

    def __init__(self, value, derivative=None, identifier=""):
        """init method

        Parameters
        ----------
        value : number
            evalu
        derivative : _type_, optional
            _description_, by default None
        identifier : str, optional
            _description_, by default ""
        """
        self.value = value
        # derivative w.r.t all independent variables
        if derivative is None:
            derivative = 1.0
        if isinstance(derivative, _ALLOWED_TYPES):
            derivative = [derivative]
        self.derivative = np.array(derivative)
        self.identifier = identifier

    def __repr__(self):
        """Represents the FabTensor as a string

        Returns
        -------
        str
            _description_
        """
        return f"value: {self.value} derivative: {self.derivative} name: {self.identifier}"

    def __str__(self):
        return f"value: {self.value} derivative: {self.derivative} name: {self.identifier}"

    def __eq__(self, other):
        """Checks if value attribute of two `FabTensor` objects are equal.

        Parameters
        ----------
        other : _type_
            _description_

        Returns
        -------
        _type_
            _description_

        Raises
        ------
        TypeError
            _description_
        """
        if isinstance(other, FabTensor):
            return other.value == self.value
        elif isinstance(other, _ALLOWED_TYPES):
            return other == self.value
        else:
            raise TypeError(f"Cannot compare FabTensor and object of type {type(other)}")

    
    def __ne__(self, other):
        if isinstance(other, FabTensor):
            return other.value != self.value
        elif isinstance(other, _ALLOWED_TYPES):
            return other != self.value
        else:
            raise TypeError(f"Cannot compare FabTensor and object of type {type(other)}")

    def __lt__(self, other):
        if isinstance(other, FabTensor):
            return self.value < other.value
        elif isinstance(other, _ALLOWED_TYPES):
            return self.value < other
        else:
            raise TypeError(f"Cannot compare FabTensor and object of type {type(other)}")

    def __gt__(self, other):
        if isinstance(other, FabTensor):
            return self.value > other.value
        elif isinstance(other, _ALLOWED_TYPES):
            return self.value > other
        else:
            raise TypeError(f"Cannot compare FabTensor and object of type {type(other)}")

    def __le__(self, other):
        if isinstance(other, FabTensor):
            return self.value <= other.value
        elif isinstance(other, _ALLOWED_TYPES):
            return self.value <= other
        else:
            raise TypeError(f"Cannot compare FabTensor and object of type {type(other)}")

    def __ge__(self, other):
        if isinstance(other, FabTensor):
            return self.value >= other.value
        elif isinstance(other, _ALLOWED_TYPES):
            return self.value >= other
        else:
            raise TypeError(f"Cannot compare FabTensor and object of type {type(other)}")

    def __len__(self):
        if self.derivative is not None:
            return len(self.derivative)
        else:
            raise ValueError("derivative is not initialized yet!")
    
    def __neg__(self):
        return -1 * self

    def __add__(self, other):
        if isinstance(other, FabTensor):
            return FabTensor(self.value + other.value, derivative=self.derivative + other.derivative, identifier=f'{self.identifier} + {other.identifier}')
        elif isinstance(other, _ALLOWED_TYPES):
            return FabTensor(self.value + other, derivative=self.derivative, identifier=f'{self.identifier} + {other}')
        else:
            raise TypeError(f"addition not supported between types FabTensor and {type(other)}")

    def __radd__(self, other):
        if isinstance(other, FabTensor):
            return FabTensor(self.value + other.value, derivative=self.derivative + other.derivative, identifier=f'{other.identifier} + {self.identifier}')
        elif isinstance(other, _ALLOWED_TYPES):
            return FabTensor(self.value + other, derivative=self.derivative, identifier=f'{other} + {self.identifier}')
        else:
            raise TypeError(f"addition not supported between types FabTensor and {type(other)}")

    def __iadd__(self, other):
        return self + other
    
    def __sub__(self, other):
        if isinstance(other, FabTensor):
            return FabTensor(self.value - other.value, derivative=self.derivative - other.derivative, identifier=f'{self.identifier} - {other.identifier}')
        elif isinstance(other, _ALLOWED_TYPES):
            return FabTensor(self.value - other.value, derivative=self.derivative, identifier=f'{self.identifier} + {other.identifier}')
        else:
            raise TypeError(f"addition not supported between types FabTensor and {type(other)}")
    
    def __rsub__(self, other):
        return -1 * self + other
    
    def __isub__(self, other):
        return self - other
    
    def __mul__(self, other):
        if isinstance(other, FabTensor):
            return FabTensor(
                self.value * other.value,
                derivative=self.value * other.derivative + other.value * self.derivative,
                identifier=f'{self.identifier} * {other.identifier}',
            )
        elif isinstance(other, _ALLOWED_TYPES):
            if (other==1):
                identifier = self.identifier
            elif (other==-1):
                identifier=f'-{self.identifier}'
            else:
                identifier = f'{self.identifier} * {other}'

            return FabTensor(
                self.value * other,
                derivative=self.derivative * other,
                identifier=identifier
            )
        else:
            raise TypeError(f"Cannot multiple FabTensor with object of type {type(other)}")

    def __rmul__(self, other):
        if isinstance(other, FabTensor):
            return FabTensor(
                self.value * other.value,
                derivative=self.value * other.derivative + other.value * self.derivative,
                identifier=f'{other.identifier} * {self.identifier}',
            )
        elif isinstance(other, _ALLOWED_TYPES):
            if (other==1):
                identifier = self.identifier
            elif (other==-1):
                identifier=f'-{self.identifier}'
            else:
                identifier = f'{other} * {self.identifier}'
            return FabTensor(
                self.value * other,
                derivative=self.derivative * other,
                identifier=identifier
            )
        else:
            raise TypeError(f"Cannot multiple FabTensor with object of type {type(other)}")

    def __imul__(self, other):
        return self * other
    
    def __truediv__(self, other):
        try:
            return self * (other ** (-1))
        except ZeroDivisionError:
            raise ZeroDivisionError(f"Cannot divide FabTensor with {other}")
        except Exception as e:
            raise e
    
    def __rtruediv__(self, other):
        return (self ** -1) * other
    
    def __itruediv__(self, other):
        return self * (other ** (-1))

    def __pow__(self, other):
        if isinstance(other, FabTensor):
            value = self.value ** other.value
            derivative = (other.value * (self.value ** (other.value - 1)) * self.derivative) + ((self.value ** other.value) * np.log(self.value) * other.derivative)
            return FabTensor(
                value=value,
                derivative=derivative,
                identifier=f"{self.identifier}^{other.identifier}"
            )
        elif isinstance(other, _ALLOWED_TYPES):
            return FabTensor(
                value=self.value ** other,
                derivative=other * (self.value ** (other - 1)) * self.derivative,
                identifier=f"{self.identifier}^{other}" if other != -1 else f"1 / {self.identifier}"
            )
        else:
            raise TypeError(f"Cannot compute power of FabTensor with object of type {type(other)}")

    def __rpow__(self, other):
        if isinstance(other, _ALLOWED_TYPES):
            return FabTensor(
                value=other ** self.value,
                derivative=(other ** self.value) * np.log(other) * self.derivative,
                identifier=f"{other}^{self.identifier}"
            )
        else:
            raise TypeError(f"Cannot compute power of object of type {type(other)} with FabTensor")

    def directional_derivative(self, seed_vector: np.array):
        return np.array(seed_vector).dot(self.derivative)
