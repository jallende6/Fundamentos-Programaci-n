import math
# Solicitud de Inputs
proteina = float(input("Ingrese los gr de proteina:\n>"))
carbohidratos = float(input("Ingrese el los de Carbohidrato:\n>"))
grasa = float(input("Ingrese el los de Grasa:\n>"))
# cálculo de calorías
calorias = 4 * (proteina + carbohidratos) + 9 * grasa
# entregar output en el formato solicitado
print(f'Las calorías totales del producto son: {math.ceil(calorias)}')