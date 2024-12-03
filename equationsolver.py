import sympy as sp
def equationsolver():
    x = sp.symbols('x')
    left = sp.sympify(input("Left side of equation: "))
    right = sp.sympify(input("Right side of equation: "))
    equation = sp.Eq(left, right)
    solution = sp.solve(equation, x)
    if solution:
        print(solution)
    else:
        print("No solution")
equationsolver()
def system():
    variables = sp.symbols(input("Variables: "))
    number = int(input("How many equations would you like to solve? "))
    equations = []
    for i in range (number):
        eq = input("Enter an equation: ")
        equations.append(sp.sympify(eq))
    solutions = sp.solve(equations, variables)
    if solutions: 
        for i in solutions:
            print(f"{variables}={solutions[variables]}")
    else:
        print("No solutions")
