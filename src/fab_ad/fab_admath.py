import math
import numbers
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
from fab_ad.fab_ad import FabTensor
from fab_ad.constants import _ALLOWED_TYPES, _SPECIAL_FUNCTIONS


def sqrt(tensor):
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


def exp(tensor):
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


def log(tensor):
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


def sin(tensor):
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


def cos(tensor):
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


def tan(tensor):
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


def arcsin(tensor):
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


def arccos(tensor):
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


def arctan(tensor):
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