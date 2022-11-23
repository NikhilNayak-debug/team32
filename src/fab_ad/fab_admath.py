import math
import numbers
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
from fab_ad import FabTensor
from constants import _ALLOWED_TYPES, _SPECIAL_FUNCTIONS


def sqrt(tensor):
    """square root of tensor with updated value and derivative

    Parameters
    ----------
    tensor : FabTensor

    Returns
    -------
    FabTensor
        square root of tensor with updated value and derivative
    
    """
    if isinstance(tensor, FabTensor):
        if tensor.value < 0:
            raise ValueError("Cannot compute sqrt for FabTensor with negative value!")
        return FabTensor(
            value=tensor.value ** 0.5,
            derivative=0.5 * (tensor.value ** -0.5) * tensor.derivative,
            identifier=f"sqrt({tensor.identifier})"
        )
    elif isinstance(tensor, _ALLOWED_TYPES):
        if tensor < 0.0:
            raise ValueError("Value of tensor out of range for function sqrt!")
        return FabTensor(value=tensor ** 0.5, derivative = 0, identifier="sqrt(input)")
    else:
        raise TypeError(f"Methods {_SPECIAL_FUNCTIONS} can be used on FabTensor objects and {_ALLOWED_TYPES} only!")


def exp(tensor):
    """exponential of tensor with updated value and derivative

    Parameters
    ----------
    tensor : FabTensor

    Returns
    -------
    FabTensor
        exponential of tensor with updated value and derivative
    
    """
    if isinstance(tensor, FabTensor):
        return FabTensor(
            value=np.exp(tensor.value),
            derivative=np.exp(tensor.value) * tensor.derivative,
            identifier=f"e^({tensor.identifier})"
        )
    elif isinstance(tensor, _ALLOWED_TYPES):
        return FabTensor(value=np.exp(tensor), derivative = 0, identifier="sqrt(input)")
    else:
        raise TypeError(f"Methods {_SPECIAL_FUNCTIONS} can be used on FabTensor objects and {_ALLOWED_TYPES} only!")


def log(tensor):
    """natural log of tensor with updated value and derivative

    Parameters
    ----------
    tensor : FabTensor

    Returns
    -------
    FabTensor
        natural log of tensor with updated value and derivative
    """
    if isinstance(tensor, FabTensor):
        if tensor.value < 0:
            raise ValueError("Cannot compute logarithm for FabTensor with negative value!")
        return FabTensor(
            value=np.log(tensor.value),
            derivative=(1.0 / tensor.value) * tensor.derivative,
            identifier=f"log({tensor.identifier})"
        )
    elif isinstance(tensor, _ALLOWED_TYPES):
        if tensor < 0.0:
            raise ValueError("Value of tensor out of range for function log!")
        return FabTensor(value=np.log(tensor), derivative = 0, identifier="sqrt(input)")
    else:
        raise TypeError(f"Methods {_SPECIAL_FUNCTIONS} can be used on FabTensor objects and {_ALLOWED_TYPES} only!")


def sin(tensor):
    """sin of tensor with updated value and derivative

    Parameters
    ----------
    tensor : FabTensor

    Returns
    -------
    FabTensor
        sin of tensor with updated value and derivative
    """
    if isinstance(tensor, FabTensor):
        return FabTensor(
            value=np.sin(tensor.value),
            derivative=np.cos(tensor.value) * tensor.derivative,
            identifier=f"sin({tensor.identifier})"
        )
    elif isinstance(tensor, _ALLOWED_TYPES):
        return FabTensor(value=np.sin(tensor), derivative = 0, identifier="sin(input)")
    else:
        raise TypeError(f"Methods {_SPECIAL_FUNCTIONS} can be used on FabTensor objects and {_ALLOWED_TYPES} only!")


def cos(tensor):
    """cos of tensor with updated value and derivative

    Parameters
    ----------
    tensor : FabTensor

    Returns
    -------
    FabTensor
        cos of tensor with updated value and derivative
    """
    if isinstance(tensor, FabTensor):
        return FabTensor(
            value=np.cos(tensor.value),
            derivative=-1 * np.sin(tensor.value) * tensor.derivative,
            identifier=f"cos({tensor.identifier})"
        )
    elif isinstance(tensor, _ALLOWED_TYPES):
        return FabTensor(value=np.cos(tensor), derivative = 0, identifier="cos(input)")
    else:
        raise TypeError(f"Methods {_SPECIAL_FUNCTIONS} can be used on FabTensor objects and {_ALLOWED_TYPES} only!")


def tan(tensor):
    """tan of tensor with updated value and derivative

    Parameters
    ----------
    tensor : FabTensor

    Returns
    -------
    FabTensor
        tan of tensor with updated value and derivative
    """
    if isinstance(tensor, FabTensor):
        return FabTensor(
            value=np.tan(tensor.value),
            derivative=(1 / (np.cos(tensor.value) ** 2)) * tensor.derivative,
            identifier=f"tan({tensor.identifier})"
        )
    elif isinstance(tensor, _ALLOWED_TYPES):
        return FabTensor(value=np.tan(tensor), derivative = 0, identifier="tan(input)")
    else:
        raise TypeError(f"Methods {_SPECIAL_FUNCTIONS} can be used on FabTensor objects and {_ALLOWED_TYPES} only!")


def arcsin(tensor):
    """sin inverse of tensor with updated value and derivative

    Parameters
    ----------
    tensor : FabTensor

    Returns
    -------
    FabTensor
        sin inverse of tensor with updated value and derivative
    """
    if isinstance(tensor, FabTensor):
        if not (-1 <= tensor.value <= 1):
            raise ValueError("Value of tensor out of range for function arcsin!")
        return FabTensor(
            value=np.arcsin(tensor.value),
            derivative=(1 / ((1 - tensor.value ** 2) ** 0.5)) * tensor.derivative,
            identifier=f"sin^{-1}({tensor.identifier})"
        )
    elif isinstance(tensor, _ALLOWED_TYPES):
        if not (-1 <= tensor <= 1):
            raise ValueError("Value of tensor out of range for function arcsin!")
        return FabTensor(value=np.arcsin(tensor), derivative = 0, identifier="sin^{-1}(input)")
    else:
        raise TypeError(f"Methods {_SPECIAL_FUNCTIONS} can be used on FabTensor objects and {_ALLOWED_TYPES} only!")


def arccos(tensor):
    """cos inverse of tensor with updated value and derivative

    Parameters
    ----------
    tensor : FabTensor

    Returns
    -------
    FabTensor
        cos inverse of tensor with updated value and derivative
    """
    if isinstance(tensor, FabTensor):
        if not (-1 <= tensor.value <= 1):
            raise ValueError("Value of tensor out of range for function arccos!")
        return FabTensor(
            value=np.arcsin(tensor.value),
            derivative=(-1 / ((1 - tensor.value ** 2) ** 0.5)) * tensor.derivative,
            identifier=f"cos^{-1}({tensor.identifier})"
        )
    elif isinstance(tensor, _ALLOWED_TYPES):
        if not (-1 <= tensor <= 1):
            raise ValueError("Value of tensor out of range for function arccos!")
        return FabTensor(value=np.arccos(tensor), derivative = 0, identifier="cos^{-1}(input)")
    else:
        raise TypeError(f"Methods {_SPECIAL_FUNCTIONS} can be used on FabTensor objects and {_ALLOWED_TYPES} only!")


def arctan(tensor):
    """tan inverse of tensor with updated value and derivative

    Parameters
    ----------
    tensor : FabTensor

    Returns
    -------
    FabTensor
        tan inverse of tensor with updated value and derivative
    """
    if isinstance(tensor, FabTensor):
        return FabTensor(
            value=np.arctan(tensor.value),
            derivative=(1 / (1 + tensor.value ** 2)) * tensor.derivative,
            identifier=f"tan^{-1}({tensor.identifier})"
        )
    elif isinstance(tensor, _ALLOWED_TYPES):
        return FabTensor(value=np.arctan(tensor), derivative = 0, identifier="tan^{-1}(input)")
    else:
        raise TypeError(f"Methods {_SPECIAL_FUNCTIONS} can be used on FabTensor objects and {_ALLOWED_TYPES} only!")


def sigmoid(tensor):
    """sigmoid of tensor with updated value and derivative

    Parameters
    ----------
    tensor : FabTensor

    Returns
    -------
    FabTensor
        sigmoid of tensor with updated value and derivative
    
    """
    if isinstance(tensor, FabTensor):
        return 1/(1 + exp(-tensor))
    elif isinstance(tensor, _ALLOWED_TYPES):
        return FabTensor(value=1/(1 + np.exp(-tensor)), derivative = 0, identifier=f"sigmoid({tensor})")
    else:
        raise TypeError(f"Methods {_SPECIAL_FUNCTIONS} can be used on FabTensor objects and {_ALLOWED_TYPES} only!")