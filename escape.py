#Desafio velocidad escape Jorge Allende

import math

r = float(input("Ingrese el radio en Kilómetros:"))
g = float(input("Ingrese la constante g:"))

velocidad_escape = math.sqrt(2*g*r*1000)

print(f"La Velocidad de Escape es {velocidad_escape:.1f}[m/s]")

