"""
Numerical Methods Lab - Complete Solutions
Author: Interactive Python Suite
Description: Comprehensive solution for all 18 numerical methods problems
with error handling and detailed explanations
"""

import math
import sys

# ============================================================================
# PROBLEM 1: Error Analysis
# ============================================================================
def problem_1():
    """
    Computes absolute error, relative error, and significant digits
    for approximations of sqrt(3).
    
    Formulas:
    - Absolute Error = |true_value - approximation|
    - Relative Error = |absolute_error / true_value|
    - Significant Digits = -floor(log10(relative_error))
    """
    print("\n" + "="*70)
    print("PROBLEM 1: Error Analysis for sqrt(3)")
    print("="*70)
    
    true_value = math.sqrt(3)
    approximations = [1.73, 1.732, 1.73205]
    
    print(f"\nTrue Value: {true_value:.10f}")
    print("\n{:<15} {:<20} {:<20} {:<15}".format(
        "Approximation", "Absolute Error", "Relative Error", "Sig. Digits"))
    print("-" * 70)
    
    for approx in approximations:
        abs_error = abs(true_value - approx)
        # Handle division by zero (though sqrt(3) != 0)
        if abs(true_value) < 1e-15:
            print("Error: Division by zero in relative error calculation")
            continue
        rel_error = abs_error / abs(true_value)
        
        # Significant digits calculation with error handling
        if rel_error > 0:
            sig_digits = max(0, -math.floor(math.log10(rel_error)))
        else:
            sig_digits = float('inf')
        
        print(f"{approx:<15.5f} {abs_error:<20.10e} {rel_error:<20.10e} {sig_digits}")

# ============================================================================
# PROBLEM 2: Absolute vs Relative Error Comparison
# ============================================================================
def problem_2():
    """
    Demonstrates that smaller absolute error doesn't necessarily mean
    smaller relative error.
    
    Example: For true value = 1000, error of 1 gives small relative error
             For true value = 0.001, error of 0.0001 gives large relative error
    """
    print("\n" + "="*70)
    print("PROBLEM 2: Absolute vs Relative Error")
    print("="*70)
    
    # Case 1: Large true value
    true_val_1 = 1000.0
    approx_1 = 999.0
    
    # Case 2: Small true value
    true_val_2 = 0.001
    approx_2 = 0.0009
    
    abs_err_1 = abs(true_val_1 - approx_1)
    abs_err_2 = abs(true_val_2 - approx_2)
    
    # Safe division with error handling
    try:
        rel_err_1 = abs_err_1 / abs(true_val_1) if abs(true_val_1) > 1e-15 else float('inf')
        rel_err_2 = abs_err_2 / abs(true_val_2) if abs(true_val_2) > 1e-15 else float('inf')
    except ZeroDivisionError:
        print("Error: Division by zero encountered")
        return
    
    print(f"\nCase 1: True Value = {true_val_1}, Approximation = {approx_1}")
    print(f"  Absolute Error: {abs_err_1:.10f}")
    print(f"  Relative Error: {rel_err_1:.10e}")
    
    print(f"\nCase 2: True Value = {true_val_2}, Approximation = {approx_2}")
    print(f"  Absolute Error: {abs_err_2:.10f}")
    print(f"  Relative Error: {rel_err_2:.10e}")
    
    print(f"\nObservation:")
    print(f"  Absolute Error 1 ({abs_err_1:.6f}) > Absolute Error 2 ({abs_err_2:.6f})")
    print(f"  BUT Relative Error 1 ({rel_err_1:.6e}) < Relative Error 2 ({rel_err_2:.6e})")

# ============================================================================
# PROBLEM 3: Numerical Stability - Direct vs Rationalized
# ============================================================================
def problem_3():
    """
    Evaluates f(x) = sqrt(x^2 + 1) - x using:
    1. Direct formula (prone to cancellation error for large x)
    2. Rationalized formula: 1 / (sqrt(x^2 + 1) + x) (numerically stable)
    
    For large x, direct method suffers from catastrophic cancellation.
    """
    print("\n" + "="*70)
    print("PROBLEM 3: Numerical Stability Analysis")
    print("="*70)
    
    x_values = [1e2, 1e4, 1e6]
    
    print("\n{:<15} {:<25} {:<25}".format("x", "Direct Formula", "Rationalized Formula"))
    print("-" * 70)
    
    for x in x_values:
        try:
            # Direct computation: sqrt(x^2 + 1) - x
            direct = math.sqrt(x**2 + 1) - x
            
            # Rationalized: 1 / (sqrt(x^2 + 1) + x)
            denominator = math.sqrt(x**2 + 1) + x
            if abs(denominator) < 1e-15:
                rationalized = float('inf')
            else:
                rationalized = 1.0 / denominator
            
            print(f"{x:<15.2e} {direct:<25.15e} {rationalized:<25.15e}")
        except (ValueError, ZeroDivisionError) as e:
            print(f"Error at x={x}: {e}")
    
    print("\nNote: Rationalized formula is more stable for large x values.")

# ============================================================================
# PROBLEM 4: Taylor Expansion vs Direct Computation
# ============================================================================
def problem_4():
    """
    Computes f(x) = ln(1+x) - x using:
    1. Direct computation (may lose precision for small x)
    2. Taylor expansion: -x^2/2 + x^3/3 - x^4/4 + ...
    
    Taylor series: ln(1+x) = x - x^2/2 + x^3/3 - x^4/4 + ...
    So ln(1+x) - x = -x^2/2 + x^3/3 - x^4/4 + ...
    """
    print("\n" + "="*70)
    print("PROBLEM 4: ln(1+x) - x Computation")
    print("="*70)
    
    x_values = [1e-2, 1e-5, 1e-8]
    
    print("\n{:<15} {:<25} {:<25}".format("x", "Direct", "Taylor Expansion"))
    print("-" * 70)
    
    for x in x_values:
        try:
            # Direct computation
            if x <= -1:
                direct = float('nan')
            else:
                direct = math.log(1 + x) - x
            
            # Taylor expansion: -x^2/2 + x^3/3 - x^4/4 + x^5/5 (5 terms)
            taylor = 0
            for n in range(2, 10):  # More terms for better accuracy
                taylor += ((-1)**n) * (x**n) / n
            
            print(f"{x:<15.2e} {direct:<25.15e} {taylor:<25.15e}")
        except (ValueError, ZeroDivisionError) as e:
            print(f"Error at x={x}: {e}")

# ============================================================================
# PROBLEM 5: Harmonic Sum - Forward vs Reverse
# ============================================================================
def problem_5():
    """
    Computes harmonic sum H_n = sum(1/k) for k=1 to n
    
    Forward summation: accumulates small terms, more rounding error
    Reverse summation: starts with small terms, often more accurate
    """
    print("\n" + "="*70)
    print("PROBLEM 5: Harmonic Sum (n=10^6)")
    print("="*70)
    
    n = 1000000
    
    # Forward summation
    forward_sum = 0.0
    for k in range(1, n + 1):
        try:
            forward_sum += 1.0 / k
        except ZeroDivisionError:
            print(f"Error: Division by zero at k={k}")
            return
    
    # Reverse summation
    reverse_sum = 0.0
    for k in range(n, 0, -1):
        try:
            reverse_sum += 1.0 / k
        except ZeroDivisionError:
            print(f"Error: Division by zero at k={k}")
            return
    
    print(f"\nForward Summation:  {forward_sum:.15f}")
    print(f"Reverse Summation:  {reverse_sum:.15f}")
    print(f"Difference:         {abs(forward_sum - reverse_sum):.15e}")
    print("\nNote: Reverse summation is often more accurate due to reduced rounding errors.")

# ============================================================================
# PROBLEM 6: Taylor Expansion for e^(-1)
# ============================================================================
def problem_6():
    """
    Approximates e^(-1) using Taylor series: e^x = sum(x^n / n!)
    For x = -1: e^(-1) = sum((-1)^n / n!)
    
    Finds minimum terms needed for error < 10^(-7)
    """
    print("\n" + "="*70)
    print("PROBLEM 6: Taylor Expansion for e^(-1)")
    print("="*70)
    
    true_value = math.exp(-1)
    tolerance = 1e-7
    
    approx = 0.0
    factorial = 1
    n = 0
    
    print(f"\nTrue value: {true_value:.15f}")
    print(f"\n{:<10} {:<25} {:<25}".format("Terms", "Approximation", "Error"))
    print("-" * 60)
    
    while True:
        try:
            if n > 0:
                factorial *= n
            term = ((-1)**n) / factorial
            approx += term
            error = abs(true_value - approx)
            
            if n % 5 == 0 or error < tolerance:  # Print every 5th term
                print(f"{n+1:<10} {approx:<25.15f} {error:<25.15e}")
            
            if error < tolerance:
                print(f"\nMinimum terms required: {n+1}")
                break
            
            n += 1
            if n > 100:  # Safety limit
                print("Exceeded maximum iterations")
                break
        except (OverflowError, ZeroDivisionError) as e:
            print(f"Error at term {n}: {e}")
            break

# ============================================================================
# PROBLEM 7: Taylor Polynomial for sin(x) at x=1
# ============================================================================
def problem_7():
    """
    Approximates sin(1) using Taylor polynomial:
    sin(x) = x - x^3/3! + x^5/5! - x^7/7! + ...
    
    Plots truncation error vs polynomial degree
    """
    print("\n" + "="*70)
    print("PROBLEM 7: Taylor Polynomial for sin(1)")
    print("="*70)
    
    x = 1.0
    true_value = math.sin(x)
    
    print(f"\nTrue value: sin(1) = {true_value:.15f}")
    print(f"\n{:<10} {:<25} {:<25}".format("Degree", "Approximation", "Truncation Error"))
    print("-" * 60)
    
    approx = 0.0
    factorial = 1
    
    for n in range(0, 20, 2):  # Only odd powers for sin(x)
        try:
            if n > 0:
                factorial *= n * (n - 1) if n > 1 else n
            
            term = ((-1)**(n//2)) * (x**n) / factorial if n > 0 else 0
            if n == 1:
                factorial = 1
                term = x
            elif n > 1:
                factorial = 1
                for i in range(1, n + 1):
                    factorial *= i
                term = ((-1)**(n//2)) * (x**n) / factorial
            
            approx += term
            error = abs(true_value - approx)
            
            print(f"{n+1:<10} {approx:<25.15f} {error:<25.15e}")
        except (OverflowError, ZeroDivisionError) as e:
            print(f"Error at degree {n}: {e}")
            break

# ============================================================================
# PROBLEM 8: Bisection Method for f(x) = x*ln(x) - 1
# ============================================================================
def bisection_method(f, a, b, tol=1e-6, max_iter=100):
    """
    Bisection Method for root finding
    
    Algorithm:
    1. Check if f(a) and f(b) have opposite signs
    2. Find midpoint c = (a + b) / 2
    3. If f(c) is close to 0, return c
    4. If f(a) and f(c) have opposite signs, set b = c
    5. Otherwise, set a = c
    6. Repeat until convergence
    
    Returns: root, iterations_list
    """
    iterations = []
    
    try:
        fa = f(a)
        fb = f(b)
        
        if fa * fb > 0:
            print(f"Error: f(a) and f(b) must have opposite signs")
            print(f"f({a}) = {fa}, f({b}) = {fb}")
            return None, iterations
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error evaluating function: {e}")
        return None, iterations
    
    for i in range(max_iter):
        try:
            c = (a + b) / 2.0
            fc = f(c)
            
            error = (b - a) / 2.0
            iterations.append({'iter': i+1, 'a': a, 'b': b, 'c': c, 'f(c)': fc, 'error': error})
            
            if abs(fc) < tol or error < tol:
                return c, iterations
            
            if fa * fc < 0:
                b = c
                fb = fc
            else:
                a = c
                fa = fc
        except (ValueError, ZeroDivisionError) as e:
            print(f"Error at iteration {i+1}: {e}")
            return None, iterations
    
    print(f"Warning: Maximum iterations reached")
    return (a + b) / 2.0, iterations

def problem_8():
    """
    Applies Bisection Method to f(x) = x*ln(x) - 1 on [1, 2]
    """
    print("\n" + "="*70)
    print("PROBLEM 8: Bisection Method for f(x) = x*ln(x) - 1")
    print("="*70)
    
    def f(x):
        if x <= 0:
            raise ValueError("ln(x) undefined for x <= 0")
        return x * math.log(x) - 1
    
    a, b = 1.0, 2.0
    root, iterations = bisection_method(f, a, b, tol=1e-6)
    
    if root is not None:
        print(f"\n{:<6} {:<12} {:<12} {:<12} {:<15} {:<15}".format(
            "Iter", "a", "b", "c", "f(c)", "Error"))
        print("-" * 80)
        
        for it in iterations[:10]:  # Show first 10 iterations
            print(f"{it['iter']:<6} {it['a']:<12.8f} {it['b']:<12.8f} {it['c']:<12.8f} "
                  f"{it['f(c)']:<15.8e} {it['error']:<15.8e}")
        
        if len(iterations) > 10:
            print("... (showing first 10 iterations)")
        
        print(f"\nRoot found: {root:.10f}")
        print(f"Total iterations: {len(iterations)}")

# ============================================================================
# PROBLEM 9: Verify Bisection Error Bound
# ============================================================================
def problem_9():
    """
    Verifies that bisection error satisfies |e_n| <= (b-a)/2^n
    """
    print("\n" + "="*70)
    print("PROBLEM 9: Verify Bisection Error Bound")
    print("="*70)
    
    def f(x):
        return x**2 - 2  # Root is sqrt(2)
    
    a, b = 0.0, 2.0
    true_root = math.sqrt(2)
    
    root, iterations = bisection_method(f, a, b, tol=1e-10)
    
    print(f"\nTrue root: {true_root:.15f}")
    print(f"\n{:<6} {:<15} {:<15} {:<15} {:<10}".format(
        "Iter", "Actual Error", "Error Bound", "Ratio", "Valid?"))
    print("-" * 75)
    
    for it in iterations[:15]:  # Show first 15
        actual_error = abs(true_root - it['c'])
        error_bound = (b - a) / (2**it['iter'])
        ratio = actual_error / error_bound if error_bound > 0 else 0
        valid = "Yes" if actual_error <= error_bound else "No"
        
        print(f"{it['iter']:<6} {actual_error:<15.8e} {error_bound:<15.8e} "
              f"{ratio:<15.8f} {valid:<10}")

# ============================================================================
# PROBLEM 10: Find all roots of x^4 - 5x^2 + 4 = 0
# ============================================================================
def problem_10():
    """
    Finds all real roots of x^4 - 5x^2 + 4 = 0
    This factors as (x^2 - 1)(x^2 - 4) = 0
    Roots: x = -2, -1, 1, 2
    """
    print("\n" + "="*70)
    print("PROBLEM 10: Find all roots of x^4 - 5x^2 + 4 = 0")
    print("="*70)
    
    def f(x):
        return x**4 - 5*x**2 + 4
    
    # Search intervals based on function analysis
    intervals = [(-3, -1.5), (-1.5, -0.5), (0.5, 1.5), (1.5, 3)]
    roots_found = []
    
    print("\nSearching for roots in different intervals...")
    
    for a, b in intervals:
        try:
            fa, fb = f(a), f(b)
            if fa * fb < 0:  # Sign change indicates root
                root, _ = bisection_method(f, a, b, tol=1e-8)
                if root is not None:
                    roots_found.append(root)
                    print(f"Root found in [{a}, {b}]: {root:.10f}")
        except Exception as e:
            print(f"Error in interval [{a}, {b}]: {e}")
    
    print(f"\nTotal roots found: {len(roots_found)}")
    print(f"Roots: {[f'{r:.6f}' for r in roots_found]}")

# ============================================================================
# PROBLEM 11: Secant Method with Different Initial Guesses
# ============================================================================
def secant_method(f, x0, x1, tol=1e-6, max_iter=100):
    """
    Secant Method for root finding
    
    Algorithm:
    x_{n+1} = x_n - f(x_n) * (x_n - x_{n-1}) / (f(x_n) - f(x_{n-1}))
    
    Similar to Newton's method but uses finite difference approximation
    for derivative
    
    Returns: root, iterations_list
    """
    iterations = []
    
    try:
        f0 = f(x0)
        f1 = f(x1)
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error evaluating function: {e}")
        return None, iterations
    
    for i in range(max_iter):
        try:
            denominator = f1 - f0
            if abs(denominator) < 1e-15:
                print(f"Error: Division by zero (f(x1) - f(x0) too small)")
                return None, iterations
            
            x2 = x1 - f1 * (x1 - x0) / denominator
            f2 = f(x2)
            
            error = abs(x2 - x1)
            iterations.append({'iter': i+1, 'x0': x0, 'x1': x1, 'x2': x2, 
                             'f(x2)': f2, 'error': error})
            
            if abs(f2) < tol or error < tol:
                return x2, iterations
            
            x0, x1 = x1, x2
            f0, f1 = f1, f2
            
        except (ValueError, ZeroDivisionError, OverflowError) as e:
            print(f"Error at iteration {i+1}: {e}")
            return None, iterations
    
    print(f"Warning: Maximum iterations reached")
    return x1, iterations

def problem_11():
    """
    Applies Secant Method to f(x) = x^3 - 2x - 5
    with three different initial guess pairs
    """
    print("\n" + "="*70)
    print("PROBLEM 11: Secant Method with Different Initial Guesses")
    print("="*70)
    
    def f(x):
        return x**3 - 2*x - 5
    
    # Three different initial guess pairs
    guess_pairs = [(1, 2), (2, 3), (0, 1)]
    
    for idx, (x0, x1) in enumerate(guess_pairs, 1):
        print(f"\n--- Case {idx}: Initial guesses x0={x0}, x1={x1} ---")
        root, iterations = secant_method(f, x0, x1, tol=1e-8)
        
        if root is not None and len(iterations) > 0:
            print(f"\n{:<6} {:<12} {:<12} {:<12} {:<15} {:<15}".format(
                "Iter", "x0", "x1", "x2", "f(x2)", "Error"))
            print("-" * 85)
            
            for it in iterations[:10]:
                print(f"{it['iter']:<6} {it['x0']:<12.8f} {it['x1']:<12.8f} "
                      f"{it['x2']:<12.8f} {it['f(x2)']:<15.8e} {it['error']:<15.8e}")
            
            print(f"\nRoot: {root:.10f}")
            print(f"Iterations: {len(iterations)}")

# ============================================================================
# PROBLEM 12: Secant Method Divergence
# ============================================================================
def problem_12():
    """
    Demonstrates divergence of Secant Method for f(x) = tan(x) - x
    with poor initial guesses (near discontinuities)
    """
    print("\n" + "="*70)
    print("PROBLEM 12: Secant Method Divergence")
    print("="*70)
    
    def f(x):
        try:
            return math.tan(x) - x
        except (ValueError, OverflowError):
            return float('inf')
    
    # Poor initial guesses near discontinuity at pi/2
    print("\n--- Poor Initial Guesses (near discontinuity) ---")
    x0, x1 = 1.5, 1.57
    
    root, iterations = secant_method(f, x0, x1, tol=1e-6, max_iter=20)
    
    if iterations:
        print(f"\n{:<6} {:<12} {:<12} {:<15}".format("Iter", "x2", "f(x2)", "Error"))
        print("-" * 50)
        
        for it in iterations[:15]:
            print(f"{it['iter']:<6} {it['x2']:<12.8f} {it['f(x2)']:<15.8e} {it['error']:<15.8e}")
        
        if root is None:
            print("\nMethod diverged or encountered numerical issues!")
        else:
            print(f"\nUnexpected convergence to: {root:.10f}")

# ============================================================================
# PROBLEM 13: Estimate Order of Convergence for Secant Method
# ============================================================================
def problem_13():
    """
    Estimates order of convergence of Secant Method numerically
    
    Theory: Secant method has order of convergence ≈ 1.618 (golden ratio)
    
    We estimate using: log|e_{n+1}| / log|e_n| ≈ order
    """
    print("\n" + "="*70)
    print("PROBLEM 13: Estimate Order of Convergence")
    print("="*70)
    
    def f(x):
        return x**3 - 2*x - 5
    
    x0, x1 = 2.0, 3.0
    true_root = 2.0945514815423265  # Computed to high precision
    
    root, iterations = secant_method(f, x0, x1, tol=1e-15, max_iter=50)
    
    print(f"\nTrue root (high precision): {true_root:.15f}")
    print(f"\n{:<6} {:<15} {:<15} {:<15}".format("Iter", "x_n", "Error", "Conv. Order"))
    print("-" * 60)
    
    errors = []
    for it in iterations:
        error = abs(true_root - it['x2'])
        errors.append(error)
    
    for i, it in enumerate(iterations[:20]):
        if i > 0 and errors[i] > 0 and errors[i-1] > 0:
            try:
                order = math.log(errors[i]) / math.log(errors[i-1]) if errors[i-1] > 1e-15 else 0
            except (ValueError, ZeroDivisionError):
                order = 0
        else:
            order = 0
        
        print(f"{it['iter']:<6} {it['x2']:<15.10f} {errors[i]:<15.8e} {order:<15.8f}")
    
    print("\nTheoretical order of convergence for Secant Method: ≈ 1.618")

# ============================================================================
# PROBLEM 14: Compare Bisection and Secant Methods
# ============================================================================
def problem_14():
    """
    Solves f(x) = x*e^(-x) - 0.1 using both methods
    Compares convergence rates and iterations
    """
    print("\n" + "="*70)
    print("PROBLEM 14: Bisection vs Secant Method Comparison")
    print("="*70)
    
    def f(x):
        try:
            return x * math.exp(-x) - 0.1
        except OverflowError:
            return float('inf') if x < 0 else -float('inf')
    
    # Find approximate root first for error calculation
    a, b = 0.1, 1.0
    approx_root, _ = bisection_method(f, a, b, tol=1e-12)
    
    print(f"\nApproximate root (high precision): {approx_root:.15f}")
    
    # Bisection Method
    print("\n--- BISECTION METHOD ---")
    root_bisect, iter_bisect = bisection_method(f, a, b, tol=1e-8)
    
    # Secant Method
    print("\n--- SECANT METHOD ---")
    x0, x1 = 0.1, 1.0
    root_secant, iter_secant = secant_method(f, x0, x1, tol=1e-8)
    
    # Comparison Table
    print("\n" + "="*70)
    print("COMPARISON TABLE")
    print("="*70)
    print(f"\n{:<20} {:<25} {:<25}".format("", "Bisection", "Secant"))
    print("-" * 70)
    print(f"{'Root Found':<20} {root_bisect:<25.15f} {root_secant:<25.15f}")
    print(f"{'Total Iterations':<20} {len(iter_bisect):<25} {len(iter_secant):<25}")
    print(f"{'Final Error':<20} {abs(approx_root-root_bisect):<25.10e} {abs(approx_root-root_secant):<25.10e}")
    
    print("\nConvergence Analysis:")
    print("- Bisection: Linear convergence (error halves each iteration)")
    print("- Secant: Superlinear convergence (faster than bisection)")
    print("- Secant is sensitive to initial guesses; Bisection is robust")

# ============================================================================
# PROBLEM 15: Solve e^(-x) = x
# ============================================================================
def problem_15():
    """
    Solves e^(-x) = x using both methods
    Verifies theoretical convergence orders
    """
    print("\n" + "="*70)
    print("PROBLEM 15: Solve e^(-x) = x")
    print("="*70)
    
    def f(x):
        try:
            return math.exp(-x) - x
        except OverflowError:
            return float('inf') if x < 0 else -float('inf')
    
    # Bisection
    a, b = 0.0, 1.0
    root_bisect, iter_bisect = bisection_method(f, a, b, tol=1e-10)
    
    # Secant
    x0, x1 = 0.0, 1.0
    root_secant, iter_secant = secant_method(f, x0, x1, tol=1e-10)
    
    print(f"\nBisection Root: {root_bisect:.15f} ({len(iter_bisect)} iterations)")
    print(f"Secant Root:    {root_secant:.15f} ({len(iter_secant)} iterations)")
    
    print("\nTheoretical Convergence Orders:")
    print("- Bisection: Order 1 (linear)")
    print("- Secant: Order ≈ 1.618 (superlinear)")

# ============================================================================
# PROBLEM 16: Hybrid Method (Bisection + Secant)
# ============================================================================
def hybrid_method(f, a, b, switch_width=1e-2, tol=1e-8, max_iter=100):
    """
    Hybrid method: starts with Bisection, switches to Secant when
    interval width < switch_width
    
    Combines robustness of Bisection with speed of Secant
    """
    iterations = []
    method_used = "Bisection"
    
    try:
        fa = f(a)
        fb = f(b)
        
        if fa * fb > 0:
            print("Error: f(a) and f(b) must have opposite signs")
            return None, iterations, method_used
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")
        return None, iterations, method_used
    
    # Bisection phase
    while (b - a) >= switch_width:
        c = (a + b) / 2.0
        fc = f(c)
        
        error = (b - a) / 2.0
        iterations.append({'method': 'Bisection', 'a': a, 'b': b, 
                          'x': c, 'f(x)': fc, 'error': error})
        
        if abs(fc) < tol:
            return c, iterations, "Bisection"
        
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
    
    # Switch to Secant
    method_used = "Hybrid (switched to Secant)"
    x0, x1 = a, b
    f0, f1 = f(x0), f(x1)
    
    for i in range(max_iter):
        try:
            denominator = f1 - f0
            if abs(denominator) < 1e-15:
                return x1, iterations, method_used
            
            x2 = x1 - f1 * (x1 - x0) / denominator
            f2 = f(x2)
            
            error = abs(x2 - x1)
            iterations.append({'method': 'Secant', 'a': None, 'b': None,
                             'x': x2, 'f(x)': f2, 'error': error})
            
            if abs(f2) < tol or error < tol:
                return x2, iterations, method_used
            
            x0, x1 = x1, x2
            f0, f1 = f1, f2
            
        except (ValueError, ZeroDivisionError) as e:
            print(f"Error in Secant phase: {e}")
            return x1, iterations, method_used
    
    return x1, iterations, method_used

def problem_16():
    """
    Applies hybrid method to f(x) = x^3 - 2x - 5
    """
    print("\n" + "="*70)
    print("PROBLEM 16: Hybrid Method (Bisection → Secant)")
    print("="*70)
    
    def f(x):
        return x**3 - 2*x - 5
    
    a, b = 2.0, 3.0
    root, iterations, method = hybrid_method(f, a, b, switch_width=1e-2, tol=1e-10)
    
    print(f"\nMethod used: {method}")
    print(f"\n{:<6} {:<12} {:<15} {:<15} {:<15}".format(
        "Iter", "Method", "x", "f(x)", "Error"))
    print("-" * 70)
    
    for i, it in enumerate(iterations, 1):
        print(f"{i:<6} {it['method']:<12} {it['x']:<15.10f} "
              f"{it['f(x)']:<15.8e} {it['error']:<15.8e}")
    
    print(f"\nFinal root: {root:.15f}")
    print(f"Total iterations: {len(iterations)}")

# ============================================================================
# PROBLEM 17: General Purpose Root Finding Module
# ============================================================================
def general_root_finder(f, method='both', a=None, b=None, x0=None, x1=None, 
                       tol=1e-8, max_iter=100):
    """
    General purpose root finder that accepts any function and applies
    Bisection and/or Secant methods
    
    Parameters:
    - f: function to find root of
    - method: 'bisection', 'secant', or 'both'
    - a, b: interval for bisection
    - x0, x1: initial guesses for secant
    - tol: tolerance
    - max_iter: maximum iterations
    """
    results = {}
    
    if method in ['bisection', 'both']:
        if a is None or b is None:
            print("Error: Bisection requires interval [a, b]")
        else:
            print("\n--- BISECTION METHOD ---")
            root, iterations = bisection_method(f, a, b, tol, max_iter)
            results['bisection'] = {'root': root, 'iterations': iterations}
    
    if method in ['secant', 'both']:
        if x0 is None or x1 is None:
            print("Error: Secant requires initial guesses x0 and x1")
        else:
            print("\n--- SECANT METHOD ---")
            root, iterations = secant_method(f, x0, x1, tol, max_iter)
            results['secant'] = {'root': root, 'iterations': iterations}
    
    return results

def problem_17():
    """
    Demonstrates the general root finding module
    """
    print("\n" + "="*70)
    print("PROBLEM 17: General Purpose Root Finding Module")
    print("="*70)
    
    # Test function: x^2 - 4 = 0 (root at x = 2)
    def test_func(x):
        return x**2 - 4
    
    print("\nTest Function: f(x) = x^2 - 4")
    print("Expected root: 2.0")
    
    results = general_root_finder(test_func, method='both', 
                                  a=0, b=3, x0=1, x1=3, tol=1e-10)
    
    # Comparison table
    print("\n" + "="*70)
    print("COMPARISON TABLE")
    print("="*70)
    
    if 'bisection' in results and 'secant' in results:
        bis_data = results['bisection']
        sec_data = results['secant']
        
        print(f"\n{:<6} {:<20} {:<20} {:<20}".format(
            "Iter", "Bisection Error", "Secant Error", "Method Comparison"))
        print("-" * 70)
        
        max_len = max(len(bis_data['iterations']), len(sec_data['iterations']))
        
        for i in range(min(15, max_len)):
            bis_err = bis_data['iterations'][i]['error'] if i < len(bis_data['iterations']) else 0
            sec_err = sec_data['iterations'][i]['error'] if i < len(sec_data['iterations']) else 0
            
            if bis_err > 0 and sec_err > 0:
                comparison = f"Secant {bis_err/sec_err:.2f}x faster"
            else:
                comparison = "-"
            
            print(f"{i+1:<6} {bis_err:<20.10e} {sec_err:<20.10e} {comparison}")

# ============================================================================
# PROBLEM 18: Chemical Engineering Application
# ============================================================================
def problem_18():
    """
    Chemical engineering problem: R(x) = x*e^(-x) - 0.05
    Find concentration where reaction rate is stable (R = 0)
    """
    print("\n" + "="*70)
    print("PROBLEM 18: Chemical Engineering Application")
    print("="*70)
    
    def R(x):
        """Reaction rate function"""
        try:
            return x * math.exp(-x) - 0.05
        except OverflowError:
            return float('inf') if x < 0 else -float('inf')
    
    # Part (a): Show root exists in [0.5, 1]
    print("\n(a) Verifying root exists in [0.5, 1]:")
    a, b = 0.5, 1.0
    Ra = R(a)
    Rb = R(b)
    
    print(f"    R(0.5) = {Ra:.10f}")
    print(f"    R(1.0) = {Rb:.10f}")
    print(f"    R(0.5) × R(1.0) = {Ra * Rb:.10f}")
    
    if Ra * Rb < 0:
        print("    ✓ Sign change confirms root exists in [0.5, 1]")
    else:
        print("    ✗ No sign change detected")
        return
    
    # Part (b) & (c): Apply Bisection Method
    print("\n(b) & (c) Applying Bisection Method (tolerance = 10^-4):")
    
    root, iterations = bisection_method(R, a, b, tol=1e-4)
    
    print(f"\n{:<6} {:<12} {:<12} {:<15} {:<15} {:<15}".format(
        "Iter", "a", "b", "c", "R(c)", "Error"))
    print("-" * 85)
    
    for it in iterations:
        print(f"{it['iter']:<6} {it['a']:<12.8f} {it['b']:<12.8f} "
              f"{it['c']:<12.8f} {it['f(c)']:<15.10e} {it['error']:<15.10e}")
    
    print(f"\nFinal Answer:")
    print(f"  Stable concentration: {root:.10f} mol/L")
    print(f"  Total iterations: {len(iterations)}")
    print(f"  Final error: {iterations[-1]['error']:.10e}")
    print(f"  Verification: R({root:.6f}) = {R(root):.10e}")

# ============================================================================
# MAIN MENU SYSTEM
# ============================================================================
def display_menu():
    """
    Displays the main menu with all problem options
    """
    print("\n" + "="*70)
    print(" " * 20 + "NUMERICAL METHODS LAB")
    print(" " * 25 + "Main Menu")
    print("="*70)
    
    problems = [
        "Error Analysis (sqrt(3))",
        "Absolute vs Relative Error",
        "Numerical Stability (Direct vs Rationalized)",
        "Taylor Expansion vs Direct (ln(1+x) - x)",
        "Harmonic Sum (Forward vs Reverse)",
        "Taylor Expansion for e^(-1)",
        "Taylor Polynomial for sin(1)",
        "Bisection: f(x) = x*ln(x) - 1",
        "Verify Bisection Error Bound",
        "Find all roots: x^4 - 5x^2 + 4 = 0",
        "Secant with Different Guesses",
        "Secant Method Divergence",
        "Estimate Convergence Order",
        "Compare Bisection vs Secant",
        "Solve e^(-x) = x",
        "Hybrid Method (Bisection + Secant)",
        "General Root Finding Module",
        "Chemical Engineering Application"
    ]
    
    for i, problem in enumerate(problems, 1):
        print(f"  {i:2d}. {problem}")
    
    print(f"\n   0. Exit Program")
    print("="*70)

def main():
    """
    Main program loop - runs indefinitely until user chooses to exit
    
    Features:
    - Interactive menu system
    - Error handling for invalid inputs
    - Clean interface
    - Infinite loop until exit
    """
    # Dictionary mapping menu choices to problem functions
    problem_functions = {
        1: problem_1,
        2: problem_2,
        3: problem_3,
        4: problem_4,
        5: problem_5,
        6: problem_6,
        7: problem_7,
        8: problem_8,
        9: problem_9,
        10: problem_10,
        11: problem_11,
        12: problem_12,
        13: problem_13,
        14: problem_14,
        15: problem_15,
        16: problem_16,
        17: problem_17,
        18: problem_18
    }
    
    print("\n" + "="*70)
    print(" " * 15 + "NUMERICAL METHODS LAB - PYTHON SUITE")
    print(" " * 20 + "by Amit K. Verma")
    print("="*70)
    print("\nThis program solves all 18 problems from the Numerical Methods Lab.")
    print("All mathematical errors (division by zero, overflow, etc.) are handled.")
    
    # Infinite loop - only exits when user chooses option 0
    while True:
        try:
            display_menu()
            
            # Get user input with error handling
            choice_input = input("\nEnter your choice (0-18): ").strip()
            
            # Handle empty input
            if not choice_input:
                print("\n⚠ Error: Please enter a number.")
                input("\nPress Enter to continue...")
                continue
            
            # Convert to integer with error handling
            try:
                choice = int(choice_input)
            except ValueError:
                print(f"\n⚠ Error: '{choice_input}' is not a valid number.")
                input("\nPress Enter to continue...")
                continue
            
            # Exit condition
            if choice == 0:
                print("\n" + "="*70)
                print(" " * 20 + "Thank you for using")
                print(" " * 15 + "NUMERICAL METHODS LAB SUITE")
                print("="*70)
                print("\nProgram terminated successfully.\n")
                break
            
            # Validate choice range
            if choice < 0 or choice > 18:
                print(f"\n⚠ Error: Please enter a number between 0 and 18.")
                input("\nPress Enter to continue...")
                continue
            
            # Execute the selected problem
            print("\n" + "="*70)
            print(f" Executing Problem {choice}")
            print("="*70)
            
            try:
                problem_functions[choice]()
            except KeyboardInterrupt:
                print("\n\n⚠ Operation cancelled by user.")
            except Exception as e:
                print(f"\n⚠ An unexpected error occurred: {e}")
                print("Please report this issue.")
            
            # Pause before returning to menu
            print("\n" + "="*70)
            input("\nPress Enter to return to main menu...")
            
        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully
            print("\n\n" + "="*70)
            print(" " * 20 + "Program Interrupted")
            print("="*70)
            
            confirm = input("\nDo you want to exit? (y/n): ").strip().lower()
            if confirm == 'y' or confirm == 'yes':
                print("\nExiting program...\n")
                break
            else:
                print("\nReturning to main menu...")
                continue
        
        except Exception as e:
            # Catch any other unexpected errors
            print(f"\n⚠ Critical error: {e}")
            print("The program will continue, but please report this issue.")
            input("\nPress Enter to continue...")

# ============================================================================
# PROGRAM ENTRY POINT
# ============================================================================
if __name__ == "__main__":
    """
    Entry point of the program
    
    This ensures the main() function only runs when the script is
    executed directly (not when imported as a module)
    """
    try:
        main()
    except Exception as e:
        print(f"\nFatal error: {e}")
        print("Program terminated.")
        sys.exit(1)