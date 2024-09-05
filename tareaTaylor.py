import math

# Función para calcular la serie de Taylor de e^x
def taylor_exp(x, n_terms):
    result = 0
    for n in range(n_terms):
        result += x**n / math.factorial(n)
    return result

# Función para calcular la serie de Taylor de sin(x)
def taylor_sin(x, n_terms):
    result = 0
    for n in range(n_terms):
        result += ((-1)**n * x**(2*n + 1)) / math.factorial(2*n + 1)
    return result

# Ejemplo para e^x con x = 1 y 5 términos
x_exp = 1
n_terms_exp = 5
print(f"Aproximación de e^({x_exp}) con {n_terms_exp} términos: {taylor_exp(x_exp, n_terms_exp)}")
print(f"Valor real de e^({x_exp}): {math.exp(x_exp)}\n")

# Ejemplo para sin(x) con x = pi/6 (30 grados) y 5 términos
x_sin = math.pi / 6
n_terms_sin = 5
print(f"Aproximación de sin({x_sin}) con {n_terms_sin} términos: {taylor_sin(x_sin, n_terms_sin)}")
print(f"Valor real de sin({x_sin}): {math.sin(x_sin)}")
