import ast

eleccion = input("""

SELECCIONE UNA OPCION:
[1]: CAMBIOS SECCION TRANSVERSAL
[2]: UNIONES CAMBIO DE SECCION BRUSCO
[3]: UNIONES

""")

# SI SE ELIGE CALCULAR CAMBIOS EN SECCION TRANVERSAL
if eleccion == '1':
    segunda_eleccion = input("""
    PARA CALCULAR CAMBIOS EN SECCION TRANSVERSAL SELECCIONE:
    [A]: AMPLIACION
    [R]: REDUCCION
    """)
    if segunda_eleccion == 'A' or 'a':
        A1 = ast.literal_eval(input('Ingresee el valor de A1: '))
        A2 = ast.literal_eval(input('Ingrese el valor de A2: '))
        p = ast.literal_eval(input('Ingrese la densidad p: '))

        X2 = (A2/A1-1)**2
        X1 = (1-A1/A2)**2
        Rshock = X2*p/(2*(A1**2))
        print(f'El valor de X1 es {X1}')
        print(f'El valor de X2 es {X2}')
        print(f'El valor de Rshock  es {Rshock}')
    else:
        A1 = ast.literal_eval(input('Ingresee el valor de A1: '))
        A2 = ast.literal_eval(input('Ingrese el valor de A2: '))
        p = ast.literal_eval(input('Ingrese la densidad p: '))
        
        X2 = 0.5*(1-A2/A1)**2
        Rshock = X2*p/(2*A1**2)
        print(f'El valor de X2 es {X2}')
        print(f'El valor de Rshock  es {Rshock}')

# SI SE ELIGE CALCULAR UNIONES CAMBIO DE SECCION BRUSCO
elif eleccion == '2':
    A1 = ast.literal_eval(input('Ingresee el valor de A1: '))
    A2 = ast.literal_eval(input('Ingrese el valor de A2: '))
    p = ast.literal_eval(input('Ingrese la densidad p: '))

    X2 = 0.5*(1+2.5*A2/A1)**2
    Rshock = X2*p/(2*A1**2)
    print(f'El valor de X2 es {X2}')
    print(f'El valor de Rshock  es {Rshock}')

# SI SE ELIGE CALCULAR EN UNIONES
elif eleccion == '3':
    u1 = ast.literal_eval(input('Ingresee el valor de U1: '))
    u2 = ast.literal_eval(input('Ingrese el valor de U2: '))
    p = ast.literal_eval(input('Ingrese la densidad p: '))

    X2 = 0.5*(1+2.5*u2/u1)
    Rshock = X2*p/(2*u1**2)
    print(f'El valor de X2 es {X2}')
    print(f'El valor de Rshock  es {Rshock}')