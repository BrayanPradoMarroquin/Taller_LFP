class token:
    def __init__(self, token, lexema, fila, columna):
        self.token = token
        self.lexema = lexema
        self.fila = fila
        self.columna = columna

class Error:
    def __init__(self, lexema, fila, columna, descripcion):
        self.lexema = lexema
        self.fila = fila
        self.columna = columna
        self.descripcion = descripcion

class AFD:
    def __init__(self, operacion, val1, val2, resultado):
        self.operacion = operacion
        self.val1 = val1
        self.val2 = val2
        self.resultado = resultado
        self.grafica = ""