# Ejercicio 2: Costo de impresion de materiales
# Calcula costos, subtotal, impuesto y total por pagar.

cantidad_afiches = int(input("Cantidad de afiches: "))
precio_afiche = float(input("Precio de impresion de cada afiche: "))
cantidad_volantes = int(input("Cantidad de volantes: "))
precio_volante = float(input("Precio de impresion de cada volante: "))
porcentaje_impuesto = float(input("Porcentaje de impuesto: "))

costo_afiches = cantidad_afiches * precio_afiche
costo_volantes = cantidad_volantes * precio_volante
subtotal = costo_afiches + costo_volantes
monto_impuesto = subtotal * (porcentaje_impuesto / 100)
total_pagar = subtotal + monto_impuesto

print("\n--- Resumen de impresion ---")
print("Costo total de los afiches:", format(costo_afiches, ".2f"))
print("Costo total de los volantes:", format(costo_volantes, ".2f"))
print("Subtotal:", format(subtotal, ".2f"))
print("Monto del impuesto:", format(monto_impuesto, ".2f"))
print("Total por pagar:", format(total_pagar, ".2f"))
