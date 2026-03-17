import numpy as np
import matplotlib.pyplot as plt

# --- Integration Rule Implementations ---

def trapezoidal(f, a, b, n):
    """Composite Trapezoidal Rule[cite: 35, 58]."""
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    return (h / 2) * (y[0] + y[-1] + 2 * np.sum(y[1:-1]))

def simpson_13(f, a, b, n):
    """Composite Simpson's 1/3 Rule[cite: 7, 43, 59]."""
    if n % 2 != 0: n += 1  # Must be even
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    return (h/3) * (y[0] + y[-1] + 4*np.sum(y[1:-1:2]) + 2*np.sum(y[2:-2:2]))

def simpson_38(f, a, b, n):
    """Composite Simpson's 3/8 Rule[cite: 51, 60]."""
    if n % 3 != 0: n = (n // 3 + 1) * 3  # Must be multiple of 3
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    integral = y[0] + y[-1]
    for i in range(1, n):
        integral += 2 * y[i] if i % 3 == 0 else 3 * y[i]
    return (3 * h / 8) * integral

# --- Hermite Interpolation Implementation ---

def hermite_interpolation(x_pts, y_pts, dy_pts, target_x):
    """Constructs Divided Difference Table and evaluates Polynomial[cite: 21, 23, 28]."""
    n = len(x_pts)
    z, Q = np.zeros(2 * n), np.zeros((2 * n, 2 * n))
    for i in range(n):
        z[2*i] = z[2*i+1] = x_pts[i]
        Q[2*i][0] = Q[2*i+1][0] = y_pts[i]
        Q[2*i+1][1] = dy_pts[i]  # f'(x) [cite: 14, 27]
        if i != 0:
            Q[2*i][1] = (Q[2*i][0] - Q[2*i-1][0]) / (z[2*i] - z[2*i-1])
    for j in range(2, 2 * n):
        for i in range(j, 2 * n):
            Q[i][j] = (Q[i][j-1] - Q[i-1][j-1]) / (z[i] - z[i-j])
    
    # Evaluation
    val, prod = Q[0][0], 1.0
    for i in range(1, 2 * n):
        prod *= (target_x - z[i-1])
        val += Q[i][i] * prod
    return val, Q

# --- Main Menu Driven Program ---

def main():
    while True:
        print("\n" + "="*45)
        print("   NUMERICAL METHODS LAB-8 MENU (Q1-Q9)")
        print("="*45)
        print("1. Q1: Integral of |2x-1| (-2 to 1)")
        print("2. Q2/3: Hermite Interpolation (Data Q3)")
        print("3. Q4: Integral of ln(1+x) (0 to 2)")
        print("4. Q5: Integral of sin(x) (0 to pi)")
        print("5. Q6: Integral of 1/(1+x^2) (0 to 3)")
        print("6. Q7: Method Comparison (e^-x^2)")
        print("7. Q8: Convergence Study (Error vs h)")
        print("8. Q9: Hybrid Combined Rules (-1 to 1)")
        print("9. Exit")
        
        choice = input("\nSelect a question to run: ")

        if choice == '1':
            f = lambda x: np.abs(2*x - 1)
            n = int(3 / 0.5) # h=0.5 [cite: 6]
            res = simpson_13(f, -2, 1, n)
            exact = 6.5 # [cite: 9]
            print(f"Simpson 1/3 Result: {res}")
            print(f"Exact Value: {exact}\nAbsolute Error: {abs(exact - res)}")

        elif choice == '2':
            # Data from Q3 [cite: 27]
            x_d = np.array([0, 1, 2]); y_d = np.array([1, 2, 0]); dy_d = np.array([0, 1, -1])
            target = 1.5 [cite: 31]
            val, _ = hermite_interpolation(x_d, y_d, dy_d, target)
            print(f"Hermite value at x={target}: {val}")
            
            # Plotting [cite: 32]
            xr = np.linspace(0, 2, 100)
            yr = [hermite_interpolation(x_d, y_d, dy_d, xi)[0] for xi in xr]
            plt.plot(xr, yr, label="Hermite Poly"); plt.scatter(x_d, y_d, color='red')
            plt.title("Hermite Interpolation (Q3)"); plt.legend(); plt.show()

        elif choice == '3':
            f = lambda x: np.log(1 + x) # [cite: 34]
            n = int(2 / 0.25) # h=0.25 [cite: 35]
            res = trapezoidal(f, 0, 2, n)
            exact = 3*np.log(3) - 2 # [cite: 37]
            print(f"Trapezoidal: {res}\nError: {abs(exact - res)}")

        elif choice == '4':
            f = lambda x: np.sin(x) # [cite: 42]
            for h_val in [np.pi/6, np.pi/12]: # [cite: 44, 45]
                n = int(np.round(np.pi/h_val))
                res = simpson_13(f, 0, np.pi, n)
                print(f"h={h_val:.4f} | Res: {res:.6f} | Error: {abs(2-res):.6e}")

        elif choice == '5':
            f = lambda x: 1 / (1 + x**2) # [cite: 50]
            n = int(3 / 0.25) # h=0.25 [cite: 52]
            res = simpson_38(f, 0, 3, n)
            print(f"Simpson 3/8: {res}\nExact: {np.arctan(3)}")

        elif choice == '6':
            f = lambda x: np.exp(-x**2) # [cite: 62]
            n = int(1 / 0.1) # h=0.1 [cite: 61]
            print(f"Trap: {trapezoidal(f, 0, 1, n)}")
            print(f"S13 : {simpson_13(f, 0, 1, n)}")
            print(f"S38 : {simpson_38(f, 0, 1, n)}")

        elif choice == '7':
            # Q8: Convergence Behavior [cite: 65]
            f = lambda x: x**0.5 # [cite: 66, 67]
            h_vals = [0.5, 0.25, 0.125] # 
            exact = 2/3
            err_t, err_s = [], []
            for h in h_vals:
                n = int(1/h)
                err_t.append(abs(exact - trapezoidal(f, 0, 1, n)))
                err_s.append(abs(exact - simpson_13(f, 0, 1, n)))
            plt.loglog(h_vals, err_t, '-o', label='Trapezoidal')
            plt.loglog(h_vals, err_s, '-s', label='Simpson 1/3')
            plt.xlabel('h'); plt.ylabel('Error'); plt.legend(); plt.show() # [cite: 70]

        elif choice == '8':
            # Q9: Hybrid Rule 
            f = lambda x: 1 / (1 + x**2) # [cite: 73]
            # Split [-1, 1] into segments: [-1, -0.6], [-0.6, 0.6], [0.6, 1.0]
            v_trap = trapezoidal(f, -1, -0.6, 1) # 
            v_s38  = simpson_38(f, -0.6, 0.6, 3) # 
            v_s13  = simpson_13(f, 0.6, 1, 2)    # 
            print(f"Hybrid Total: {v_trap + v_s38 + v_s13}")
            print(f"Exact Value : {np.arctan(1) - np.arctan(-1)}")

        elif choice == '9':
            print("Exiting...")
            break
        else:
            print("Invalid Option!")

if __name__ == "__main__":
    main()