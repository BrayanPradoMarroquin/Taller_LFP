#importaciones
from clases import *

# variales generales para el analizador
columna = 0
fila = 0
valor=""
cont=0

# Listas para utilizar en el analizador
tablaSimbolos = []
tablaErrores = []

## Banderas para el analizador
flagcadena=False # bandera para saber si se esta leyendo una cadena
flagExpressionDecimal=False # bandera para saber si se esta leyendo una expresion decimal

def expresioncadena(c):
    global valor, columna, fila, flagcadena
    if ord(c)==34:
        columna+=1
        tablaSimbolos.append(token("tk_cadena", valor, fila, columna))
        valor=""
        flagcadena=False
        return
    else:
        valor+=c
        fila+=1

def esnumero(c):
    return (ord(c)>=48) & (ord(c)<=57)        

def ExpresionDecimal(c, val):
    global valor, fila, columna, cont, flagExpressionDecimal
    conta=cont
    if esnumero(c) & (cont <= 2):
        val += c
        cont = cont + 1
        valor=val
        return
    elif (cont>0) & (cont<=2) & (ord(c)==32):
        columna+=1
        tablasimbolos.append(token("Numero", valor, fila, (columna - 1 - len(valor))))
        valor=""
        cont=0
        flagExpressionDecimal = False
    elif (cont>0) & (cont<=2) & (ord(c)==44):
        columna += 1
        tablasimbolos.append(token("Numero", valor, fila, (columna - 1 - len(valor))))
        columna+=1
        tablasimbolos.append(token("coma",",",fila,(columna-2)))
        valor = ""
        flagExpressionDecimal=False
        cont = 0
    else:
        val += c
        Error(valor, fila, columna,  "Se espera un numero con formato ##.##")
        flagExpressionDecimal=False
        cont = 0
        return