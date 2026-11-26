# Ejercicio 3: Distribucion del presupuesto de un viaje
# Calcula costos totales, por participante y diarios.

costo_transporte = float(input("Costo total del transporte: "))
costo_hospedaje = float(input("Costo total del hospedaje: "))
costo_alimentacion = float(input("Costo total de la alimentacion: "))
participantes = int(input("Cantidad de participantes: "))
dias = int(input("Cantidad de dias del viaje: "))

costo_total = costo_transporte + costo_hospedaje + costo_alimentacion
costo_por_persona = costo_total / participantes
costo_diario_grupo = costo_total / dias
costo_diario_persona = costo_diario_grupo / participantes

print("\n--- Presupuesto del viaje ---")
print("Costo total del viaje:", format(costo_total, ".2f"))
print("Costo del viaje por persona:", format(costo_por_persona, ".2f"))
print("Costo diario del grupo:", format(costo_diario_grupo, ".2f"))
print("Costo diario por persona:", format(costo_diario_persona, ".2f"))
