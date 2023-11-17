import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ancho = 1000
alto = 800
tamano = str(ancho) + "x" + str(alto)
ventana.geometry(tamano)
ventana.title("ECUACION DE CONTINUIDAD")


ttk.Label(ventana, text="VELOCIDAD DE ENTRADA").grid(row=2, column=3, pady=5)
va_entry = ttk.Entry(ventana, width=40)
va_entry.grid(row=3, column=3)

ttk.Label(ventana, text="SECCION DE ENTRADA").grid(row=4, column=3, pady=5)
sa_entry = ttk.Entry(ventana, width=40)
sa_entry.grid(row=5, column=3)

ttk.Label(ventana, text="VELOCIDAD DE SALIDA").grid(row=6, column=3, pady=5)
vb_entry = ttk.Entry(ventana, width=40)
vb_entry.grid(row=7, column=3)

ttk.Label(ventana, text="SECCION DE SALIDA").grid(row=8, column=3, pady=5)
sb_entry = ttk.Entry(ventana, width=40)
sb_entry.grid(row=9, column=3)

def click1():
    va = float(vb_entry.get()) * float(sb_entry.get()) / float(sa_entry.get())
    boton5.config(text=f"Resultado: {va}")

boton1 = ttk.Button(ventana, text="CALCULAR VELOCIDAD DE ENTRADA", command=click1)
boton1.grid(row=10, column=3, pady=10)

def click2():
    vb = float(va_entry.get()) * float(sa_entry.get()) / float(sb_entry.get())
    boton5.config(text=f"Resultado: {vb}")

boton2 = ttk.Button(ventana, text="CALCULAR VELOCIDAD DE SALIDA", command=click2)
boton2.grid(row=11, column=3, pady=10)

def click3():
    sa = float(vb_entry.get()) * float(sb_entry.get()) / float(va_entry.get())
    boton5.config(text=f"Resultado: {sa}")

boton3 = ttk.Button(ventana, text="CALCULAR SECCION DE ENTRADA", command=click3)
boton3.grid(row=12, column=3, pady=10)

def click4():
    sb = float(va_entry.get()) * float(sa_entry.get()) / float(vb_entry.get())
    boton5.config(text=f"Resultado: {sb}")

boton4 = ttk.Button(ventana, text="CALCULAR SECCION DE SALIDA", command=click4)
boton4.grid(row=13, column=3, pady=10)

boton5 = ttk.Button(ventana, text="RESPUESTA")
boton5.grid(row=15, column=3, pady=10)

ventana.mainloop()

