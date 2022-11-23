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
            evaluated function value
        derivative : array, optional
            derivative w.r.t all seed vectors, by default None
        identifier : str, optional
            function expression, by default ""
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
            FabTensor as a string
        """
        return f"value: {self.value} derivative: {self.derivative} name: {self.identifier}"

    def __str__(self):
        """Represents the FabTensor as a string

        Returns
        -------
        str
            FabTensor as a string
        """
        return f"value: {self.value} derivative: {self.derivative} name: {self.identifier}"

    def __eq__(self, other):
        """Checks if value attribute of two `FabTensor` objects are equal.

        Parameters
        ----------
        other : FabTensor

        Returns
        -------
        boolean
            if value attribute of two `FabTensor` objects are equal
        """
        if isinstance(other, FabTensor):
            return other.value == self.value
        elif isinstance(other, _ALLOWED_TYPES):
            return other == self.value
        else:
            raise TypeError(f"Cannot compare FabTensor and object of type {type(other)}")

    
    def __ne__(self, other):
        """Checks if value attribute of two `FabTensor` objects are not equal.

        Parameters
        ----------
        other : FabTensor

        Returns
        -------
        boolean
            if value attribute of two `FabTensor` objects are not equal
        
        """
        if isinstance(other, FabTensor):
            return other.value != self.value
        elif isinstance(other, _ALLOWED_TYPES):
            return other != self.value
        else:
            raise TypeError(f"Cannot compare FabTensor and object of type {type(other)}")

    def __lt__(self, other):
        """Checks if value attribute of self is less than other `FabTensor` object

        Parameters
        ----------
        other : FabTensor

        Returns
        -------
        boolean
            if value attribute of self is less than other `FabTensor` object
        
        """
        if isinstance(other, FabTensor):
            return self.value < other.value
        elif isinstance(other, _ALLOWED_TYPES):
            return self.value < other
        else:
            raise TypeError(f"Cannot compare FabTensor and object of type {type(other)}")

    def __gt__(self, other):
        """Checks if value attribute of self is greater than other `FabTensor` object

        Parameters
        ----------
        other : FabTensor

        Returns
        -------
        boolean
            if value attribute of self is greater than other `FabTensor` object
        
        """
        if isinstance(other, FabTensor):
            return self.value > other.value
        elif isinstance(other, _ALLOWED_TYPES):
            return self.value > other
        else:
            raise TypeError(f"Cannot compare FabTensor and object of type {type(other)}")

    def __le__(self, other):
        """Checks if value attribute of self is less than or equal to other `FabTensor` object

        Parameters
        ----------
        other : FabTensor

        Returns
        -------
        boolean
            if value attribute of self is less than or equal to other `FabTensor` object
        
        """
        if isinstance(other, FabTensor):
            return self.value <= other.value
        elif isinstance(other, _ALLOWED_TYPES):
            return self.value <= other
        else:
            raise TypeError(f"Cannot compare FabTensor and object of type {type(other)}")

    def __ge__(self, other):
        """Checks if value attribute of self is greater than or equal to other `FabTensor` object

        Parameters
        ----------
        other : FabTensor

        Returns
        -------
        boolean
            if value attribute of self is greater than or equal to other `FabTensor` object
        
        """
        if isinstance(other, FabTensor):
            return self.value >= other.value
        elif isinstance(other, _ALLOWED_TYPES):
            return self.value >= other
        else:
            raise TypeError(f"Cannot compare FabTensor and object of type {type(other)}")

    def __len__(self):
        """return length of derivative array

        Returns
        -------
        array
            length of derivative array
        
        """
        if self.derivative is not None:
            return len(self.derivative)
        else:
            raise ValueError("derivative is not initialized yet!")
    
    def __neg__(self):
        """negation of `FabTensor` object

        Returns
        -------
        FabTensor
            negation of `FabTensor` object
        """
        return -1 * self

    def __add__(self, other):
        """sum of two `FabTensor` objects

        Parameters
        ----------
        other : FabTensor

        Returns
        -------
        FabTensor
            sum of two `FabTensor` objects
        
        """
        if isinstance(other, FabTensor):
            return FabTensor(self.value + other.value, derivative=self.derivative + other.derivative, identifier=f'{self.identifier} + {other.identifier}')
        elif isinstance(other, _ALLOWED_TYPES):
            return FabTensor(self.value + other, derivative=self.derivative, identifier=f'{self.identifier} + {other}')
        else:
            raise TypeError(f"addition not supported between types FabTensor and {type(other)}")

    def __radd__(self, other):
        """sum of two `FabTensor` objects

        Parameters
        ----------
        other : FabTensor

        Returns
        -------
        FabTensor
            sum of two `FabTensor` objects
        
        """
        if isinstance(other, FabTensor):
            return FabTensor(self.value + other.value, derivative=self.derivative + other.derivative, identifier=f'{other.identifier} + {self.identifier}')
        elif isinstance(other, _ALLOWED_TYPES):
            return FabTensor(self.value + other, derivative=self.derivative, identifier=f'{other} + {self.identifier}')
        else:
            raise TypeError(f"addition not supported between types FabTensor and {type(other)}")

    def __iadd__(self, other):
        """sum of two `FabTensor` objects

        Parameters
        ----------
        other : FabTensor

        Returns
        -------
        FabTensor
            sum of two `FabTensor` objects
        """
        return self + other
    
    def __sub__(self, other):
        """difference of two `FabTensor` objects

        Parameters
        ----------
        other : FabTensor

        Returns
        -------
        FabTensor
            difference of two `FabTensor` objects
        
        """
        if isinstance(other, FabTensor):
            return FabTensor(self.value - other.value, derivative=self.derivative - other.derivative, identifier=f'{self.identifier} - {other.identifier}')
        elif isinstance(other, _ALLOWED_TYPES):
            return FabTensor(self.value - other.value, derivative=self.derivative, identifier=f'{self.identifier} + {other.identifier}')
        else:
            raise TypeError(f"addition not supported between types FabTensor and {type(other)}")
    
    def __rsub__(self, other):
        """difference of two `FabTensor` objects

        Parameters
        ----------
        other : FabTensor

        Returns
        -------
        FabTensor
            difference of two `FabTensor` objects
        """
        return -1 * self + other
    
    def __isub__(self, other):
        """difference of two `FabTensor` objects

        Parameters
        ----------
        other : FabTensor

        Returns
        -------
        FabTensor
            difference of two `FabTensor` objects
        """
        return self - other
    
    def __mul__(self, other):
        """product of two `FabTensor` objects

        Parameters
        ----------
        other : FabTensor

        Returns
        -------
        FabTensor
            product of two `FabTensor` objects
        
        """
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
        """product of two `FabTensor` objects

        Parameters
        ----------
        other : FabTensor

        Returns
        -------
        FabTensor
            product of two `FabTensor` objects
        """
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
        """product of two `FabTensor` objects

        Parameters
        ----------
        other : FabTensor

        Returns
        -------
        FabTensor
            product of two `FabTensor` objects
        """
        return self * other
    
    def __truediv__(self, other):
        """division of two `FabTensor` objects

        Parameters
        ----------
        other : FabTensor

        Returns
        -------
        FabTensor
            division of two `FabTensor` objects
        """
        try:
            return self * (other ** (-1))
        except ZeroDivisionError:
            raise ZeroDivisionError(f"Cannot divide FabTensor with {other}")
        except Exception as e:
            raise e
    
    def __rtruediv__(self, other):
        """division of two `FabTensor` objects

        Parameters
        ----------
        other : FabTensor

        Returns
        -------
        FabTensor
            division of two `FabTensor` objects
        """
        return (self ** -1) * other
    
    def __itruediv__(self, other):
        """division of two `FabTensor` objects

        Parameters
        ----------
        other : FabTensor

        Returns
        -------
        FabTensor
            division of two `FabTensor` objects
        """
        return self * (other ** (-1))

    def __pow__(self, other):
        """power of two `FabTensor` objects

        Parameters
        ----------
        other : FabTensor

        Returns
        -------
        FabTensor
            power of two `FabTensor` objects
        """
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
        """power of two `FabTensor` objects

        Parameters
        ----------
        other : FabTensor

        Returns
        -------
        FabTensor
            power of two `FabTensor` objects
        """
        if isinstance(other, _ALLOWED_TYPES):
            return FabTensor(
                value=other ** self.value,
                derivative=(other ** self.value) * np.log(other) * self.derivative,
                identifier=f"{other}^{self.identifier}"
            )
        else:
            raise TypeError(f"Cannot compute power of object of type {type(other)} with FabTensor")

    def directional_derivative(self, seed_vector: np.array):
        """directional derivative w.r.t alls eed vectors

        Parameters
        ----------
        seed_vector : np.array
            array of seed vectors or all the independent variables

        Returns
        -------
        number
            directional derivative w.r.t given seed vectors
        """
        return np.array(seed_vector).dot(self.derivative)
