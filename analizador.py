import condiciones
from clases import *

def analizador(c):
    if condiciones.flagcadena==True:
        condiciones.expresioncadena(c)
    elif condiciones.flagExpressionDecimal==True:
        condiciones.ExpresionDecimal(c,condiciones.valor)
    elif ord(c)==123:
        condiciones.columna+=1
        condiciones.fila+=1
        condiciones.tablaSimbolos.append(token("Tk_llaveabre","{",condiciones.fila,condiciones.columna))
    elif ord(c)==34:
        condiciones.flagcadena=True
    elif condiciones.esnumero(c):
        condiciones.flagExpressionDecimal=True
        condiciones.valor+=c
    elif ord(c)==58:
        condiciones.columna+=1
        condiciones.fila+=1
        condiciones.tablaSimbolos.append(token("Tk_dospuntos",":",condiciones.fila,condiciones.columna))
    elif ord(c)==91: ## [
        condiciones.fila+=1
        condiciones.columna=0
        condiciones.tablaSimbolos.append(token("Tk_corcheteabre","[",condiciones.fila,condiciones.columna))
    elif ord(c)==44: ## ,
        condiciones.columna+=1
        condiciones.tablaSimbolos.append(token("Tk_coma",",",condiciones.fila,condiciones.columna))
    elif ord(c)==93: ## ]
        condiciones.columna+=1
        condiciones.tablaSimbolos.append(token("Tk_corchetecierra","]",condiciones.fila,condiciones.columna))
    elif ord(c)==125: ## }
        condiciones.columna+=0
        condiciones.tablaSimbolos.append(token("Tk_llavecierra","}",condiciones.fila,condiciones.columna))
    elif c=="\n":
        condiciones.fila+=1
    elif c==" ":
        condiciones.columna+=1
    else:
        condiciones.tablaErrores.append(Error(c,condiciones.fila,condiciones.columna,"Lexico: Caracter no valido"))
        return
        

