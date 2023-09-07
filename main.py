
import analizador

## llamar al archivo operaciones.json y mostrarlo en pantalla
with open("operaciones.json", "r") as texto:
    contenido = texto.read()

## convertir el archivo en un array e itera la lista
Array = list(contenido)
for i in Array:
    analizador.analizador(i)

print("Tabla de simbolos")