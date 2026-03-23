import numpy as np
from scipy.special import roots_legendre, roots_chebyt, roots_laguerre

def f1(x): return 1 / (1 + x**2)
def f2(x): return np.exp(-x**2)
def f3(x): return np.cos(x) # Weight 1/sqrt(1-x^2) is handled by Gauss-Chebyshev
def f4(x): return x**3 # Weight e^-x is handled by Gauss-Laguerre
def f5(x): return np.abs(x)
def f7(x): return x**3 + 1
def f8(x): return 1 / (1 + x)
def f9(x): return 1 / (2 + 2*x + x**2) # Function part for Gauss-Laguerre (needs transformation)

# --- Integration Methods ---

def trapezoidal(f, a, b, n):
    """Standard Trapezoidal Rule [cite: 27, 35]"""
    x = np.linspace(a, b, n + 1)
    y = f(x)
    h = (b - a) / n
    return (h / 2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])

def simpson13(f, a, b, n):
    """Simpson's 1/3 Rule (n must be even) [cite: 21, 28, 36]"""
    if n % 2 != 0: n += 1
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    return (h / 3) * (y[0] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]) + y[-1])

def simpson38(f, a, b, n):
    """Simpson's 3/8 Rule (n must be multiple of 3) [cite: 6, 30]"""
    if n % 3 != 0: n = (n // 3 + 1) * 3
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    s = y[0] + y[-1]
    for i in range(1, n):
        s += 3 * y[i] if i % 3 != 0 else 2 * y[i]
    return (3 * h / 8) * s

def gauss_legendre(f, a, b, n):
    """n-point Gauss-Legendre Quadrature [cite: 11, 16, 29]"""
    nodes, weights = roots_legendre(n)
    # Rescale nodes and weights from [-1, 1] to [a, b]
    rescaled_nodes = 0.5 * (b - a) * nodes + 0.5 * (a + b)
    rescaled_weights = 0.5 * (b - a) * weights
    return np.sum(rescaled_weights * f(rescaled_nodes))

def gauss_chebyshev(f, n):
    """Gauss-Chebyshev for integral of f(x)/sqrt(1-x^2) from -1 to 1 [cite: 14, 31]"""
    nodes, weights = roots_chebyt(n)
    return np.sum(weights * f(nodes))

def main():
    while True:
        print("\n--- Numerical Methods Lab-9 Menu ---")
        print("1. Problem 1: Combined Trapezoidal, 1/3, and 3/8 Rule")
        print("2. Problem 2 & 6: Gauss-Legendre (n-point)")
        print("3. Problem 3: Gauss-Chebyshev (n=3)")
        print("4. Problem 5: Composite Simpson vs 2-pt Gauss (|x|)")
        print("5. Problem 7: Compare Trap vs Simpson (x^3 + 1)")
        print("6. Problem 9: Gauss-Laguerre (0 to inf)")
        print("0. Exit")
        
        choice = input("Select a problem (0-6): ")

        if choice == '1':
            # Needs n to be multiple of 6 to use all three methods appropriately [cite: 7]
            n, a, b = 6, -1, 1
            exact = 2 * np.arctan(1) # Exact value of 1/(1+x^2)
            res_t = trapezoidal(f1, a, b, n)
            res_s1 = simpson13(f1, a, b, n)
            res_s3 = simpson38(f1, a, b, n)
            print(f"Exact: {exact:.6f}")
            print(f"Trapezoidal: {res_t:.6f}, Error: {abs(exact-res_t):.6e}")
            print(f"Simpson 1/3: {res_s1:.6f}, Error: {abs(exact-res_s1):.6e}")
            print(f"Simpson 3/8: {res_s3:.6f}, Error: {abs(exact-res_s3):.6e}")

        elif choice == '2':
            # Evaluates e^-x^2 [cite: 13, 25]
            n = int(input("Enter n (e.g., 3): "))
            res = gauss_legendre(f2, -1, 1, n)
            print(f"Gauss-Legendre ({n}-point) Result: {res:.6f}")

        elif choice == '3':
            # Gauss-Chebyshev for cos(x)/sqrt(1-x^2) [cite: 15]
            res = gauss_chebyshev(f3, 3)
            print(f"Gauss-Chebyshev (n=3) Result: {res:.6f}")

        elif choice == '4':
            # Split interval at x=0 because |x| is not smooth there 
            res_s = simpson13(f5, -2, 0, 10) + simpson13(f5, 0, 2, 10)
            res_g = gauss_legendre(f5, -2, 0, 2) + gauss_legendre(f5, 0, 2, 2)
            print(f"Composite Simpson 1/3: {res_s:.6f}")
            print(f"Piecewise 2-pt Gauss: {res_g:.6f}")
            print("Exact Value for integral of |x| from -2 to 2: 4.0")

        elif choice == '5':
            # Integrate x^3 + 1 from 1 to 10 [cite: 34, 37]
            a, b, n = 1, 10, 20
            exact = ( (10**4/4 + 10) - (1**4/4 + 1) )
            print(f"Exact: {exact:.2f}")
            print(f"Trapezoidal: {trapezoidal(f7, a, b, n):.4f}")
            print(f"Simpson 1/3: {simpson13(f7, a, b, n):.4f}")

        elif choice == '6':
            # Gauss-Laguerre for 0 to infinity [cite: 42, 44]
            # f(x) = 1 / (2 + 2x + x^2). Gauss-Laguerre expects weight e^-x.
            # We rewrite: integral e^-x * [e^x / (2 + 2x + x^2)] dx
            def laguerre_integrand(x): return np.exp(x) / (2 + 2*x + x**2)
            nodes, weights = roots_laguerre(3)
            res = np.sum(weights * laguerre_integrand(nodes))
            print(f"Gauss-Laguerre (n=3) Result: {res:.6f}")

        elif choice == '0':
            break
        else:
            print("Invalid selection.")

if __name__ == "__main__":
    main()