class videojuego:
    def __init__(self, identificador, nombre, categoria, precio, esrb, stock, consola):
        self._id = identificador
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self._esrb = esrb
        self.stock = stock
        self.consola = consola

    @property
    def id(self):
        return self._id

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or valor.strip() == "":
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = valor.strip()

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, valor):
        if not isinstance(valor, str) or valor.strip() == "":
            raise ValueError("La categoría no puede estar vacía.")
        self._categoria = valor.strip()

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        if valor < 0:
            raise ValueError("El precio no puede ser negativo.")
        self._precio = float(valor)

    @property
    def esrb(self):
        return self._esrb

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, valor):
        if valor < 0:
            raise ValueError("El stock no puede ser negativo.")
        self._stock = int(valor)

    @property
    def consola(self):
        return self._consola

    @consola.setter
    def consola(self, valor):
        if not isinstance(valor, str) or valor.strip() == "":
            raise ValueError("La consola no puede estar vacía.")
        self._consola = valor.strip()

    def mostrar_info(self):
        return (
            f"ID: {self.id} | "
            f"Nombre: {self.nombre} | "
            f"Categoría: {self.categoria} | "
            f"Precio: ${self.precio:.2f} | "
            f"ESRB: {self.esrb} | "
            f"Stock: {self.stock} | "
            f"Consola: {self.consola}"
        )
    
    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "esrb": self.esrb,
            "stock": self.stock,
            "consola": self.consola
        }
    def __str__(self):
        return self.mostrar_info()