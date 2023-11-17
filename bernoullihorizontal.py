import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ancho = 1000
alto = 800
tamano = str(ancho) + "x" + str(alto)
ventana.geometry(tamano)
ventana.title("ECUACION DE BERNOULLI TBOS HORIZONTALES")

# Create Labels for the entry widgets
ttk.Label(ventana, text="PRESION DE ENTRADA").grid(row=2, column=3, pady=5)
pa_entry = ttk.Entry(ventana, width=40)
pa_entry.grid(row=3, column=3)

ttk.Label(ventana, text="DENSIDAD DEL FLUIDO").grid(row=4, column=3, pady=5)
rho_entry = ttk.Entry(ventana, width=40)
rho_entry.grid(row=5, column=3)

ttk.Label(ventana, text="VELOCIDAD DE ENTRADA").grid(row=6, column=3, pady=5)
va_entry = ttk.Entry(ventana, width=40)
va_entry.grid(row=7, column=3)

ttk.Label(ventana, text="PRESION DE SALIDA").grid(row=8, column=3, pady=5)
pb_entry = ttk.Entry(ventana, width=40)
pb_entry.grid(row=9, column=3)

ttk.Label(ventana, text="VELOCIDAD DE SALIDA").grid(row=10, column=3, pady=5)
vb_entry = ttk.Entry(ventana, width=40)
vb_entry.grid(row=11, column=3)

def click1():
    pa = float(pb_entry.get()) + (float(rho_entry.get())/2) * ((float(vb_entry.get()))**2 - (float(va_entry.get()))**2)
    boton5.config(text=f"Resultado: {pa}")

boton1 = ttk.Button(ventana, text="CALCULAR PRESION DE ENTRADA", command=click1)
boton1.grid(row=12, column=3, pady=10)

def click2():
    pb = float(pa_entry.get()) + (float(rho_entry.get())/2) * ((float(va_entry.get()))**2 - (float(vb_entry.get()))**2)
    boton5.config(text=f"Resultado: {pb}")

boton2 = ttk.Button(ventana, text="CALCULAR PRESION DE SALIDA", command=click2)
boton2.grid(row=13, column=3, pady=10)

def click3():
    va = (((2*float(pb_entry.get()) - 2*float(pa_entry.get())) / float(rho_entry.get())) + (float(vb_entry.get()))**2)**(1/2)
    boton5.config(text=f"Resultado: {va}")

boton3 = ttk.Button(ventana, text="CALCULAR VELOCIDAD DE ENTRADA", command=click3)
boton3.grid(row=14, column=3, pady=10)

def click4():
    vb = (((2*float(pa_entry.get()) - 2*float(pb_entry.get())) / float(rho_entry.get())) + (float(va_entry.get()))**2)**(1/2)
    boton5.config(text=f"Resultado: {vb}")

boton4 = ttk.Button(ventana, text="CALCULAR VELOCIDAD DE SALIDA", command=click4)
boton4.grid(row=15, column=3, pady=10)

boton5 = ttk.Label(ventana, text="RESPUESTA")
boton5.grid(row=15, column=5, pady=10)

ventana.mainloop()

