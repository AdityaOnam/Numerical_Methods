import math
import sys

def problem_1():
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
        if abs(true_value) < 1e-15:
            print("Error: Division by zero in relative error calculation")
            continue
        rel_error = abs_error / abs(true_value)
        
        if rel_error > 0:
            sig_digits = max(0, -math.floor(math.log10(rel_error)))
        else:
            sig_digits = float('inf')
        
        print(f"{approx:<15.5f} {abs_error:<20.10e} {rel_error:<20.10e} {sig_digits}")

def problem_2():
    print("\n" + "="*70)
    print("PROBLEM 2: Absolute vs Relative Error")
    print("="*70)
    
    true_val_1 = 1000.0
    approx_1 = 999.0
    true_val_2 = 0.001
    approx_2 = 0.0009
    
    abs_err_1 = abs(true_val_1 - approx_1)
    abs_err_2 = abs(true_val_2 - approx_2)
    
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

def problem_3():
    print("\n" + "="*70)
    print("PROBLEM 3: Numerical Stability Analysis")
    print("="*70)
    x_values = [1e2, 1e4, 1e6]
    print("\n{:<15} {:<25} {:<25}".format("x", "Direct Formula", "Rationalized Formula"))
    print("-" * 70)
    for x in x_values:
        try:
            direct = math.sqrt(x**2 + 1) - x
            denominator = math.sqrt(x**2 + 1) + x
            rationalized = 1.0 / denominator if abs(denominator) > 1e-15 else float('inf')
            print(f"{x:<15.2e} {direct:<25.15e} {rationalized:<25.15e}")
        except (ValueError, ZeroDivisionError) as e:
            print(f"Error at x={x}: {e}")

def problem_4():
    print("\n" + "="*70)
    print("PROBLEM 4: ln(1+x) - x Computation")
    print("="*70)
    x_values = [1e-2, 1e-5, 1e-8]
    print("\n{:<15} {:<25} {:<25}".format("x", "Direct", "Taylor Expansion"))
    print("-" * 70)
    for x in x_values:
        direct = math.log(1 + x) - x if x > -1 else float('nan')
        taylor = sum([((-1)**n) * (x**n) / n for n in range(2, 10)])
        print(f"{x:<15.2e} {direct:<25.15e} {taylor:<25.15e}")

def problem_5():
    print("\n" + "="*70)
    print("PROBLEM 5: Harmonic Sum (n=10^6)")
    print("="*70)
    n = 1000000
    forward_sum = sum(1.0/k for k in range(1, n + 1))
    reverse_sum = sum(1.0/k for k in range(n, 0, -1))
    print(f"\nForward Summation:  {forward_sum:.15f}")
    print(f"Reverse Summation:  {reverse_sum:.15f}")
    print(f"Difference:         {abs(forward_sum - reverse_sum):.15e}")

def problem_6():
    print("\n" + "="*70)
    print("PROBLEM 6: Taylor Expansion for e^(-1)")
    print("="*70)
    true_value = math.exp(-1)
    approx, factorial, n = 0.0, 1, 0
    while True:
        if n > 0: factorial *= n
        term = ((-1)**n) / factorial
        approx += term
        error = abs(true_value - approx)
        if error < 1e-7:
            print(f"Minimum terms required: {n+1}")
            print(f"Approximation: {approx:.15f}")
            break
        n += 1

def problem_7():
    print("\n" + "="*70)
    print("PROBLEM 7: Taylor Polynomial for sin(1)")
    print("="*70)
    x, true_value = 1.0, math.sin(1.0)
    approx = 0.0
    for n in range(0, 10):
        term = ((-1)**n * x**(2*n+1)) / math.factorial(2*n+1)
        approx += term
        print(f"Degree {2*n+1}: {approx:.15f} | Error: {abs(true_value - approx):.15e}")

def bisection_method(f, a, b, tol=1e-6, max_iter=100):
    iterations = []
    fa, fb = f(a), f(b)
    if fa * fb > 0: return None, iterations
    for i in range(max_iter):
        c = (a + b) / 2.0
        fc = f(c)
        error = (b - a) / 2.0
        iterations.append({'iter': i+1, 'a': a, 'b': b, 'c': c, 'f(c)': fc, 'error': error})
        if abs(fc) < tol or error < tol: return c, iterations
        if fa * fc < 0:
            b, fb = c, fc
        else:
            a, fa = c, fc
    return c, iterations

def problem_8():
    print("\nPROBLEM 8: Bisection for x*ln(x) - 1")
    f = lambda x: x * math.log(x) - 1
    root, _ = bisection_method(f, 1.0, 2.0)
    print(f"Root: {root:.10f}")

def problem_9():
    print("\nPROBLEM 9: Verify Bisection Error Bound")
    f = lambda x: x**2 - 2
    root, iters = bisection_method(f, 0, 2, tol=1e-10)
    for it in iters[:5]:
        print(f"Iter {it['iter']}: Bound {(2-0)/2**it['iter']:.5e}")

def problem_10():
    print("\nPROBLEM 10: Roots of x^4 - 5x^2 + 4 = 0")
    f = lambda x: x**4 - 5*x**2 + 4
    for bounds in [(-3, -1.5), (-1.5, -0.5), (0.5, 1.5), (1.5, 3)]:
        root, _ = bisection_method(f, bounds[0], bounds[1])
        print(f"Root in {bounds}: {root:.4f}")

def secant_method(f, x0, x1, tol=1e-6, max_iter=100):
    iterations = []
    f0, f1 = f(x0), f(x1)
    for i in range(max_iter):
        if abs(f1 - f0) < 1e-15: return None, iterations
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        f2 = f(x2)
        error = abs(x2 - x1)
        iterations.append({'iter': i+1, 'x2': x2, 'error': error})
        if abs(f2) < tol or error < tol: return x2, iterations
        x0, x1, f0, f1 = x1, x2, f1, f2
    return x1, iterations

def problem_11():
    print("\nPROBLEM 11: Secant Method x^3 - 2x - 5")
    f = lambda x: x**3 - 2*x - 5
    for x0, x1 in [(1,2), (2,3)]:
        root, _ = secant_method(f, x0, x1)
        print(f"Guesses {x0, x1} -> Root: {root:.6f}")

def problem_12():
    print("\nPROBLEM 12: Secant Divergence (tan x - x)")
    f = lambda x: math.tan(x) - x
    root, _ = secant_method(f, 1.5, 1.57, max_iter=10)
    print("Method Diverged" if root is None else f"Root: {root}")

def problem_13():
    print("\nPROBLEM 13: Convergence Order")
    f = lambda x: x**3 - 2*x - 5
    root, iters = secant_method(f, 2, 3, tol=1e-12)
    print("Order ≈ 1.618 (Theoretical)")

def problem_14():
    f = lambda x: x * math.exp(-x) - 0.1
    r1, _ = bisection_method(f, 0.1, 1.0)
    r2, _ = secant_method(f, 0.1, 1.0)
    print(f"\nPROBLEM 14 Comparison:\nBisection: {r1}\nSecant: {r2}")

def problem_15():
    f = lambda x: math.exp(-x) - x
    r, _ = secant_method(f, 0, 1)
    print(f"\nPROBLEM 15: e^-x = x -> Root: {r}")

def problem_16():
    print("\nPROBLEM 16: Hybrid Method")
    f = lambda x: x**3 - 2*x - 5
    # Simplified hybrid logic
    root, _ = bisection_method(f, 2, 3, tol=1e-2)
    root, _ = secant_method(f, root-0.1, root+0.1)
    print(f"Root: {root}")

def problem_17():
    print("\nPROBLEM 17: General Module Test")
    problem_14()

def problem_18():
    print("\nPROBLEM 18: Chemical Engineering Application")
    R = lambda x: x * math.exp(-x) - 0.05
    root, _ = bisection_method(R, 0.5, 1.0, tol=1e-4)
    print(f"Stable Concentration: {root:.6f} mol/L")

def display_menu():
    print("\n" + "="*70 + "\n" + " "*20 + "NUMERICAL METHODS LAB MENU\n" + "="*70)
    options = ["Exit", "sqrt(3)", "Abs vs Rel", "Stability", "ln(1+x)-x", "Harmonic", "e^-1", "sin(1)", 
               "Bisection 1", "Error Bound", "All Roots", "Secant 1", "Divergence", "Order", "Compare", 
               "e^-x=x", "Hybrid", "General", "Chem Eng"]
    for i, opt in enumerate(options):
        print(f"{i:2d}. {opt}")

def main():
    funcs = {i: globals().get(f"problem_{i}") for i in range(1, 19)}
    while True:
        display_menu()
        try:
            choice = int(input("\nChoice (0-18): "))
            if choice == 0: break
            if choice in funcs: funcs[choice]()
            input("\nPress Enter...")
        except: break

if __name__ == "__main__":
    main()