from modelos.videojuegos import videojuego

class JuegoNintendo(videojuego):
    def __init__(self, identificador, nombre, categoria, precio, esrb, stock):
        super().__init__(identificador, nombre, categoria, precio, esrb, stock, "Nintendo")