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