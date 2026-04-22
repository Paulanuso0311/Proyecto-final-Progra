from datetime import datetime

class Factura:
    def __init__(self, nombre_cliente, carrito):
        if not nombre_cliente.strip():
            raise ValueError("El nombre del cliente no puede estar vacío.")

        if carrito.esta_vacio():
            raise ValueError("No se puede crear una factura con el carrito vacío.")

        self.nombre_cliente = nombre_cliente.strip()
        self.fecha_compra = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.detalle = []
        self.total = carrito.calcular_total()

        for item in carrito.items:
            juego = item["juego"]
            cantidad = item["cantidad"]

            self.detalle.append({
                "id": juego.id,
                "nombre": juego.nombre,
                "cantidad": cantidad,
                "precio_individual": juego.precio,
                "subtotal": juego.precio * cantidad
            })

    def to_dict(self):
        return {
            "nombre_cliente": self.nombre_cliente,
            "fecha_compra": self.fecha_compra,
            "videojuegos": self.detalle,
            "total_pagar": self.total
        }

    def __str__(self):
        texto = []
        texto.append("FACTURA")
        texto.append(f"Cliente: {self.nombre_cliente}")
        texto.append(f"Fecha: {self.fecha_compra}")
        texto.append("-" * 50)

        for item in self.detalle:
            texto.append(
                f"{item['nombre']} | Cantidad: {item['cantidad']} | "
                f"Precio: ${item['precio_individual']:.2f} | "
                f"Subtotal: ${item['subtotal']:.2f}"
            )

        texto.append("-" * 50)
        texto.append(f"TOTAL A PAGAR: ${self.total:.2f}")

        return "\n".join(texto)