import os
import math
import numpy as np
from .constants import _ALLOWED_TYPES


class FabTensor(object):

    def __init__(self, value, derivative=None):
        self.value = value
        self.derivative = derivative

    def __repr__(self):
        """Represents the FabTensor as a string

        Returns
        -------
        str
            _description_
        """
        return f"value: {self.value} derivative: {self.derivative}"

    def __str__(self):
        return f"value: {self.value} derivative: {self.derivative}"

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
            return FabTensor(self.value + other.value, derivative=self.derivative + other.derivative)
        elif isinstance(other, _ALLOWED_TYPES):
            return FabTensor(self.value + other.value, derivative=self.value)
        else:
            raise TypeError(f"addition not supported between types FabTensor and {type(other)}")

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        return self + other
    
    def __sub__(self, other):
        if isinstance(other, FabTensor):
            return FabTensor(self.value - other.value, derivative=self.derivative - other.derivative)
        elif isinstance(other, _ALLOWED_TYPES):
            return FabTensor(self.value - other.value, derivative=self.value)
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
                derivative=self.value * other.derivative + other.value * self.derivative
            )
        elif isinstance(other, _ALLOWED_TYPES):
            return FabTensor(
                self.value * other,
                derivative=self.derivative * other
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
        raise NotImplementedError  

    def __pow__(self, other):
        raise NotImplementedError

    def __ipow__(self, other):
        raise NotImplementedError

    def __rpow__(self, other):
        raise NotImplementedError 

    def directional_derivative(self, direction=None):
        raise NotImplementedError

    @staticmethod
    def sqrt(tensor):
        raise NotImplementedError

    @staticmethod
    def exp(tensor):
        raise NotImplementedError

    @staticmethod
    def log(tensor):
        raise NotImplementedError

    @staticmethod
    def sin(tensor):
        raise NotImplementedError

    @staticmethod
    def cos(tensor):
        raise NotImplementedError

    @staticmethod
    def tan(tensor):
        raise NotImplementedError

    @staticmethod
    def arcsin(tensor):
        raise NotImplementedError

    @staticmethod
    def arccos(tensor):
        raise NotImplementedError

    @staticmethod
    def arctan(tensor):
        raise NotImplementedError
