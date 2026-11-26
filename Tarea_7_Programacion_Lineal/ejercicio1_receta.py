# Ejercicio 1: Preparacion de una receta
# Ajusta las cantidades de ingredientes para la cantidad de personas indicada.

personas = int(input("Cantidad de personas: "))
arroz_base = float(input("Gramos de arroz para 4 personas: "))
carne_base = float(input("Gramos de carne para 4 personas: "))
salsa_base = float(input("Mililitros de salsa para 4 personas: "))

factor_ajuste = personas / 4

arroz_necesario = arroz_base * factor_ajuste
carne_necesaria = carne_base * factor_ajuste
salsa_necesaria = salsa_base * factor_ajuste

print("\n--- Ingredientes necesarios ---")
print("Arroz:", format(arroz_necesario, ".2f"), "gramos")
print("Carne:", format(carne_necesaria, ".2f"), "gramos")
print("Salsa:", format(salsa_necesaria, ".2f"), "mililitros")
