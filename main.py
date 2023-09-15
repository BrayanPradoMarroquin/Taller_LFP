
import analizador
import condiciones
import AFD

## llamar al archivo operaciones.json y mostrarlo en pantalla
with open("operaciones.json", "r") as texto:
    contenido = texto.read()

## convertir el archivo en un array e itera la lista
Array = list(contenido)
for i in Array:
    analizador.analizador(i)

for token in condiciones.tablaSimbolos:
    AFD.analizarAFD(token)

AFD.graficarAFD()