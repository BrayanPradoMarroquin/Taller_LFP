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
    if esnumero(c):
        valor+=c
        columna+=1
    elif ord(c)==46:
        valor+=c
        columna+=1
        cont+=1
    elif ord(c)==44:
        flagExpressionDecimal=False
        tablaSimbolos.append(token("Tk_numero", valor, fila, columna-1))
        tablaSimbolos.append(token("Tk_coma", ",", fila, columna))
        valor=""
        return
    elif c==' ':
        flagExpressionDecimal=False
        tablaSimbolos.append(token("Tk_numero", valor, fila, columna))
        valor=""
        return
    else:
        tablaErrores.append(Error(c, fila, columna, "Lexico: Caracter no valido"))
        return