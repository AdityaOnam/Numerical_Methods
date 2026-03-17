import sympy as sp
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Given data
x_vals = [1.0, 1.3, 1.6, 1.9, 2.2]
y_vals = [0.7651977, 0.6200860, 0.4554022, 0.2818186, 0.1103623]

x = sp.Symbol('x')


# (i) Lagrange Interpolation

def lagrange_interpolation(x_vals, y_vals):
    n = len(x_vals)
    poly = 0

    for i in range(n):
        term = y_vals[i]
        for j in range(n):
            if i != j:
                term *= (x - x_vals[j])/(x_vals[i] - x_vals[j])
        poly += term

    return sp.simplify(poly)

lagrange_poly = lagrange_interpolation(x_vals, y_vals)
lagrange_poly_simplified = sp.expand(lagrange_poly)

print("\nLagrange Polynomial:")
print(lagrange_poly_simplified)

#forward diffrence 

def forward_difference_table(x_vals, y_vals):
    n = len(y_vals)
    table = np.zeros((n,n))
    table[:,0] = y_vals

    for j in range(1,n):
        for i in range(n-j):
            table[i][j] = table[i+1][j-1] - table[i][j-1]

    return table

fd_table = forward_difference_table(x_vals, y_vals)
print("\nForward Difference Table:")
print(pd.DataFrame(fd_table))

h = x_vals[1] - x_vals[0]
s = (x - x_vals[0]) / h

newton_forward_poly = y_vals[0]
prod = 1
fact = 1

for i in range(1,len(x_vals)):
    prod *= (s - (i-1))
    fact *= i
    newton_forward_poly += (fd_table[0][i] * prod) / fact

newton_forward_poly = sp.expand(newton_forward_poly)

print("\nNewton Forward Polynomial:")
print(newton_forward_poly)


# ----------------------------
# (iii) Newton Backward Difference
# ----------------------------

def backward_difference_table(x_vals, y_vals):
    n = len(y_vals)
    table = np.zeros((n,n))
    table[:,0] = y_vals

    for j in range(1,n):
        for i in range(n-1,j-2,-1):
            table[i][j] = table[i][j-1] - table[i-1][j-1]

    return table

bd_table = backward_difference_table(x_vals, y_vals)

print("\nBackward Difference Table:")
print(pd.DataFrame(bd_table))

s = (x - x_vals[-1]) / h

newton_backward_poly = y_vals[-1]
prod = 1
fact = 1

n = len(x_vals)

for i in range(1,n):
    prod *= (s + (i-1))
    fact *= i
    newton_backward_poly += (bd_table[n-1][i] * prod) / fact

newton_backward_poly = sp.expand(newton_backward_poly)

print("\nNewton Backward Polynomial:")
print(newton_backward_poly)


# ----------------------------
# (d) Compare Polynomials
# ----------------------------
print("\nComparison:")
print(sp.simplify(lagrange_poly_simplified - newton_forward_poly))
print(sp.simplify(lagrange_poly_simplified - newton_backward_poly))

# ----------------------------
# (e) Plot
# ----------------------------
f_lagrange = sp.lambdify(x, lagrange_poly_simplified)

x_plot = np.linspace(1,2.3,200)
y_plot = f_lagrange(x_plot)

plt.scatter(x_vals, y_vals, color='red', label="Data Points")
plt.plot(x_plot, y_plot, label="Interpolating Polynomial")

plt.legend()
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Interpolation Polynomial")
plt.show()