#Pregunta 3 Jorge Allende

p = float(input("Ingrese Precio de Suscripcion:\n>"))
u = float(input("Ingrese Numero de Usuarios:\n>"))
gt = float(input("Ingrese Gastos totales:\n>"))
u_año_pasado = float(input("Ingrese las Utilidades del Año Anterior:\n >"))
utilidades = p*u - gt

print(f"La razón entre las utilidades actuales y las del año pasado es: {utilidades/u_año_pasado:.2f}")