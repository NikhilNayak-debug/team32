import os
import math
import numpy as np


class AD(object):

    def __init__(self, val, order=2):
        pass

    def __repr__(self):
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError

    def __eq__(self, other):
        raise NotImplementedError
    
    def __ne__(self, other):
        raise NotImplementedError

    def __lt__(self, other):
        raise NotImplementedError

    def __gt__(self, other):
        raise NotImplementedError

    def __le__(self, other):
        raise NotImplementedError

    def __ge__(self, other):
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError
    
    def __neg__(self):
        raise NotImplementedError

    def __add__(self, other):
        raise NotImplementedError

    def __radd__(self, other):
        raise NotImplementedError

    def __iadd__(self, other):
        raise NotImplementedError
    
    def __sub__(self, other):
        raise NotImplementedError
    
    def __rsub__(self, other):
        raise NotImplementedError
    
    def __isub__(self, other):
        raise NotImplementedError
    
    def __mul__(self, other):
        raise NotImplementedError

    def __rmul__(self, other):
        raise NotImplementedError

    def __imul__(self, other):
        raise NotImplementedError    
    
    def __truediv__(self, other):
        raise NotImplementedError
    
    def __rtruediv__(self, other):
        raise NotImplementedError
    
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
