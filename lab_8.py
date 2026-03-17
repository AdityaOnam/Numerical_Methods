import numpy as np
import matplotlib.pyplot as plt

def exact_val_q1():
    # Integral of |2x - 1| from -2 to 1
    # Split at x = 0.5: integral from -2 to 0.5 of (1-2x) + integral from 0.5 to 1 of (2x-1)
    # Area 1: [x - x^2] from -2 to 0.5 = (0.5 - 0.25) - (-2 - 4) = 0.25 + 6 = 6.25
    # Area 2: [x^2 - x] from 0.5 to 1 = (1 - 1) - (0.25 - 0.5) = 0.25
    return 6.5

def simpson_13(f, a, b, n):
    """Implementation of Composite Simpson's 1/3 Rule."""
    if n % 2 != 0: n += 1  # n must be even
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    integral = h/3 * (y[0] + y[-1] + 4*np.sum(y[1:-1:2]) + 2*np.sum(y[2:-2:2]))
    return integral

def simpson_38(f, a, b, n):
    """Implementation of Composite Simpson's 3/8 Rule."""
    if n % 3 != 0: n = (n // 3 + 1) * 3  # n must be multiple of 3
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    # Weights for 3/8 rule: 1, 3, 3, 2, 3, 3, 2 ... 1
    weights = np.ones(n + 1)
    weights[1:-1] = 3
    weights[3:-1:3] = 2
    return (3 * h / 8) * np.sum(weights * y)

def trapezoidal(f, a, b, n):
    """Implementation of Composite Trapezoidal Rule."""
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    return (h / 2) * (y[0] + y[-1] + 2 * np.sum(y[1:-1]))

def hermite_interpolation(x_pts, y_pts, dy_pts, target_x):
    """Constructs and evaluates Hermite Divided Difference Table[cite: 21, 28]."""
    n = len(x_pts)
    z = np.zeros(2 * n)
    Q = np.zeros((2 * n, 2 * n))
    
    # Step 1: Initialize the table with repeated x values and f(x) [cite: 13, 27]
    for i in range(n):
        z[2*i] = z[2*i+1] = x_pts[i]
        Q[2*i][0] = Q[2*i+1][0] = y_pts[i]
        Q[2*i+1][1] = dy_pts[i]  # First derivative given [cite: 14, 27]
        if i != 0:
            Q[2*i][1] = (Q[2*i][0] - Q[2*i-1][0]) / (z[2*i] - z[2*i-1])
            
    # Step 2: Compute remaining Divided Differences [cite: 21, 28]
    for i in range(2, 2 * n):
        for j in range(2, i + 1):
            Q[i][j] = (Q[i][j-1] - Q[i-1][j-1]) / (z[i] - z[i-j])
            
    # Step 3: Evaluate the polynomial at target_x [cite: 24, 31]
    val = Q[0][0]
    prod = 1.0
    for i in range(1, 2 * n):
        prod *= (target_x - z[i-1])
        val += Q[i][i] * prod
    return val, Q

def main():
    while True:
        print("\n--- Numerical Methods Lab-8 Menu ---")
        print("1. Q1: Integral of |2x-1| (-2 to 1)")
        print("2. Q2/Q3: Hermite Interpolation (Divided Differences)")
        print("3. Q4: Integral of ln(1+x) (0 to 2)")
        print("4. Q5: Integral of sin(x) (0 to pi)")
        print("5. Q6: Integral of 1/(1+x^2) (0 to 3)")
        print("6. Q7: Compare Methods for e^(-x^2)")
        print("7. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            f = lambda x: np.abs(2*x - 1)
            h = 0.5 [cite: 6]
            n = int((1 - (-2)) / h)
            res_13 = simpson_13(f, -2, 1, n) [cite: 7]
            exact = exact_val_q1() [cite: 9]
            print(f"Simpson's 1/3 result: {res_13}")
            print(f"Exact value: {exact}")
            print(f"Error: {abs(exact - res_13)}")

        elif choice == '2':
            # Example Data from Q3 [cite: 27]
            x_data = np.array([0, 1, 2])
            y_data = np.array([1, 2, 0])
            dy_data = np.array([0, 1, -1])
            target = 1.5 [cite: 31]
            
            val, table = hermite_interpolation(x_data, y_data, dy_data, target)
            print(f"Hermite value at x={target}: {val}")
            
            # Plotting [cite: 25, 32]
            x_range = np.linspace(min(x_data), max(x_data), 100)
            y_poly = [hermite_interpolation(x_data, y_data, dy_data, xi)[0] for xi in x_range]
            plt.plot(x_range, y_poly, label="Hermite Poly")
            plt.scatter(x_data, y_data, color='red', label="Data points")
            plt.title("Hermite Interpolation")
            plt.legend()
            plt.show()

        elif choice == '3':
            f = lambda x: np.log(1 + x)
            n = int(2 / 0.25) # h=0.25 [cite: 35]
            res = trapezoidal(f, 0, 2, n) [cite: 36]
            exact = (3 * np.log(3) - 2) [cite: 37]
            print(f"Trapezoidal Result: {res}")
            print(f"Exact Value: {exact}")
            print(f"Absolute Error: {abs(exact - res)}") [cite: 38]

        elif choice == '4':
            f = lambda x: np.sin(x)
            h1, h2 = np.pi/6, np.pi/12 [cite: 44, 45]
            n1, n2 = int(np.pi/h1), int(np.pi/h2)
            res1 = simpson_13(f, 0, np.pi, n1)
            res2 = simpson_13(f, 0, np.pi, n2)
            print(f"Simpson 1/3 (h=pi/6): {res1}, Error: {abs(2 - res1)}") [cite: 46, 47]
            print(f"Simpson 1/3 (h=pi/12): {res2}, Error: {abs(2 - res2)}")

        elif choice == '5':
            f = lambda x: 1 / (1 + x**2) [cite: 50]
            n = int(3 / 0.25) [cite: 52]
            res = simpson_38(f, 0, 3, n) [cite: 51]
            exact = np.arctan(3) [cite: 53]
            print(f"Simpson's 3/8 Result: {res}")
            print(f"Exact Value: {exact}")
            print(f"Absolute Error: {abs(exact - res)}") [cite: 54]

        elif choice == '6':
            f = lambda x: np.exp(-x**2) [cite: 62]
            h = 0.1 [cite: 61]
            n = int(1 / h)
            t_res = trapezoidal(f, 0, 1, n) [cite: 58]
            s13_res = simpson_13(f, 0, 1, n) [cite: 59]
            s38_res = simpson_38(f, 0, 1, n) [cite: 60]
            print(f"Trapezoidal: {t_res}")
            print(f"Simpson's 1/3: {s13_res}")
            print(f"Simpson's 3/8: {s38_res}") [cite: 63]

        elif choice == '7':
            break
        else:
            print("Invalid Choice!")

if __name__ == "__main__":
    main()