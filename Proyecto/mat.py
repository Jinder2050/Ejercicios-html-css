# import math

# e=4
# D=3


# f =1 / ((1.74 - 2 * math.log(2 * e / D)) ** 2 )

# print(round(f,4))


# import numpy as np
# # Constantes
# D = 3
# e = 4

# # Despejar f
# result = np.power(1/(1.74-2*np.log(2*e/D)),2)

# # Mostrar resultado
# print("El resultado de la formula es:", result)

# import math

# Re = 0
# e = 0
# D = 0

# f = 0.25 / (math.log10(((e / 3.71*D) + (5.74/Re**0.9))) ** 2)

# print(round(f,4))
# =============================================================================

import numpy as np
import math

def friccion(f, e, D, Re):
    return 1/np.sqrt(f) - (-2 * np.log((2 * e / D) / 3.71 + 2.51 / (Re * np.sqrt(f))))

def biseccion(a, b, epsilon, e, D, Re):
    while abs(b - a) > epsilon:
        c = (a + b) / 2
        f_c = friccion(c, e, D, Re)
        if f_c == 0:
            return c
        f_a = friccion(a, e, D, Re)
        if f_a * f_c < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

# Ingresa los valores de e y D
e = float(input("Ingresa el valor de e: "))
D = float(input("Ingresa el valor de D: "))
Re = float(input("Ingresa el valor de Re: "))


valor_f = biseccion(0, 1000, 0.001, e, D, Re)
print("El valor de f es:", valor_f)


# ===============================================================


# import math

# e = 5
# D = 10
# Re = 10000.0
# term = 2.51 / (Re * math.sqrt(f))
# derecha = -2.0 * math.log((e / D) / 3.71 + term)
# izquierda = 1.0 / math.sqrt(f)
# from scipy.optimize import fsolve

# def equation(f):
#     term = 2.51 / (Re * math.sqrt(f))
#     derecha = -2.0 * math.log((e / D) / 3.71 + term)
#     izquierda = 1.0 / math.sqrt(f)
#     return izquierda - derecha

# f_solution = fsolve(equation, 0.01)

# print(f_solution)