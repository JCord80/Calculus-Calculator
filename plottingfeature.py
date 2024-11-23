import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def graph():
    x, y, t, r, theta = sp.symbols('x y t r theta')
    
    coordinates = input("What type of coordinates would you like to graph? ")
    if coordinates == "cartesian":
        type_of_function = input("How many variables does your function have? ")
        if type_of_function == "1":
            function_singlevar = sp.sympify(input("Enter a function of x: "))
            a = float(input("Least x-value: "))
            b = float(input("Greatest x-value: "))
            d = float(input("Least y-value: "))
            f = float(input("Greatest y-value: "))

            x_vals = np.linspace(a, b)
            func_lambdified = sp.lambdify(x, function_singlevar)
            y_vals = func_lambdified(x_vals)

            plt.figure(figsize=(8, 6))
            plt.plot(x_vals, y_vals)
            plt.xlim(a, b)
            plt.ylim(d, f)
            plt.title("Graph of the Function")
            plt.xlabel("x")
            plt.ylabel("f(x)")
            plt.grid(True)
            plt.show()

        if type_of_function == "2":
            function_multivar = sp.sympify(input("Enter a function of x and y: "))
            g = float(input("Least x-value: "))
            h = float(input("Greatest x-value: "))
            i = float(input("Least y-value: "))
            j = float(input("Greatest y-value: "))
            k = float(input("Least z-value: "))
            l = float(input("Greatest z-value: "))

            x_vals = np.linspace(g, h)
            y_vals = np.linspace(i, j)
            x_mesh, y_mesh = np.meshgrid(x_vals, y_vals)
            func_lambdified = sp.lambdify((x, y), function_multivar)
            z_vals = func_lambdified(x_mesh, y_mesh)

            fig = plt.figure(figsize=(10, 8))
            ax = fig.add_subplot(111, projection='3d')
            ax.plot_surface(x_mesh, y_mesh, z_vals)
            ax.set_xlim(g, h)
            ax.set_ylim(i, j)
            ax.set_zlim(k, l)
            ax.set_title("3D Graph of the Function")
            ax.set_xlabel("x")
            ax.set_ylabel("y")
            ax.set_zlabel("z")
            plt.show()

        else:
            print("You can only plot in 2 or 3 dimensions")
    if coordinates == "parametric":
        xfunction = sp.sympify(input("Enter a function of t for x: "))
        yfunction = sp.sympify(input("Enter a function of t for y: "))
        xvalues = sp.lambdify(t, xfunction)
        yvalues = sp.lambdify(t, yfunction)
        tmin = sp.sympify(input("Least t-value: "))
        tmax = sp.sympify(input("Greatest t-value: "))
        tmin = float(tmin.evalf())
        tmax = float(tmax.evalf())
        tvalues = np.linspace(tmin, tmax)
        xmin = float(input("Least x-value: "))
        xmax = float(input("Greatest x-value: "))
        ymin = float(input("Least y-value: "))
        ymax = float(input("Greatest y-value: "))
        xgraph = xvalues(tvalues)
        ygraph = yvalues(tvalues)
        plt.figure(figsize=(10, 10))
        plt.plot(xgraph, ygraph)
        plt.xlim(xmin, xmax)
        plt.ylim(ymin, ymax)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True)
        plt.show()
    else:
        print("Unsupported coordinate type.")
graph()


