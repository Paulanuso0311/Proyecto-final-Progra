class Carrito:
    def __init__(self):
        self._items = []

    @property
    def items(self):
        return self._items

    def agregar_juego(self, juego, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")

        if juego.stock < cantidad:
            raise ValueError("No hay suficiente stock disponible.")

        for item in self._items:
            if item["juego"].id == juego.id:
                if juego.stock < item["cantidad"] + cantidad:
                    raise ValueError("No hay suficiente stock disponible.")
                item["cantidad"] += cantidad
                return

        self._items.append({
            "juego": juego,
            "cantidad": cantidad
        })

    def eliminar_juego(self, id_juego):
        for item in self._items:
            if item["juego"].id == id_juego:
                self._items.remove(item)
                return True
        return False

    def calcular_total(self):
        total = 0
        for item in self._items:
            total += item["juego"].precio * item["cantidad"]
        return total

    def esta_vacio(self):
        return len(self._items) == 0

    def mostrar_carrito(self):
        if self.esta_vacio():
            print("El carrito está vacío.")
            return

        print("\nCARRITO DE COMPRAS")
        print("-" * 100)
        for item in self._items:
            juego = item["juego"]
            cantidad = item["cantidad"]
            subtotal = juego.precio * cantidad
            print(
                f"ID: {juego.id} | Nombre: {juego.nombre} | "
                f"Cantidad: {cantidad} | Precio: ${juego.precio:.2f} | "
                f"Subtotal: ${subtotal:.2f}"
            )
        print("-" * 100)
        print(f"TOTAL: ${self.calcular_total():.2f}")