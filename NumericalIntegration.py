import sympy as sp

def simpson_integral():
    x = sp.symbols('x')
    function = input("Enter a function of x: ")
    simplified_function = sp.sympify(function)
    a = float(input("Choose a lower bound: "))
    b = float(input("Choose an upper bound: "))
    n = int(input("Enter an even number of subdivisions: "))
    
    if n % 2 != 0:
        print("The number of subdivisions must be even for Simpson's Rule.")
        return
   
    h = (b-a)/n
    f = sp.lambdify(x, simplified_function)
    integral = f(a) + f(b)

    for i in range (1, n):
        xi = a+i*h
        if i % 2 == 0:
            integral += 2 * f(xi)
        else:
            integral += 4 * f(xi)
    integral *= h/3
    print(f"{integral}")
simpson_integral()
    