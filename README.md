[![.github/workflows/test.yml](https://code.harvard.edu/CS107/team32/actions/workflows/test.yml/badge.svg)](https://code.harvard.edu/CS107/team32/actions/workflows/test.yml)
[![.github/workflows/coverage.yml](https://code.harvard.edu/CS107/team32/actions/workflows/coverage.yml/badge.svg)](https://code.harvard.edu/CS107/team32/actions/workflows/coverage.yml)

# team32
CS107/AC207 Project

# Introduction
Differentiation is defined as the process of finding the 
gradients/derivatives of a particular function in hand. It finds multiple 
applications in the areas of science and engineering. With the exponential 
growth in the size of the dataset and advancements in technologies - the 
complexity of computing derivatives has increased and we have become 
increasingly dependent on computers to compute derivatives.

Currently, there are three ways to compute derivatives - finite, symbolic, 
automatic differentiation. The finite differentiation method although 
being quick and easy to implement - suffers from machine precision and 
rounding errors. We are able to alleviate these issues using symbolic 
differentiation, however, it becomes computationally very expensive as the 
function(s) starts to get complex. We are able to alleviate both the 
issues of computational complexity and machine precision using automatic 
differentiation.

Automatic Differentiation leverages symbolic rules for evaluating 
gradients - which is more accurate than using finite difference 
approximations. But unlike a purely symbolic process, the evaluation of 
expressions takes place early in the computation - it evaluates 
derivatives at particular numeric values.

The package fab-AD implements automatic differentiation for computational 
use. fabAD can be used to automatically differentiate functions via 
forward mode. Automatic Differentiation finds applications in 
optimization, machine learning, and numerical methods.

# Installation
Our package is for Python 3 only. You can access our package by cloning 
our repository. To clone run our repository, run `git clone 
git@code.harvard.edu:CS107/team32.git` from command line. Once you clone 
the repository you can use `cd team32` where you can find all the files. 
From there, you can use `cd src` to go where all the modules reside. Then 
use `python -m pip install toml` which will install all the requirements 
specified in toml.

 # User Guide
Once you install the package, you can simple import it by `from fab_ad 
import FabTensor`.
Afterwards, you could initiate the FabTensor object by giving the point 
where you wish to differentiate. FabTensor can take in a vector input 
values, representing a point's coordinates in multi-dimensional space. 
Moreover, you could also add other supplementary features as in the code 
demo provided below. You can find this demo file by the name of usage.py 
under src in the github.

```Python
from fab_ad import FabTensor
import numpy as np


if __name__ == "__main__":
    # value field should be initialized with value of the variable
    # derivative field should have dimension equal to number of independent input variables i.e [df/dx, df/dy] in this case.
    x = FabTensor(value=3, derivative=np.array([1, 0]), identifier='x')
    y = FabTensor(value=-4, derivative=np.array([0, 1]), identifier='y')
    # the following seed vector gives partial derivative w.r.t y
    seed_vector = np.array([0, 1])
    z = x * y
    print(z)
    print("gradient: ", z.directional_derivative(seed_vector))

    x = FabTensor(value=3, derivative=1, identifier='x')
    y = FabTensor(value=-4, derivative=0, identifier='y')
    z = x ** 2 + y ** 2
    print(z)
```

# Documentation
You can find the documentation for this package [here](https://code.harvard.edu/pages/CS107/team32/).

We use `numpydoc==1.5.0`  and `sphinx==4.2` for documentation.

# Future Features
As part of the extension for this project we plan on implementing higher order and mixed derivatives of vector functions. Specifically we will implement the Hessian matrix which includes the derivative of a function twice w.r.t each independent variable (similar to the Laplacian operator) and mixed derivatives (i.e. derivative w.r.t one independent variable followed by another independent variable). Currently, we have implemented only the first derivative of a function w.r.t all the seed vectors/independent variables.

### Changes in software
Currently the derivative data member of FabTensor object is a 1D array. This would change to 2D array to accommodate the Hessian matrix. Also, we would have to update each of our elementary math functions to return the second derivatives by taking the derivative of the first derivative. The main challenge here will be to efficiently compute the second derivatives from the first derivatives by reusing most of the code already written and using a helper function to call the same derivative function twice.

### Changes in directory structure, new modules, classes, data structures, etc
Directory structure would remain the same. Modules and classes would also remain the same because we don't need a new class to implement the second derivative. We would need a new method in the fab_ad class to call the derivative for the second time (derivative of the first derivative). Also, we would have to update each of our elementary math functions to return the second derivatives. Data structure of the derivative member of the FabTensor class would change from being a 1D array to 2D array to store all the second derivatives i.e. the Hessian matrix.

Higher order and mixed derivatives, specifically second order derivatives can then be used to determine the concavity, convexity, the points of inflection, and local extrema of functions. As pointed out earlier it can also be used to compute the Laplacian operator which is useful in describing many different phenomena, from electric potentials, to the diffusion equation for heat and fluid flow, and quantum mechanics.

# Broader Impact, Inclusivity and Future directions
We hope that our package will be used in a variety of disciplines, 
including physics, engineering, applied mathematics, astronomy, and even 
domains that the package's creators could never have envisaged. We believe 
that this package can be used to perform automatic differentiations 
accurately and effectively as well as serve as a model for the future 
creation of improved automatic differentiation packages. We see several 
opportunities for this package to be improved and would be pleased to see 
them realized.

On the other hand, we don't want to see this program being used as a 
shortcut for differentiating work or for plagiarism or cheating. This 
package's open-source nature makes it available to everyone, but it also 
leaves it vulnerable to those who intend to use it for plagiarism. Users 
should be mindful of this nature and pick their method of using this 
package carefully. This software is not intended to be used as a shortcut 
for differentiation procedures. It could be used to check results for 
derivative calculations done manually or using other algorithms, although 
derivative calculation techniques should still be used instead. These 
exercises serve a purpose, and using this software to find the solutions 
does not advance learning.

Also evident is the connection between our automatic differentiation 
algorithms and mathematical concepts like the Leibniz Rule and the Faa di 
Bruno Formula that we made while working on this project. It shouldn't be 
the first time that these formulas have been employed to compute 
higher-order derivatives, but it provided motivation for us to carry out 
the implementation ourselves. In order to close the gap between theories 
and applications, we want for our project to serve as a case study. This 
experience demonstrates that now is the perfect time for all types of 
information to come together in order to support new discoveries, which 
will enable us and many students to continue working toward this aim.

# Software Inclusivity
Users and collaborators from all origins and identities are welcome to the 
fab_ad package and its developer. As was seen during the creation of this 
package, we think that trust, respect, and care are the foundations of 
greatness in a collaborative endeavor. In an effort to reach as many 
people as possible who are interested in this package, we made every 
effort to make it as inclusive and user-friendly as possible by including 
the necessary documentation and instructions. Although this package was 
created using Python and English, anyone who is proficient in another 
language or programming language is welcome to contribute. Pull requests 
are examined and approved by all developers while this package is being 
developed.

Every time one of us feels the need to start a pull request, that person 
would talk to the other members and come to a consensus. We would adore 
the opportunity to carry this constructive dialogue into other 
collaborations with this package.



## Development environment setup

1. Create virtual environment

2. Use poetry to install Dependencies
```bash
python3 -m pip install poetry
poetry install
```

### Running tests
<TO DO>
All tests can be run for the repository using below command:

```
python -m pytest tests/
```


### Making documentation
```
Populate your master file team32/index.rst and create other documentation source files. Use the Makefile to build the docs, like so:
   make builder
where "builder" is one of the supported builders, e.g. html, latex or linkcheck.

```


