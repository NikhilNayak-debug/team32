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

# Broader Impact, Inclusivity and Future directions
