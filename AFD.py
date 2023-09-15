import condiciones
import clases
import math
import os

Estado = 0
Estadoop1 = 0
Estadoop2 = 0
cont = 0
contador = 1
operaciones = []
grafo = []

classAFD = None
classAFDop1 = None
classAFDop2 = None

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
            Estado = 21 ## para un futuro >D 
            ## classAFD.val2 = (int)token.lexema
    elif Estado == 17:
        if token.lexema=="}":
            Estado = 18
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
        Estado = 0 
        return
    ## INGRESAR A LOS 2 ANALIZADORES HIJOS
    elif Estado == 13:
        classAFD.val1 = AnalizarOp1(token)
    elif Estado == 21:
        classAFD.val2 = AnalizarOp2(token)

## ANALIZADOR HIJO DEL VALOR 1
def AnalizarOp1(token):
    global Estadoop1, classAFDop1, Estado
    if token.lexema == '{':
        Estadoop1 = 1
    elif Estadoop1 == 1:
        if token.lexema == 'operacion':
            Estadoop1 = 2
            classAFDop1 = clases.AFD("", 0, 0, 0)
    elif Estadoop1 == 2:
        if token.lexema == ':':
            Estadoop1 = 3
    elif Estadoop1 == 3:
        if token.lexema == 'suma':
            classAFDop1.operacion = token.lexema
            Estadoop1 = 4
        elif token.lexema == 'resta':
            classAFDop1.operacion = token.lexema
            Estadoop1 = 4
        elif token.lexema == 'multiplicacion':
            classAFDop1.operacion = token.lexema
            Estadoop1 = 4
        elif token.lexema == 'division':
            classAFDop1.operacion = token.lexema
            Estadoop1 = 4
        elif token.lexema == 'potencia':
            classAFDop1.operacion = token.lexema
            Estadoop1 = 4
        elif token.lexema == 'raiz':
            classAFDop1.operacion = token.lexema
            Estadoop1 = 4
        elif token.lexema == 'inverso':
            classAFDop1.operacion = token.lexema
            Estadoop1 = 4
        elif token.lexema == 'seno':
            classAFDop1.operacion = token.lexema
            Estadoop1 = 4
        elif token.lexema == 'coseno':
            classAFDop1.operacion = token.lexema
            Estadoop1 = 4
        elif token.lexema == 'tangente':
            classAFDop1.operacion = token.lexema
            Estadoop1 = 4
        elif token.lexema == 'Mod':
            classAFDop1.operacion = token.lexema
            Estadoop1 = 4
    elif Estadoop1 == 4:
        if token.lexema == ',':
            Estadoop1 = 5
    elif Estadoop1 == 5:
        if token.lexema == 'valor1':
            Estadoop1 = 6
    elif Estadoop1 == 6:
        if token.lexema == ':':
            Estadoop1 = 7
    elif Estadoop1 == 7:
        if token.token == 'Tk_numero':
            classAFDop1.val1 = token.lexema
            Estadoop1 = 8
    elif Estadoop1 == 8:
        if token.lexema == ',':
            Estadoop1 = 9
    elif Estadoop1 == 9:
        if token.lexema == 'valor2':
            Estadoop1 = 10
    elif Estadoop1 == 10:
        if token.lexema == ':':
            Estadoop1 = 11
    elif Estadoop1 == 11:
        if token.token == 'Tk_numero':
            classAFDop1.val2 = token.lexema
            Estadoop1 = 12
    elif Estadoop1 == 12:
        if token.lexema == '}':
            Estadoop1 = 13
    elif Estadoop1 == 13:
        if token.lexema == ']':
            Estadoop1 = 0
            Estado = 12
            return classAFDop1

## ANALIZADOR HIJO DEL VALOR 2
def AnalizarOp2(token):
    global Estadoop2, classAFDop2, Estado
    if token.lexema == '{':
        Estadoop2 = 1
    elif Estadoop2 == 1:
        if token.lexema == 'operacion':
            Estadoop2 = 2
            classAFDop2 = clases.AFD("", 0, 0, 0)
    elif Estadoop2 == 2:
        if token.lexema == ':':
            Estadoop2 = 3
    elif Estadoop2 == 3:
        if token.lexema == 'suma':
            classAFDop2.operacion = token.lexema
            Estadoop2 = 4
        elif token.lexema == 'resta':
            classAFDop2.operacion = token.lexema
            Estadoop2 = 4
        elif token.lexema == 'multiplicacion':
            classAFDop2.operacion = token.lexema
            Estadoop2 = 4
        elif token.lexema == 'division':
            classAFDop2.operacion = token.lexema
            Estadoop2 = 4
        elif token.lexema == 'potencia':
            classAFDop2.operacion = token.lexema
            Estadoop2 = 4
        elif token.lexema == 'raiz':
            classAFDop2.operacion = token.lexema
            Estadoop2 = 4
        elif token.lexema == 'inverso':
            classAFDop2.operacion = token.lexema
            Estadoop2 = 4
        elif token.lexema == 'seno':
            classAFDop2.operacion = token.lexema
            Estadoop2 = 4
        elif token.lexema == 'coseno':
            classAFDop2.operacion = token.lexema
            Estadoop2 = 4
        elif token.lexema == 'tangente':
            classAFDop2.operacion = token.lexema
            Estadoop2 = 4
        elif token.lexema == 'Mod':
            classAFDop2.operacion = token.lexema
            Estadoop2 = 4
    elif Estadoop2 == 4:
        if token.lexema == ',':
            Estadoop2 = 5
    elif Estadoop2 == 5:
        if token.lexema == 'valor1':
            Estadoop2 = 6
    elif Estadoop2 == 6:
        if token.lexema == ':':
            Estadoop2 = 7
    elif Estadoop2 == 7:
        if token.token == 'Tk_numero':
            classAFDop2.val1 = token.lexema
            Estadoop2 = 8
    elif Estadoop2 == 8:
        if token.lexema == ',':
            Estadoop2 = 9
    elif Estadoop2 == 9:
        if token.lexema == 'valor2':
            Estadoop2 = 10
    elif Estadoop2 == 10:
        if token.lexema == ':':
            Estadoop2 = 11
    elif Estadoop2 == 11:
        if token.token == 'Tk_numero':
            classAFDop2.val2 = token.lexema
            Estadoop2 = 12
    elif Estadoop2 == 12:
        if token.lexema == '}':
            Estadoop2 = 13
    elif Estadoop2 == 13:
        if token.lexema == ']':
            Estadoop2 = 0
            Estado = 17
            return classAFDop2

def graficarAFD():
    global operaciones, cont, contador, grafo
    for operacionG in operaciones:
        file = open("AFD.dot", "w")
        escritura = "digraph Salida {\n rankdir=TR;\n node [shape = circle, color=blue , style=filled, fillcolor=white];\n"
        if (type(operacionG.val1) == str) and (type(operacionG.val2) == str):
            operacionG.resultado = operacion(operacionG.operacion, operacionG.val1, operacionG.val2)
            # cont = 0
            escritura += "node" + str(cont) + " [label = \"" + operacionG.operacion + "\n " + str(operacionG.resultado) + "\"];\n"
            cont += 1
            # cont = 1
            escritura += "node" + str(cont) + " [label = \"" + operacionG.val1 + "\"];\n"
            cont += 1
            # cont = 2
            escritura += "node" + str(cont) + " [label = \"" + operacionG.val2 + "\"];\n"
            escritura += "node" + str(cont-2) + " -> node" + str(cont-1) + ";\n"
            escritura += "node" + str(cont-2) + " -> node" + str(cont) + ";\n"
        elif (type(operacionG.val1) == str) and (type(operacionG.val2) != str):
            operacionG.resultado = operacion(operacionG.operacion, operacionG.val1, operacionDes(operacionG.val2).resultado) 
            # cont = 0
            escritura += "node" + str(cont) + " [label = \"" + operacionG.operacion + "\\n " + str(operacionG.resultado) + "\"];\n"
            cont += 1
            # cont = 1
            escritura += "node" + str(cont) + " [label = \"" + str(operacionG.val1) + "\"];\n"
            cont += 1
            # cont = 2
            escritura += "node" + str(cont) + " [label = \"" + operacionG.val2.operacion + "\\n " + str(operacionG.val2.resultado) + "\"];\n"
            cont += 1
            escritura += "node" + str(cont-3) + " -> node" + str(cont-2) + ";\n"
            escritura += "node" + str(cont-3) + " -> node" + str(cont-1) + ";\n"
            # cont = 3
            escritura += "node" + str(cont) + "[label = \"" + operacionG.val2.val1 + "\"];\n"
            cont += 1
            # cont = 4
            escritura += "node" + str(cont) + "[label = \"" + operacionG.val2.val2 + "\"];\n"
            escritura += "node" + str(cont-2) + " -> node" + str(cont-1) + ";\n"
            escritura += "node" + str(cont-2) + " -> node" + str(cont) + ";\n"
            #print(operacionG.operacion + " \n " + str(operacionG.resultado) + "\n")
            #print("/     \\")
            #print(operacionG.val1 + "     " + str(operacionG.val2.operacion) +
            # " \n \t" + str(operacionG.val2.resultado) + "\n")
            #print("\t/     \\")
            #print("\t"+ str(operacionG.val2.val1) + "     " + str(operacionG.val2.val2))
            #print("\n \n")
        elif (type(operacionG.val1) != str) and (type(operacionG.val2) == str):
            operacionG.resultado = operacion(operacionG.operacion, operacionDes(operacionG.val1).resultado, operacionG.val2) 
            escritura += "node" + str(cont) + " [label = \"" + operacionG.operacion + "\\n " + str(operacionG.resultado) + "\"];\n"
            cont += 1
            # cont = 1
            escritura += "node" + str(cont) + " [label = \"" + operacionG.val1.operacion + "\\n " + str(operacionG.val1.resultado) + "\"];\n"
            cont += 1
            escritura += "node" + str(cont) + " [label = \"" + str(operacionG.val2) + "\"];\n"
            cont += 1
            escritura += "node" + str(cont-3) + " -> node" + str(cont-2) + ";\n"
            escritura += "node" + str(cont-3) + " -> node" + str(cont-1) + ";\n"
            # cont = 2
            escritura += "node" + str(cont) + "[label = \"" + operacionG.val1.val1 + "\"];\n"
            cont += 1
            # cont = 3
            escritura += "node" + str(cont) + "[label = \"" + operacionG.val1.val2 + "\"];\n"
            escritura += "node" + str(cont-2) + " -> node" + str(cont-1) + ";\n"
            escritura += "node" + str(cont-2) + " -> node" + str(cont) + ";\n"
            #print(operacionG.operacion + " \n " + str(operacionG.resultado) + "\n")
            #print("/     \\")
            #print(operacionG.val1.operacion +
            #" \n" + str(operacionG.val1.resultado)
            #+ "     " + str(operacionG.val2) + "\n")
            #print("/     \\")
            #print(str(operacionG.val1.val1) + "     " + str(operacionG.val1.val2))
            #print("\n \n")
        elif (type(operacionG.val1) != str) and (type(operacionG.val2) != str):
            operacionG.resultado = operacion(operacionG.operacion, operacionDes(operacionG.val1).resultado, operacionDes(operacionG.val2).resultado)
            escritura += "node" + str(cont) + " [label = \""+ str(cont) + " | "  + operacionG.operacion + "\\n " + str(operacionG.resultado) + "\"];\n"
            cont += 1
            # cont = 1
            escritura += "node" + str(cont) + " [label = \"" + str(cont) + " | "  + operacionG.val1.operacion + "\\n " + str(operacionG.val1.resultado) + "\"];\n"
            cont += 1
            # cont = 2
            escritura += "node" + str(cont) + " [label = \" " + str(cont) + " | " + operacionG.val2.operacion + "\\n " + str(operacionG.val2.resultado) + "\"];\n"
            escritura += "node" + str(cont-2) + " -> node" + str(cont-1) + ";\n"
            escritura += "node" + str(cont-2) + " -> node" + str(cont) + ";\n"
            # cont = 3
            cont += 1
            escritura += "node" + str(cont) + "[label = \""+ str(cont) + " | "  + str(operacionG.val1.val1) + "\"];\n"
            cont += 1
            # cont = 4
            escritura += "node" + str(cont) + "[label = \""+ str(cont) + " | "  + str(operacionG.val1.val2) + "\"];\n"
            print(cont)
            escritura += "node" + str(cont-3) + " -> node" + str(cont-1) + ";\n"
            escritura += "node" + str(cont-3) + " -> node" + str(cont) + ";\n"
            cont += 1
            # cont = 5
            escritura += "node" + str(cont) + "[label = \""+ str(cont) + " | "  + str(operacionG.val2.val1) + "\"];\n"
            cont += 1
            # cont = 6
            escritura += "node" + str(cont) + "[label = \""+ str(cont) + " | "  + str(operacionG.val2.val2) + "\"];\n"
            print(cont)
            escritura += "node" + str(cont-4) + " -> node" + str(cont-1) + ";\n"
            escritura += "node" + str(cont-4) + " -> node" + str(cont) + ";\n"
            #print("\t " + operacionG.operacion + " \n " + str(operacionG.resultado) + "\n")
            #print("\t/     \\")
            #print("\t" + operacionG.val1.operacion + "     " + operacionG.val2.operacion)
            #print("\t   "+ str(operacionG.val1.resultado) + "     " + str(operacionG.val2.resultado))
            #print("\t   /     \\ \t \t /     \\")
            #print("\t  " + str(operacionG.val1.val1) + "     " + str(operacionG.val1.val2) + "\t \t" + str(operacionG.val2.val1) + "     " + str(operacionG.val2.val2))
        escritura += "}"
        file.write(escritura)
        #file.close()
        escritura = ""
        imagen = "AFD"+str(contador)+".png"
        cont = 0
        grafo.append(imagen)
        os.system("dot -Tpng AFD.dot -o " + imagen)
        contador += 1

def operacionDes(operacionDerecha):
    operacionDerecha.resultado = operacion(operacionDerecha.operacion, operacionDerecha.val1, operacionDerecha.val2)
    return operacionDerecha

def operacion(simbolo, ValR1, ValR2):
    if simbolo=="suma":
        return float(ValR1) + float(ValR2)
    elif simbolo=="resta":
        return float(ValR1) - float( ValR2)
    elif simbolo=="multiplicacion":
        return float(ValR1) * float( ValR2)
    elif simbolo=="division":
        return float(ValR1) / float(ValR2)
    elif simbolo=="potencia":
        return float(ValR1) ** float(ValR2)
    elif simbolo=="raiz":
        return float(ValR1) ** (1/float(ValR2))
    elif simbolo=="inverso":
        return 1/float(ValR1)
    elif simbolo=="seno":
        return math.sin(float(2*math.pi*float(ValR1)/180))
    elif simbolo=="coseno":
        return math.cos(float(2*math.pi*float(ValR1)/180))
    elif simbolo=="tangente":
        return math.tan(float(2*math.pi*float(ValR1)/180))
    elif simbolo=="Mod":
        return float(ValR1) % float(ValR2)
    else:
        return 0
    