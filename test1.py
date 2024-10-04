# Código a analizar
def suma_numeros(lista_numeros):
  suma = 0
  for numero in lista_numeros:
    suma =+ numero # Error lógico aquí: usa =+ en lugar de +=   
  return suma
# Lista de números de ejemplo
numeros = [1, 2, 3, 4, 5]
# Llamando a la función y mostrando el resultado
resultado = suma_numeros(numeros)
print(f"La suma de los números es: {resultado}")
