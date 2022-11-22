import sys, os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fab_ad import FabTensor


if __name__ == "__main__":
    x = FabTensor(value=3, derivative=0, identifier='x')
    y = FabTensor(value=-4, derivative=1, identifier='y')
    z = x ** 2 + y ** 2
    print(z)

    x = FabTensor(value=3, derivative=1, identifier='x')
    y = FabTensor(value=-4, derivative=0, identifier='y')
    z = x ** 2 + y ** 2
    print(z)

