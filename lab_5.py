import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import math

# ==========================================
# CORE HELPER FUNCTIONS
# ==========================================

def lagrange_basis_term(i, x_val, X_nodes):
    """
    Computes the i-th Lagrange basis polynomial L_i(x) at a specific point.
    Formula: Product of (x - x_j) / (x_i - x_j) for all j != i.
    Refers to Question 2[cite: 7].
    """
    L_i = 1.0
    for j in range(len(X_nodes)):
        if i != j:
            # Multiply by the term (x - x_j) / (x_i - x_j)
            L_i *= (x_val - X_nodes[j]) / (X_nodes[i] - X_nodes[j])
    return L_i

def lagrange_interpolation(X, Y, x_val):
    """
    General function to compute interpolated value using Lagrange's method.
    Iterates through all data points, calculates basis L_i, and sums y_i * L_i.
    Refers to Question 4[cite: 16].
    """
    n = len(X)
    result = 0.0
    for i in range(n):
        # Calculate L_i(x)
        L_i = lagrange_basis_term(i, x_val, X)
        # Add y_i * L_i(x) to the polynomial sum
        result += Y[i] * L_i
    return result

# ==========================================
# PROBLEM SOLVERS
# ==========================================

def solve_q1():
    """
    Q1: Find interpolated value of x=2.5 for data (1,2), (2,3), (4,1)[cite: 5, 6].
    """
    print("\n--- Solution for Question 1 ---")
    # Define the known data points
    X = [1, 2, 4]
    Y = [2, 3, 1]
    target_x = 2.5
    
    # Compute interpolation
    interp_val = lagrange_interpolation(X, Y, target_x)
    
    print(f"Data Points: {list(zip(X, Y))}")
    print(f"Interpolated value at x = {target_x} is: {interp_val:.4f}")

def solve_q2():
    """
    Q2: Function for i-th Lagrange basis polynomial[cite: 7].
    Demonstrates the helper function defined above.
    """
    print("\n--- Solution for Question 2 ---")
    X = [1, 2, 4]
    i = 1 # We want L_1(x), corresponding to node x=2
    x_val = 2.5
    
    val = lagrange_basis_term(i, x_val, X)
    print(f"Calculated L_{i}({x_val}) for nodes {X}: {val:.4f}")
    print("Note: This logic is encapsulated in the 'lagrange_basis_term' function.")

def solve_q3():
    """
    Q3: Nested loops ONLY (no built-in libs) for X=[1,2,4,5], Y=[2,3,1,4] at x=3 [cite: 12-14].
    """
    print("\n--- Solution for Question 3 ---")
    X = [1, 2, 4, 5]
    Y = [2, 3, 1, 4]
    x_p = 3
    n = len(X)
    yp = 0.0
    
    # Outer loop: Summation over i
    for i in range(n):
        p = 1.0
        # Inner loop: Product over j
        for j in range(n):
            if i != j:
                p = p * (x_p - X[j]) / (X[i] - X[j])
        yp = yp + Y[i] * p
        
    print(f"Data X: {X}, Data Y: {Y}")
    print(f"Interpolated value at x={x_p} using nested loops: {yp}")

def solve_q4():
    """
    Q4: Develop general python function lagrange_interpolation(X, Y, x) [cite: 15-17].
    """
    print("\n--- Solution for Question 4 ---")
    print("The function 'lagrange_interpolation' has been defined in the Helper section.")
    print("Example usage:")
    X = [0, 1, 2]
    Y = [1, 3, 2]
    val = lagrange_interpolation(X, Y, 1.5)
    print(f"Interpolation for {list(zip(X,Y))} at x=1.5: {val}")

def solve_q5_q6():
    """
    Q5 & Q6: Evaluate at multiple values and store in a list[cite: 18, 19].
    """
    print("\n--- Solution for Question 5 & 6 ---")
    X = [1, 2, 4, 5]
    Y = [2, 3, 1, 4]
    
    # Define multiple evaluation points
    test_points = [1.5, 2.5, 3.5, 4.5]
    results = []
    
    print(f"Evaluating polynomial for nodes {X} at points: {test_points}")
    for tp in test_points:
        val = lagrange_interpolation(X, Y, tp)
        results.append(val)
        
    print(f"Resulting list of interpolated values: {results}")

def solve_q7():
    """
    Q7: f(x)=sin(x) at x=0, pi/4, pi/2. Compute absolute error at x=pi/6 [cite: 20-28].
    """
    print("\n--- Solution for Question 7 ---")
    # Define nodes in radians
    X = [0, np.pi/4, np.pi/2]
    Y = [np.sin(x) for x in X] # f(x) = sin(x)
    
    target_x = np.pi/6
    exact_val = np.sin(target_x)
    approx_val = lagrange_interpolation(X, Y, target_x)
    abs_error = abs(exact_val - approx_val)
    
    print(f"Nodes: 0, pi/4, pi/2")
    print(f"Target x: pi/6 ({target_x:.4f})")
    print(f"Exact sin(pi/6): {exact_val:.5f}")
    print(f"Lagrange Approximation: {approx_val:.5f}")
    print(f"Absolute Error: {abs_error:.5f}")

def solve_q8():
    """
    Q8: Compare user-defined Lagrange vs numpy.polyfit [cite: 29-32].
    """
    print("\n--- Solution for Question 8 ---")
    X = [1, 2, 3, 4]
    Y = [1, 4, 9, 16] # y = x^2
    target = 2.5
    
    # a) User defined
    user_val = lagrange_interpolation(X, Y, target)
    
    # b) Numpy polyfit (Degree = len(X)-1 for interpolation)
    deg = len(X) - 1
    coeffs = np.polyfit(X, Y, deg)
    numpy_val = np.polyval(coeffs, target)
    
    print(f"Data: y = x^2 at {X}")
    print(f"Target x: {target}")
    print(f"(a) User-defined Lagrange: {user_val}")
    print(f"(b) Numpy polyfit/polyval: {numpy_val}")
    print(f"Difference: {abs(user_val - numpy_val)}")

def solve_q9():
    """
    Q9: Use sympy to display symbolic form[cite: 33].
    """
    print("\n--- Solution for Question 9 ---")
    x = sp.symbols('x')
    X_nodes = [0, 1, 2]
    Y_nodes = [1, 3, 2]
    
    n = len(X_nodes)
    poly = 0
    
    # Construct symbolic polynomial
    for i in range(n):
        L_i = 1
        for j in range(n):
            if i != j:
                L_i *= (x - X_nodes[j]) / (X_nodes[i] - X_nodes[j])
        poly += Y_nodes[i] * L_i
        
    print(f"Nodes: {X_nodes}, Values: {Y_nodes}")
    print("Symbolic Lagrange Polynomial:")
    sp.pprint(sp.simplify(poly))

def solve_q10():
    """
    Q10: Plot polynomial and original data points[cite: 34].
    """
    print("\n--- Solution for Question 10 ---")
    X = [0, 1, 2, 4]
    Y = [1, 2, 0, 3]
    
    # Generate smooth x axis for plotting curve
    x_smooth = np.linspace(min(X), max(X), 100)
    y_smooth = [lagrange_interpolation(X, Y, xi) for xi in x_smooth]
    
    plt.figure()
    plt.plot(x_smooth, y_smooth, label='Lagrange Polynomial')
    plt.scatter(X, Y, color='red', zorder=5, label='Data Points')
    plt.title("Q10: Lagrange Interpolation Plot")
    plt.legend()
    plt.grid(True)
    plt.show()
    print("Plot generated.")

def solve_q11():
    """
    Q11: f(x)=sin(x) on [0, pi]. Plot f(x) and polynomial [cite: 35-39].
    """
    print("\n--- Solution for Question 11 ---")
    # Define equally spaced nodes
    nodes_x = np.linspace(0, np.pi, 5) # 5 nodes
    nodes_y = np.sin(nodes_x)
    
    # Smooth plotting data
    x_plot = np.linspace(0, np.pi, 100)
    y_exact = np.sin(x_plot)
    y_interp = [lagrange_interpolation(nodes_x, nodes_y, xi) for xi in x_plot]
    
    plt.figure()
    plt.plot(x_plot, y_exact, 'g--', label='Exact sin(x)')
    plt.plot(x_plot, y_interp, 'b-', label='Interpolated P(x)')
    plt.scatter(nodes_x, nodes_y, color='red', label='Nodes')
    plt.title("Q11: Sin(x) vs Interpolation")
    plt.legend()
    plt.grid(True)
    plt.show()
    print("Plot generated.")

def solve_q12():
    """
    Q12: f(x)=e^x on [0,1]. Plot absolute error |f(x) - Pn(x)| [cite: 40-44].
    """
    print("\n--- Solution for Question 12 ---")
    # Define nodes
    nodes_x = np.linspace(0, 1, 4) # 4 nodes
    nodes_y = np.exp(nodes_x)
    
    x_plot = np.linspace(0, 1, 100)
    exact_vals = np.exp(x_plot)
    interp_vals = np.array([lagrange_interpolation(nodes_x, nodes_y, xi) for xi in x_plot])
    
    error = np.abs(exact_vals - interp_vals)
    
    plt.figure()
    plt.plot(x_plot, error, color='purple')
    plt.title("Q12: Absolute Error |e^x - P(x)|")
    plt.xlabel("x")
    plt.ylabel("Error")
    plt.grid(True)
    plt.show()
    print("Error plot generated.")

def solve_q13():
    """
    Q13: Study effect of increasing nodes (Runge's Phenomenon-like study) [cite: 45-47].
    Plots error for different N.
    """
    print("\n--- Solution for Question 13 ---")
    # Function to test: f(x) = sin(x)
    x_smooth = np.linspace(0, np.pi, 100)
    y_exact = np.sin(x_smooth)
    
    plt.figure()
    
    # Compare N=3 and N=6 nodes
    for N in [3, 6]:
        nodes_x = np.linspace(0, np.pi, N)
        nodes_y = np.sin(nodes_x)
        
        y_interp = np.array([lagrange_interpolation(nodes_x, nodes_y, xi) for xi in x_smooth])
        error = np.abs(y_exact - y_interp)
        
        plt.plot(x_smooth, error, label=f'Error with {N} nodes')
        
    plt.title("Q13: Error vs Number of Nodes")
    plt.legend()
    plt.grid(True)
    plt.show()
    print("Comparison plot generated.")

def solve_q14():
    """
    Q14: n=7 data points (square function), plot curve and points [cite: 48-54].
    x: [0..6], y: [0, 1, 4, 9, 16, 25, 36]
    """
    print("\n--- Solution for Question 14 ---")
    X = [0, 1, 2, 3, 4, 5, 6]
    Y = [0, 1, 4, 9, 16, 25, 36]
    
    x_smooth = np.linspace(0, 6, 100)
    y_smooth = [lagrange_interpolation(X, Y, xi) for xi in x_smooth]
    
    plt.figure()
    plt.plot(x_smooth, y_smooth, label='Interpolated Curve')
    plt.scatter(X, Y, color='red', label='Data Points (y=x^2)')
    plt.title("Q14: Interpolation of Discrete Data")
    plt.legend()
    plt.grid(True)
    plt.show()
    print("Plot generated.")

def solve_q15():
    """
    Q15: f(x)=1/x with nodes 2.5, 3, 4. Plot P2(x) and f(x) [cite: 55-61].
    """
    print("\n--- Solution for Question 15 ---")
    # (a) Construct polynomial logic (handled by function)
    nodes_x = [2.5, 3, 4]
    nodes_y = [1/x for x in nodes_x]
    
    # (b) Evaluate at suitable points
    test_x = np.linspace(2.5, 4, 50)
    poly_vals = [lagrange_interpolation(nodes_x, nodes_y, xi) for xi in test_x]
    exact_vals = 1 / test_x
    
    # (c) Plot
    plt.figure()
    plt.plot(test_x, exact_vals, 'g--', label='f(x) = 1/x')
    plt.plot(test_x, poly_vals, 'b-', label='P2(x)')
    plt.scatter(nodes_x, nodes_y, color='red', label='Nodes')
    plt.title("Q15: Interpolating f(x)=1/x")
    plt.legend()
    plt.grid(True)
    plt.show()
    print("Plot generated.")

# ==========================================
# MAIN MENU DRIVER
# ==========================================

def menu():
    while True:
        print("\n" + "="*40)
        print("      NUMERICAL METHODS LAB 5 MENU      ")
        print("="*40)
        print("1.  Solve Q1: Simple Point Interpolation")
        print("2.  Solve Q2: Basis Polynomial Calculation")
        print("3.  Solve Q3: Nested Loops (No functions)")
        print("4.  Solve Q4: General Function Definition")
        print("5.  Solve Q5 & Q6: List Evaluation")
        print("7.  Solve Q7: Sin(x) Error Analysis")
        print("8.  Solve Q8: Compare with Numpy Polyfit")
        print("9.  Solve Q9: Symbolic Representation (Sympy)")
        print("10. Solve Q10: Simple Plotting")
        print("11. Solve Q11: Sin(x) Function Plotting")
        print("12. Solve Q12: Error Plotting (e^x)")
        print("13. Solve Q13: Effect of Node Count")
        print("14. Solve Q14: Large Dataset Plotting (n=7)")
        print("15. Solve Q15: 1/x Interpolation")
        print("0.  Exit")
        print("="*40)
        
        try:
            choice = int(input("Enter Question Number (0 to Exit): "))
            
            if choice == 0:
                print("Exiting...")
                break
            elif choice == 1: solve_q1()
            elif choice == 2: solve_q2()
            elif choice == 3: solve_q3()
            elif choice == 4: solve_q4()
            elif choice == 5 or choice == 6: solve_q5_q6()
            elif choice == 7: solve_q7()
            elif choice == 8: solve_q8()
            elif choice == 9: solve_q9()
            elif choice == 10: solve_q10()
            elif choice == 11: solve_q11()
            elif choice == 12: solve_q12()
            elif choice == 13: solve_q13()
            elif choice == 14: solve_q14()
            elif choice == 15: solve_q15()
            else:
                print("Invalid choice, please try again.")
        except ValueError:
            print("Please enter a valid integer.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    menu()