
# TP2 organizacion empresarial - Escenario a
# ID Jira: TP2-5 (p2 - Paco)

import csv
import matplotlib.pyplot as plt #Libreriria para generar graficos
import os #Libreria 

os.makedirs("resultados", exist_ok=True)

#Listas de acumulacion de datos
fechas = []
temperaturas = []
precipitaciones = []

with open("datos/datos_climatico.csv", "r") as archivo:
  lector = csv.reader(archivo)
  next(lector)
  for fila in lector:
    fechas.append(fila[0]) #Agrega el primer dato de cada fila (fechas) al acumulador de fechas
    temperaturas.append(float(fila[1])) #Formatea y agrea el segundo dato al acumulador de temperaturas
    precipitaciones.append(float(fila[2])) #Formatea y agrea el tercer dato al acumulador de precipitaciones

#Funciones para calculos
# Promedio de valores con bucle for para agregar los valores a variable local y dividirla por la cantidad de datos
def promedio(lista):
  suma_de_valores = 0
  for valor in lista:
    suma_de_valores += valor
  return suma_de_valores / len(lista)

# Valor maximo, usa una variable para almacenar el dato y un ciclo for que agrega el mayor valor encontrado a esa variable
def valor_maximo(lista):
  maximo = lista[0]
  for valor in lista:
    if valor > maximo:
      maximo = valor
    return maximo

# Valor minimo, usa la misma mecanica que valor maximo pero de manera invertida
def valor_minimo(lista):
  minimo = lista[0]
  for valor in lista:
    if valor < minimo:
      minimo = valor
  return minimo

# Invocacion de funciones y mostrar datos en pantalla
print(f"El promedio de temperatura es {promedio(temperaturas):.1f}ºC\n")
print(f"La maxima temperatura registrada fue de {valor_maximo(temperaturas):.1f}ºC\n")
print(f"La minima tempertarua registrada fue de {valor_minimo(temperaturas):.1f}ºC\n")
print(f"El promedio de precipitaciones registrado fue de {promedio(precipitaciones):.1f}mm\n")

# Guardar resultados en archivo
with open("resultados/indicadores.txt", "w") as archivo:
  archivo.write(f"El promedio de temperatura es {promedio(temperaturas):.1f}ºC\n")
  archivo.write(f"La maxima temperatura registrada fue de {valor_maximo(temperaturas):.1f}ºC\n")
  archivo.write(f"La minima tempertarua registrada fue de {valor_minimo(temperaturas):.1f}ºC\n")
  archivo.write(f"El promedio de precipitaciones registrado fue de {promedio(precipitaciones):.1f}mm\n")

# Generar grafico, en este bloque recurri extensamente al uso de IA ya que desconozco la herramienta y libreria en cuestion
plt.figure(figsize=(10, 5))
plt.plot(fechas, temperaturas, marker="o", linewidth=2, label="Temperatura (ºC)")
plt.bar(fechas, precipitaciones, alpha=0.5, label="Precipitaciones (mm)")
plt.xlabel("Fecha")
plt.ylabel("Valores")
plt.title("Evolución de Temperatura y Precipitaciones")
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig("resultados/grafico_resultados.png")
plt.show()

print("\nGrafico guardado en 'resultados/grafico_resultados.png'")
