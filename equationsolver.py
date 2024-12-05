import sympy as sp

def equation_solver():
    print("Enter your equation in terms of x (e.g., x**2 + 2*x - 3 = 0):")
    equation = sp.sympify(input("Equation: "))
    x = sp.symbols('x')    
    solutions = sp.solve(equation, x)
    if solutions:
        print(solutions)
    else:
        print("No solutions.")
equation_solver()