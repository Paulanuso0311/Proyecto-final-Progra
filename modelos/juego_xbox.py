from modelos.videojuegos import videojuego

class JuegoXbox(videojuego):
    def __init__(self, identificador, nombre, categoria, precio, esrb, stock):
        super().__init__(identificador, nombre, categoria, precio, esrb, stock, "XBOX")