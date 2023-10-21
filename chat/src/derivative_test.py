import sympy as sp
# Define symbolic variables
x, y = sp.symbols('x y')

# Define a mathematical expression
expr = sp.sin(x**2) + 2*x*y + y**2

expr = sp.Add(sp.cos(x**3),expr)

f_d = sp.diff(expr,x)
# Convert the expression to LaTeX
latex_expr = sp.latex(f_d)


print(latex_expr)
