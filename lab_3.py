import sympy as sp
import numpy as np
import math
import sys

# ==========================================
# HELPER FUNCTIONS
# ==========================================

def calculate_convergence_order(errors):
    """
    Calculates the computational order of convergence 'p' using the formula:
    p ≈ ln|e_{k+1}/e_k| / ln|e_k/e_{k-1}|
    Requires at least 3 error terms (current, previous, pre-previous).
    """
    if len(errors) < 3:
        return 0.0
    
    e_curr = errors[-1]      # e_{k+1}
    e_prev = errors[-2]      # e_k
    e_prev2 = errors[-3]     # e_{k-1}
    
    try:
        # Avoid math domain errors (log of zero) or division by zero
        if e_prev == 0 or e_prev2 == 0: return 0.0
        
        ratio1 = abs(e_curr / e_prev)
        ratio2 = abs(e_prev / e_prev2)
        
        if ratio1 == 0 or ratio2 == 0: return 0.0
        
        numerator = np.log(ratio1)
        denominator = np.log(ratio2)
        
        # Check to avoid division by zero in the final calculation
        if denominator == 0: return 0.0
        
        return numerator / denominator
    except Exception:
        return 0.0

# ==========================================
# PROBLEM 1: SYMBOLIC DERIVATIVE
# ==========================================

def solve_problem_1():
    """
    Solves Problem 1: Computes symbolic derivative using SymPy.
    """
    print("\n" + "="*60)
    print("PROBLEM 1: Symbolic Derivative")
    print("="*60)
    
    # 1. Define the symbolic variable
    x = sp.symbols('x')
    
    # 2. Define the function f(x)
    # Source Eq: f(x) = x^4*sin(x) + e^(2x)*ln(x) - sqrt(x)/(1+x^2)
    f = x**4 * sp.sin(x) + sp.exp(2*x) * sp.log(x) - sp.sqrt(x) / (1 + x**2)
    
    print("\nOriginal Function f(x):")
    sp.pprint(f)
    
    # 3. Compute Derivative
    f_prime = sp.diff(f, x)
    
    print("\nCalculated Derivative f'(x):")
    sp.pprint(f_prime)
    
    print("\n[Note: 'log' in SymPy represents the natural logarithm ln]")
    input("\nPress Enter to return to menu...")

# ==========================================
# PROBLEM 2: NEWTON-RAPHSON ROOTS
# ==========================================

def newton_raphson_solver(func, deriv_func, x0, tol=1e-6, max_iter=50, label=""):
    """
    Generic Newton-Raphson solver that prints a formatted table.
    """
    print(f"\n--- Solving {label} ---")
    print(f"Initial Approx: {x0}, Tolerance: {tol}")
    print(f"{'Iter':<5} | {'Approximation (xn)':<18} | {'Abs Error':<15} | {'Order (p)':<10}")
    print("-" * 60)
    
    x_curr = x0
    errors = []
    
    for i in range(1, max_iter + 1):
        f_val = func(x_curr)
        df_val = deriv_func(x_curr)
        
        if df_val == 0:
            print("Derivative is zero. Cannot continue.")
            break
            
        # Newton-Raphson Formula: x_{n+1} = x_n - f(x_n)/f'(x_n)
        x_next = x_curr - (f_val / df_val)
        
        # Calculate Error
        error = abs(x_next - x_curr)
        errors.append(error)
        
        # Calculate Order
        p = calculate_convergence_order(errors)
        p_str = f"{p:.4f}" if len(errors) >= 3 else "-"
        
        print(f"{i:<5} | {x_next:<18.9f} | {error:<15.2e} | {p_str:<10}")
        
        if error < tol:
            print(f"\n> Converged to {x_next:.9f} in {i} iterations.")
            return
        
        x_curr = x_next
    
    print("> Max iterations reached without satisfying tolerance.")

def solve_problem_2():
    """
    Solves Problem 2: Real roots using Newton-Raphson for two specific equations.
    """
    print("\n" + "="*60)
    print("PROBLEM 2: Newton-Raphson Method")
    print("="*60)
    
    # --- Part A ---
    # f1(x) = 3x - 1 - cos(x)
    # f1'(x) = 3 + sin(x)
    def f1(x): return 3*x - 1 - math.cos(x)
    def df1(x): return 3 + math.sin(x)
    
    newton_raphson_solver(f1, df1, x0=0.5, tol=1e-6, label="(a) 3x - 1 - cos(x)")
    
    # --- Part B ---
    # f2(x) = x^3 - 1 - 3 => x^3 - 4
    # f2'(x) = 3x^2
    def f2(x): return x**3 - 4
    def df2(x): return 3 * x**2
    
    newton_raphson_solver(f2, df2, x0=1.5, tol=1e-6, label="(b) x^3 - 4")
    
    input("\nPress Enter to return to menu...")

# ==========================================
# PROBLEM 3: MULTIPLE ROOTS COMPARISON
# ==========================================

def solve_problem_3():
    """
    Solves Problem 3: Compares Standard NR, Modified NR, and Secant method
    for a function with multiple roots: f(x) = (x-1)^3 * e^x
    """
    print("\n" + "="*60)
    print("PROBLEM 3: Methods for Multiple Roots")
    print("="*60)
    
    # Function Definition
    # f(x) = (x-1)^3 * e^x
    # Root is x=1 with multiplicity m=3
    def f3(x): 
        return ((x - 1)**3) * math.exp(x)

    # Derivative
    # f'(x) = e^x * (x-1)^2 * (x+2)
    def df3(x): 
        return math.exp(x) * ((x - 1)**2) * (x + 2)

    # Parameters
    tol = 1e-8
    x0 = 1.5
    max_iter = 50
    
    print(f"Target Function: f(x) = (x-1)^3 * e^x")
    print(f"True Root: x = 1 (Multiplicity m=3)")
    print(f"Stopping Criterion: Abs Error < {tol}")
    print("-" * 60)

    results = [] # To store summary

    # --- 1. Standard Newton-Raphson ---
    print("\n>>> Method A: Standard Newton-Raphson")
    x = x0
    errors = []
    iter_count = 0
    final_p = 0
    
    for i in range(1, max_iter + 1):
        fx = f3(x)
        dfx = df3(x)
        if dfx == 0: break
        
        x_new = x - (fx / dfx)
        error = abs(x_new - x)
        errors.append(error)
        
        x = x_new
        iter_count = i
        if error < tol: break
    
    final_p = calculate_convergence_order(errors)
    results.append(["Standard NR", iter_count, x, errors[-1], final_p])
    print(f"Result: Converged to {x:.8f} in {iter_count} iterations.")

    # --- 2. Modified Newton-Raphson ---
    print("\n>>> Method B: Modified Newton-Raphson (m=3)")
    x = x0
    m = 3 # Multiplicity
    errors = []
    iter_count = 0
    
    for i in range(1, max_iter + 1):
        fx = f3(x)
        dfx = df3(x)
        if dfx == 0: break
        
        # Modified Formula: x = x - m * (f/f')
        x_new = x - m * (fx / dfx)
        error = abs(x_new - x)
        errors.append(error)
        
        x = x_new
        iter_count = i
        if error < tol: break
        
    final_p = calculate_convergence_order(errors)
    results.append(["Modified NR", iter_count, x, errors[-1], final_p])
    print(f"Result: Converged to {x:.8f} in {iter_count} iterations.")

    # --- 3. Secant Method ---
    print("\n>>> Method C: Secant Method")
    x_prev = 0.5
    x_curr = 1.5
    errors = []
    iter_count = 0
    
    print(f"Initial approximations: x0={x_prev}, x1={x_curr}")
    
    for i in range(1, max_iter + 1):
        f_prev = f3(x_prev)
        f_curr = f3(x_curr)
        
        if (f_curr - f_prev) == 0: break
        
        # Secant Formula
        x_new = x_curr - f_curr * (x_curr - x_prev) / (f_curr - f_prev)
        error = abs(x_new - x_curr)
        errors.append(error)
        
        x_prev = x_curr
        x_curr = x_new
        iter_count = i
        if error < tol: break
        
    final_p = calculate_convergence_order(errors)
    results.append(["Secant Method", iter_count, x_curr, errors[-1], final_p])
    print(f"Result: Converged to {x_curr:.8f} in {iter_count} iterations.")

    # --- Summary Table ---
    print("\n" + "="*80)
    print("FINAL COMPARISON TABLE")
    print("="*80)
    print(f"{'Method':<20} | {'Iters':<6} | {'Root Found':<12} | {'Final Error':<12} | {'Final Order'}")
    print("-" * 80)
    for res in results:
        # res = [Name, Iters, Root, Error, Order]
        print(f"{res[0]:<20} | {res[1]:<6} | {res[2]:<12.8f} | {res[3]:<12.2e} | {res[4]:.4f}")
    
    print("\nObservation: Modified NR is fastest (Quadratic) for multiple roots.")
    print("Standard NR degrades to Linear convergence for multiple roots.")
    input("\nPress Enter to return to menu...")

# ==========================================
# MAIN MENU DRIVER
# ==========================================

def main_menu():
    while True:
        print("\n" + "="*40)
        print(" NUMERICAL METHODS LAB - MAIN MENU")
        print("="*40)
        print("1. Problem 1: Symbolic Derivative")
        print("2. Problem 2: Newton-Raphson (Simple Roots)")
        print("3. Problem 3: Multiple Roots Comparison")
        print("4. Exit")
        print("-" * 40)
        
        choice = input("Enter choice (1-4): ").strip()
        
        if choice == '1':
            solve_problem_1()
        elif choice == '2':
            solve_problem_2()
        elif choice == '3':
            solve_problem_3()
        elif choice == '4':
            print("Exiting program. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()