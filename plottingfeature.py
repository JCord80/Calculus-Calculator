import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def graph():
    x, y, t, r, θ = sp.symbols('x y t r θ')
    
    coordinates = input("What type of coordinates would you like to graph? ")
    if coordinates == "cartesian":
        type_of_function = input("How many variables does your function have? ")
        if type_of_function == "1":
            function_singlevar = sp.sympify(input("Enter a function of x: "))
            xmin = float(input("Least x-value: "))
            xmax = float(input("Greatest x-value: "))  
            ymin = float(input("Least y-value: "))
            ymax = float(input("Greatest y-value: "))
            xvals = np.linspace(xmin, xmax, 10000000)
            lambdified = sp.lambdify(x, function_singlevar)
            yvals = lambdified(xvals)
            yvals = np.where(np.abs(yvals) > 1000000, np.nan, yvals)
            plt.figure(figsize=(8, 6))
            plt.plot(xvals, yvals)
            plt.xlim(xmin, xmax)
            plt.ylim(ymin, ymax)
            plt.title("Graph of the Function")
            plt.xlabel("x")
            plt.ylabel("f(x)")
            plt.grid(True)
            plt.show()
        if type_of_function == "2":
            function_multivar = sp.sympify(input("Enter a function of x and y: "))
            xmin = float(input("Least x-value: "))
            xmax = float(input("Greatest x-value: "))
            ymin = float(input("Least y-value: "))
            ymax = float(input("Greatest y-value: "))
            zmin = float(input("Least z-value: "))
            zmax = float(input("Greatest z-value: "))
            xvals = np.linspace(xmin, xmax, 100)
            yvals = np.linspace(ymin, ymax, 100)
            yvals = np.where(np.abs(yvals) > 1000000, np.nan, yvals)
            xmesh, ymesh = np.meshgrid(xvals, yvals)
            lambdified = sp.lambdify((x, y), function_multivar)
            zvals = lambdified(xmesh, ymesh)
            fig = plt.figure(figsize=(10, 8))
            ax = fig.add_subplot(111, projection='3d')
            ax.plot_surface(xmesh, ymesh, zvals)
            ax.set_xlim(xmin, xmax)
            ax.set_ylim(ymin, ymax)
            ax.set_zlim(zmin, zmax)
            ax.set_xlabel("x")
            ax.set_ylabel("y")
            ax.set_zlabel("z")
            plt.show()
        else:
            print("You can only plot in 2 or 3 dimensions")
    if coordinates == "parametric":
        xfunction = sp.sympify(input("Enter a function of t for x: "))
        yfunction = sp.sympify(input("Enter a function of t for y: "))
        xvals = sp.lambdify(t, xfunction)
        yvals = sp.lambdify(t, yfunction)
        tmin = sp.sympify(input("Least t-value: "))
        tmax = sp.sympify(input("Greatest t-value: "))
        tmin = float(tmin.evalf())
        tmax = float(tmax.evalf())
        tvals = np.linspace(tmin, tmax, 10000)
        xmin = float(input("Least x-value: "))
        xmax = float(input("Greatest x-value: "))
        ymin = float(input("Least y-value: "))
        ymax = float(input("Greatest y-value: "))
        xgraph = xvals(tvals)
        ygraph = yvals(tvals)
        plt.figure(figsize=(10, 10))
        plt.plot(xgraph, ygraph)
        plt.xlim(xmin, xmax)
        plt.ylim(ymin, ymax)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True)
        plt.show()
    if coordinates == "polar":
        rexpression = sp.sympify(input("r="))
        rfunction = sp.lambdify(θ, rexpression)
        θvals = np.linspace(0, 100 * np.pi, 10000)
        rvals = rfunction(θvals)
        xvals = rvals * np.cos(θvals)
        yvals = rvals * np.sin(θvals)
        xmin = float(input("Least x-value: "))
        xmax = float(input("Greatest x-value: "))
        ymin = float(input("Least y-value: "))
        ymax = float(input("Greatest y-value: "))
        plt.figure(figsize=(10, 10))
        plt.plot(xvals, yvals)
        plt.xlim(xmin, xmax)
        plt.ylim(ymin, ymax)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True)
        plt.show() 
graph()


