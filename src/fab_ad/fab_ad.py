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
        self.value = value
        # directional derivative
        self.derivative = derivative
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
            return FabTensor(self.value + other.value, derivative=self.value, identifier=f'{self.identifier} + constant')
        else:
            raise TypeError(f"addition not supported between types FabTensor and {type(other)}")

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        return self + other
    
    def __sub__(self, other):
        if isinstance(other, FabTensor):
            return FabTensor(self.value - other.value, derivative=self.derivative - other.derivative, identifier=f'{self.identifier} - {other.identifier}')
        elif isinstance(other, _ALLOWED_TYPES):
            return FabTensor(self.value - other.value, derivative=self.value, identifier=f'{self.identifier} + {other.identifier}')
        else:
            raise TypeError(f"addition not supported between types FabTensor and {type(other)}")
    
    def __rsub__(self, other):
        raise -1 * self + other
    
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
            return FabTensor(
                self.value * other,
                derivative=self.derivative * other,
                identifier=f'{self.identifier} * {other.identifier}'
            )
        else:
            raise TypeError(f"Cannot multiple FabTensor with object of type {type(other)}")

    def __rmul__(self, other):
        return self * other

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
            derivative = (other.value * (self.value ** (other.value - 1)) * self.derivative) + ((self.value ** other.value) * np.log(other.value) * other.derivative)
            return FabTensor(
                value=value,
                derivative=derivative,
                identifier=f"{self.identifier}^{other.identifier}"
            )
        elif isinstance(other, _ALLOWED_TYPES):
            return FabTensor(
                value=self.value ** other,
                derivative=other * (self.value ** (other - 1)) * self.derivative,
                identifier=f"{self.identifier}^{other}"
            )
        else:
            raise TypeError(f"Cannot compute power of FabTensor with object of type {type(other)}")

    def __ipow__(self, other):
        raise NotImplementedError

    def __rpow__(self, other):
        if isinstance(other, _ALLOWED_TYPES):
            return FabTensor(
                value=other ** self.value,
                derivative=(other ** self.value) * np.log(other) * self.derivative,
                identifier=f"{other}^{self.identifier}"
            )
        else:
            raise TypeError(f"Cannot compute power of object of type {type(other)} with FabTensor")

    def directional_derivative(self, direction=None):
        raise NotImplementedError

    @staticmethod
    def exp(tensor: Union[Type[FabTensor], Number]):
        if isinstance(tensor, FabTensor):
            return FabTensor(
                value=np.exp(tensor.value),
                derivative=np.exp(tensor.value) * tensor.derivative,
                identifier=f"e^({tensor.identifier})"
            )
        elif isinstance(tensor, _ALLOWED_TYPES):
            return FabTensor(value=np.exp(tensor), name="sqrt(input)")
        else:
            raise TypeError(f"Methods {_SPECIAL_FUNCTIONS} can be used on FabTensor objects and {_ALLOWED_TYPES} only!")

    @staticmethod
    def log(tensor: Union[Type[FabTensor], Number]):
        if isinstance(tensor, FabTensor):
            if tensor.value < 0:
                raise ValueError("Cannot compute logarithm for FabTensor with negative value!")
            return FabTensor(
                value=np.log(tensor.value),
                derivative=(1.0 / tensor.value) * tensor.derivative,
                identifier=f"log({tensor.identifier})"
            )
        elif isinstance(tensor, _ALLOWED_TYPES):
            return FabTensor(value=np.log(tensor), name="sqrt(input)")
        else:
            raise TypeError(f"Methods {_SPECIAL_FUNCTIONS} can be used on FabTensor objects and {_ALLOWED_TYPES} only!")

    @staticmethod
    def sin(tensor: Union[Type[FabTensor], Number]):
        if isinstance(tensor, FabTensor):
            return FabTensor(
                value=np.sin(tensor.value),
                derivative=np.cos(tensor.value) * tensor.derivative,
                identifier=f"sin({tensor.identifier})"
            )
        elif isinstance(tensor, _ALLOWED_TYPES):
            return FabTensor(value=np.sin(tensor), name="sin(input)")
        else:
            raise TypeError(f"Methods {_SPECIAL_FUNCTIONS} can be used on FabTensor objects and {_ALLOWED_TYPES} only!")

    @staticmethod
    def cos(tensor: Union[Type[FabTensor], Number]):
        if isinstance(tensor, FabTensor):
            return FabTensor(
                value=np.cos(tensor.value),
                derivative=-1 * np.sin(tensor.value) * tensor.derivative,
                identifier=f"cos({tensor.identifier})"
            )
        elif isinstance(tensor, _ALLOWED_TYPES):
            return FabTensor(value=np.cos(tensor), name="cos(input)")
        else:
            raise TypeError(f"Methods {_SPECIAL_FUNCTIONS} can be used on FabTensor objects and {_ALLOWED_TYPES} only!")

    @staticmethod
    def tan(tensor: Union[Type[FabTensor], Number]):
        if isinstance(tensor, FabTensor):
            return FabTensor(
                value=np.tan(tensor.value),
                derivative=(1 / (np.cos(tensor.value) ** 2)) * tensor.derivative,
                identifier=f"tan({tensor.identifier})"
            )
        elif isinstance(tensor, _ALLOWED_TYPES):
            return FabTensor(value=np.tan(tensor), name="tan(input)")
        else:
            raise TypeError(f"Methods {_SPECIAL_FUNCTIONS} can be used on FabTensor objects and {_ALLOWED_TYPES} only!")

    @staticmethod
    def arcsin(tensor: Union[Type[FabTensor], Number]):
        if isinstance(tensor, FabTensor):
            if not (-1 <= tensor.value <= 1):
                raise ValueError("Value of tensor out of range for function arcsin!")
            return FabTensor(
                value=np.arcsin(tensor.value),
                derivative=(1 / ((1 - tensor.value ** 2) ** 0.5)) * tensor.derivative,
                identifier=f"sin^{-1}({tensor.identifier})"
            )
        elif isinstance(tensor, _ALLOWED_TYPES):
            if not (-1 <= tensor.value <= 1):
                raise ValueError("Value of tensor out of range for function arcsin!")
            return FabTensor(value=np.arcsin(tensor), name="sin^{-1}(input)")
        else:
            raise TypeError(f"Methods {_SPECIAL_FUNCTIONS} can be used on FabTensor objects and {_ALLOWED_TYPES} only!")

    @staticmethod
    def arccos(tensor: Union[Type[FabTensor], Number]):
        if isinstance(tensor, FabTensor):
            if not (-1 <= tensor.value <= 1):
                raise ValueError("Value of tensor out of range for function arccos!")
            return FabTensor(
                value=np.arcsin(tensor.value),
                derivative=(-1 / ((1 - tensor.value ** 2) ** 0.5)) * tensor.derivative,
                identifier=f"cos^{-1}({tensor.identifier})"
            )
        elif isinstance(tensor, _ALLOWED_TYPES):
            if not (-1 <= tensor.value <= 1):
                raise ValueError("Value of tensor out of range for function arccos!")
            return FabTensor(value=np.arccos(tensor), name="cos^{-1}(input)")
        else:
            raise TypeError(f"Methods {_SPECIAL_FUNCTIONS} can be used on FabTensor objects and {_ALLOWED_TYPES} only!")

    @staticmethod
    def arctan(tensor: Union[Type[FabTensor], Number]):
        if isinstance(tensor, FabTensor):
            return FabTensor(
                value=np.arctan(tensor.value),
                derivative=(1 / (1 + tensor.value ** 2)) * tensor.derivative,
                identifier=f"tan^{-1}({tensor.identifier})"
            )
        elif isinstance(tensor, _ALLOWED_TYPES):
            if not (-1 <= tensor.value <= 1):
                raise ValueError("Value of tensor out of range for function arctan!")
            return FabTensor(value=np.arcsin(tensor), name="tan^{-1}(input)")
        else:
            raise TypeError(f"Methods {_SPECIAL_FUNCTIONS} can be used on FabTensor objects and {_ALLOWED_TYPES} only!")


def sqrt(tensor: Union[Type[FabTensor], Number]):
    if isinstance(tensor, FabTensor):
        if tensor.value < 0:
            raise ValueError("Cannot compute sqrt for FabTensor with negative value!")
        return FabTensor(
            value=tensor.value ** 0.5,
            derivative=0.5 * (tensor.value ** -0.5),
            identifier=f"sqrt({tensor.identifier})"
        )
    elif isinstance(tensor, _ALLOWED_TYPES):
        return FabTensor(value=tensor ** 0.5, name="sqrt(input)")
    else:
        raise TypeError(f"Methods {_SPECIAL_FUNCTIONS} can be used on FabTensor objects and {_ALLOWED_TYPES} only!")
