import condiciones
import clases
import math

Estado = 0
operaciones = []

classAFD = None


# Función que analiza el contenido del archivo operaciones.json
def analizarAFD(token):
    global Estado, classAFD
    if Estado == 0:
        if token.lexema=="{":
            Estado = 1
    elif Estado == 1:
        if token.lexema=="operaciones":
            Estado = 2
            return
    elif Estado == 2:
        if token.lexema==":":
            Estado = 3
            return
    elif Estado == 3:
        if token.lexema=="[":
            Estado = 4
            return
    elif Estado == 4:
        if token.lexema=="{":
            Estado = 5
            return
    elif Estado == 5:
        if token.lexema=="operacion":
            Estado = 6
            classAFD = clases.AFD("", 0, 0, 0)
            return
    elif Estado == 6:
        if token.lexema==":":
            Estado = 7
            return
    elif Estado == 7:
        if token.lexema=="suma":
            classAFD.operacion = token.lexema
            Estado = 8
        elif token.lexema=="resta":
            classAFD.operacion = token.lexema
            Estado = 8
        elif token.lexema=="multiplicacion":
            classAFD.operacion = token.lexema
            Estado = 8
        elif token.lexema=="division":
            classAFD.operacion = token.lexema
            Estado = 8
        elif token.lexema=="potencia":
            classAFD.operacion = token.lexema
            Estado = 8
        elif token.lexema=="raiz":
            classAFD.operacion = token.lexema
            Estado = 8
        elif token.lexema=="inverso":
            classAFD.operacion = token.lexema
            Estado = 8
        elif token.lexema=="seno":
            classAFD.operacion = token.lexema
            Estado = 8
        elif token.lexema=="coseno":
            classAFD.operacion = token.lexema
            Estado = 8
        elif token.lexema=="tangente":
            classAFD.operacion = token.lexema
            Estado = 8
        elif token.lexema=="Mod":
            classAFD.operacion = token.lexema
            Estado = 8
    elif Estado == 8:
        if token.lexema==",":
            Estado = 9
    elif Estado == 9:
        if token.lexema=="valor1":
            Estado = 10
    elif Estado == 10:
        if token.lexema==":":
            Estado = 11
    elif Estado == 11:
        if token.token=="Tk_numero":
            classAFD.val1 = token.lexema
            Estado = 12
        elif token.lexema=="[":
            Estado = 13 ## para un futuro >D 
            ## classAFD.val2 = (int)token.lexema
    elif Estado == 12:
        if token.lexema==",":
            Estado = 14
        elif token.lexema=="}":
            Estado = 18
            classAFD.resultado = operacion()
            operaciones.append(classAFD)
            classAFD = None
    elif Estado == 14:
        if token.lexema=="valor2":
            Estado = 15
    elif Estado == 15:
        if token.lexema==":":
            Estado = 16
    elif Estado == 16:
        if token.token=="Tk_numero":
            classAFD.val2 = token.lexema
            Estado = 17
        elif token.lexema=="[":
            Estado = 13 ## para un futuro >D 
            ## classAFD.val2 = (int)token.lexema
    elif Estado == 17:
        if token.lexema=="}":
            Estado = 18
            classAFD.resultado = operacion()
            operaciones.append(classAFD)
            classAFD = None
    elif Estado == 18:
        if token.lexema==",":
            Estado = 4
        if token.lexema=="]":
            Estado = 19
    elif Estado == 19:
        if token.lexema=="}":
            Estado = 20
    elif Estado == 20:
        return


def operacion():
    if classAFD.operacion=="suma":
        return float(classAFD.val1) + float(classAFD.val2)
    elif classAFD.operacion=="resta":
        return float(classAFD.val1) - float( classAFD.val2)
    elif classAFD.operacion=="multiplicacion":
        return classAFD.val1 * classAFD.val2
    elif classAFD.operacion=="division":
        return classAFD.val1 / classAFD.val2
    elif classAFD.operacion=="potencia":
        return classAFD.val1 ** classAFD.val2
    elif classAFD.operacion=="raiz":
        return classAFD.val1 ** (1/classAFD.val2)
    elif classAFD.operacion=="inverso":
        return 1/float(classAFD.val1)
    elif classAFD.operacion=="seno":
        return math.sin(float(2*math.pi*float(classAFD.val1)/180))
    elif classAFD.operacion=="coseno":
        return math.cos(float(2*math.pi*float(classAFD.val1)/180))
    elif classAFD.operacion=="tangente":
        return math.tan(float(2*math.pi*float(classAFD.val1)/180))
    elif classAFD.operacion=="Mod":
        return float(classAFD.val1) % float(classAFD.val2)
    else:
        return 0