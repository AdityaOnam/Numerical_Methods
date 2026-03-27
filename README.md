# Numerical Methods Laboratory

This repository contains Python implementations of various numerical methods covered in a Numerical Methods course. Each lab file demonstrates different computational techniques for solving mathematical problems numerically.

## Overview

Numerical methods are algorithms for approximating solutions to mathematical problems that cannot be solved analytically. This collection covers fundamental techniques in error analysis, interpolation, differentiation, integration, and differential equations.

## Lab Files

### Lab 2 & Lab 2.1: Error Analysis
- **Topics**: Absolute error, relative error, significant digits
- **Concepts**: Error propagation, precision analysis, comparison of error types
- **Key Functions**: Error calculation formulas, significant digit determination

### Lab 3: Differentiation and Convergence
- **Topics**: Symbolic derivatives, numerical differentiation, convergence order
- **Concepts**: Computational order of convergence, error analysis in differentiation
- **Key Functions**: Symbolic differentiation using SymPy, convergence rate calculation

### Lab 5: Lagrange Interpolation
- **Topics**: Polynomial interpolation, Lagrange basis polynomials
- **Concepts**: Interpolation theory, basis functions, polynomial approximation
- **Key Functions**: Lagrange interpolation algorithm, basis term calculation

### Lab 6: Interpolation and Finite Differences
- **Topics**: Lagrange interpolation, forward difference tables
- **Concepts**: Polynomial interpolation, finite difference methods
- **Key Functions**: Lagrange polynomial construction, difference table generation

### Lab 8: Numerical Integration and Hermite Interpolation
- **Topics**: Trapezoidal rule, Simpson's rules (1/3 and 3/8), Hermite interpolation
- **Concepts**: Composite integration methods, oscillatory integral approximation, derivative-based interpolation
- **Key Functions**: Integration algorithms, Hermite polynomial construction

### Lab 9: Gaussian Quadrature
- **Topics**: Gauss-Legendre, Gauss-Chebyshev, Gauss-Laguerre quadrature
- **Concepts**: Weighted integration, orthogonal polynomials, high-accuracy quadrature
- **Key Functions**: Gaussian quadrature implementations for different weight functions

### Lab 10: Ordinary Differential Equations
- **Topics**: Euler method, Heun's method, Runge-Kutta 2nd order
- **Concepts**: Initial value problems, multi-step methods, predictor-corrector schemes
- **Key Functions**: ODE solvers for systems of equations

## Dependencies

The implementations use the following Python libraries:
- `numpy` - Numerical computations and arrays
- `sympy` - Symbolic mathematics
- `matplotlib` - Plotting and visualization
- `scipy` - Scientific computing (for special functions)
- `pandas` - Data manipulation (for tables)

## Installation

1. Ensure Python 3.7+ is installed
2. Install required packages:
   ```bash
   pip install numpy sympy matplotlib scipy pandas
   ```

## Usage

Each lab file contains standalone functions that can be run independently. Most files include example problems with predefined data. To run a specific lab:

```python
python lab_2.py
```

Or import specific functions:

```python
from lab_5 import lagrange_interpolation
result = lagrange_interpolation([1, 2, 4], [2, 3, 1], 2.5)
```

## Educational Purpose

These implementations are designed for learning numerical methods. They include:
- Detailed comments explaining algorithms
- Error handling for edge cases
- Step-by-step output for understanding
- References to mathematical formulas

## Course Context

This repository corresponds to laboratory assignments in a Numerical Methods course, typically covering:
- Error analysis and floating-point arithmetic
- Interpolation and approximation theory
- Numerical differentiation and integration
- Solution of ordinary differential equations

## Contributing

This is an educational repository. For improvements or corrections, please ensure changes maintain the pedagogical value of the implementations.