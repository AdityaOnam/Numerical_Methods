import numpy as np

def f(x, y, z):
    """Defines dy/dx"""
    return y + z

def g(x, y, z):
    """Defines dz/dx"""
    return x - z

def euler_method(x0, y0, z0, h, steps):
    print(f"\n--- Euler's Method ---")
    x, y, z = x0, y0, z0
    for i in range(steps):
        # Update values using the slope at the BEGINNING of the interval
        y_new = y + h * f(x, y, z)
        z_new = z + h * g(x, y, z)
        x += h
        y, z = y_new, z_new
        print(f"Step {i+1}: x = {x:.1f}, y = {y:.5f}, z = {z:.5f}")
    return y, z

def heun_method(x0, y0, z0, h, steps):
    print(f"\n--- Heun's Method (Modified Euler) ---")
    x, y, z = x0, y0, z0
    for i in range(steps):
        # Predictor step (Standard Euler)
        k1y = f(x, y, z)
        k1z = g(x, y, z)
        
        y_pred = y + h * k1y
        z_pred = z + h * k1z
        
        # Corrector step (Average of slopes)
        k2y = f(x + h, y_pred, z_pred)
        k2z = g(x + h, y_pred, z_pred)
        
        y = y + (h/2) * (k1y + k2y)
        z = z + (h/2) * (k1z + k2z)
        x += h
        print(f"Step {i+1}: x = {x:.1f}, y = {y:.5f}, z = {z:.5f}")
    return y, z

def rk2_method(x0, y0, z0, h, steps):
    print(f"\n--- Runge-Kutta 2nd Order (RK2) ---")
    # Note: Heun's is a type of RK2. Here we use the Midpoint method variation.
    x, y, z = x0, y0, z0
    for i in range(steps):
        k1y = h * f(x, y, z)
        k1z = h * g(x, y, z)
        
        k2y = h * f(x + h/2, y + k1y/2, z + k1z/2)
        k2z = h * g(x + h/2, y + k1y/2, z + k1z/2)
        
        y += k2y
        z += k2z
        x += h
        print(f"Step {i+1}: x = {x:.1f}, y = {y:.5f}, z = {z:.5f}")
    return y, z

def rk4_method(x0, y0, z0, h, steps):
    print(f"\n--- Runge-Kutta 4th Order (RK4) ---")
    x, y, z = x0, y0, z0
    for i in range(steps):
        k1y = h * f(x, y, z)
        k1z = h * g(x, y, z)
        
        k2y = h * f(x + h/2, y + k1y/2, z + k1z/2)
        k2z = h * g(x + h/2, y + k1y/2, z + k1z/2)
        
        k3y = h * f(x + h/2, y + k2y/2, z + k2z/2)
        k3z = h * g(x + h/2, y + k2y/2, z + k2z/2)
        
        k4y = h * f(x + h, y + k3y, z + k3z)
        k4z = h * g(x + h, y + k3y, z + k3z)
        
        y += (k1y + 2*k2y + 2*k3y + k4y) / 6
        z += (k1z + 2*k2z + 2*k3z + k4z) / 6
        x += h
        print(f"Step {i+1}: x = {x:.1f}, y = {y:.5f}, z = {z:.5f}")
    return y, z

def main():
    # Problem Constraints
    x0, y0, z0 = 0, 1, 0
    h = 0.1
    target_x = 0.2
    steps = int(target_x / h)

    while True:
        print("\n--- Numerical ODE Solver Menu ---")
        print("1. Euler's Method")
        print("2. Heun's Method (Modified Euler)")
        print("3. RK2 (Midpoint Method)")
        print("4. RK4 (Fourth Order)")
        print("5. Run All and Compare")
        print("6. Exit")
        
        choice = input("Select a method (1-6): ")
        
        if choice == '1': euler_method(x0, y0, z0, h, steps)
        elif choice == '2': heun_method(x0, y0, z0, h, steps)
        elif choice == '3': rk2_method(x0, y0, z0, h, steps)
        elif choice == '4': rk4_method(x0, y0, z0, h, steps)
        elif choice == '5':
            euler_method(x0, y0, z0, h, steps)
            heun_method(x0, y0, z0, h, steps)
            rk2_method(x0, y0, z0, h, steps)
            rk4_method(x0, y0, z0, h, steps)
        elif choice == '6': break
        else: print("Invalid choice.")

if __name__ == "__main__":
    main()