#Pregunta 2 Jorge Allende

p = float(input("Ingrese Precio de Suscripcion:\n>"))
u = float(input("Ingrese Numero de Usuarios Normales:\n>"))
u_premium = float(input("Ingrese Numero de Usuarios Premium:\n>"))
gt = float(input("Ingrese Gastos totales:\n>"))

utilidades = p*u + 1.5*p*u_premium - gt
print(f"Las utilidades totales son: {utilidades}")