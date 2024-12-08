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

# str = "1,2,3,4,5,"
# g = 0
# for l in range(str.count(",")):
#     y = str.index(",",g)
#     z = str[g:y]
#     print(z)
#     g=y+1


# def enter():
#     try:
#         if "{" in answer["text"]:
#             answer["text"]=answer["text"].replace("{", ",")
#             answer["text"]=answer["text"].replace("}", ",")
#         if "^" in expr["text"]:
#             expr["text"]=expr["text"].replace("^", "**")
#         if "√" in expr["text"]:
#             expr["text"]=expr["text"].replace("√", "sqrt")
#         if ("e") in expr["text"]:
#             expr["text"]=expr["text"].replace("e", "E")
#         if "π" in expr["text"]:
#             expr["text"]=expr["text"].replace("π","pi")
#         save = expr["text"]
#         if ("x" in save) and ("x" not in answer["text"]):
#             if "," in answer:
#                 r=[]
#                 g = 0
#                 for l in range(answer["text"].count(",")):
#                     y = answer["text"].index(",",g)
#                     eqchunk = str[g:y]
#                     z = sp.symbols('z')
#                     d = sp.sympify(eqchunk)
#                     func = sp.lambdify(z,d)
#                     r.append(str(func(1)))
#                     g=y+1
#                 answer["text"] = str(r)
#             else:
#                 z = sp.symbols('z')
#                 y = sp.sympify(answer["text"])
#                 func = sp.lambdify(z,y)
#                 answer["text"] = str(func(1))
#         elif ("x" in save) and ("x" in answer):
#             answer["text"] = "Can't Evaluate"
#         else:
#             z = sp.symbols('z')
#             y = sp.sympify(save)
#             func = sp.lambdify(z,y)
#             answer["text"] = str(func(1))
#             expr["text"] = ""
#             history = hist(save,answer["text"])
#             history.pack()
#     except Exception as e:
#         answer["text"] = "Error"