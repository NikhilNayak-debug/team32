from fab_ad import FabTensor
import numpy as np


if __name__ == "__main__":
    x = FabTensor(value=3, derivative=np.array([1, 0]), identifier='x')
    y = FabTensor(value=-4, derivative=np.array([0, 1]), identifier='y')
    seed_vector = np.array([0, 1])
    z = x * y
    print(z)
    print("gradient: ", z.directional_derivative(seed_vector))

    x = FabTensor(value=3, derivative=1, identifier='x')
    y = FabTensor(value=-4, derivative=0, identifier='y')
    z = x ** 2 + y ** 2
    print(z)

