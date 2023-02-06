import ast
import tkinter as tk
from tkinter import messagebox

def calculate():
    eleccion = option.get()

    # SI SE ELIGE CALCULAR CAMBIOS EN SECCION TRANVERSAL
    if eleccion == '1':
        segunda_eleccion = option2.get()
        if segunda_eleccion == 'A':
            A1 = ast.literal_eval(entry1.get())
            A2 = ast.literal_eval(entry2.get())
            p = ast.literal_eval(entry3.get())

            X2 = (A2/A1-1)**2
            X1 = (1-A1/A2)**2
            Rshock = X2*p/(2*(A1**2))
            result.config(text=f'El valor de X1 es {X1}\nEl valor de X2 es {X2}\nEl valor de Rshock  es {Rshock}')
        else:
            A1 = ast.literal_eval(entry1.get())
            A2 = ast.literal_eval(entry2.get())
            p = ast.literal_eval(entry3.get())

            X2 = 0.5*(1-A2/A1)**2
            Rshock = X2*p/(2*A1**2)
            result.config(text=f'El valor de X2 es {X2}\nEl valor de Rshock  es {Rshock}')

    # SI SE ELIGE CALCULAR UNIONES CAMBIO DE SECCION BRUSCO
    elif eleccion == '2':
        A1 = ast.literal_eval(entry1.get())
        A2 = ast.literal_eval(entry2.get())
        p = ast.literal_eval(entry3.get())

        X2 = 0.5*(1+2.5*A2/A1)**2
        Rshock = X2*p/(2*A1**2)
        result.config(text=f'El valor de X2 es {X2}\nEl valor de Rshock  es {Rshock}')

    # SI SE ELIGE CALCULAR EN UNIONES
    elif eleccion == '3':
        u1 = ast.literal_eval(entry1.get())
        u2 = ast.literal_eval(entry2.get())
        p = ast.literal_eval(entry3.get())

        X2 = 0.5*(1+2.5*u2/u1)
        Rshock = X2*p/(2*u1**2)
        result.config(text=f'El valor de X2 es {X2}\nEl valor de Rshock  es {Rshock}')
    else:
        messagebox.showerror("Error", "Invalid option selected")

root = tk.Tk()
root.title("Calculate Rshock")
root.geometry("400x400")

option = tk.StringVar()

label1 = tk.Label(root)



