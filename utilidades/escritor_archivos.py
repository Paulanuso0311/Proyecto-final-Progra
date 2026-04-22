import json
import csv


def guardar_catalogo_json(ruta, catalogo):
    datos = [juego.to_dict() for juego in catalogo]
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)


def guardar_catalogo_csv(ruta, catalogo):
    datos = [juego.to_dict() for juego in catalogo]

    with open(ruta, "w", newline="", encoding="utf-8") as archivo:
        campos = ["id", "nombre", "categoria", "precio", "esrb", "stock", "consola"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(datos)


def guardar_factura_json(ruta, factura):
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(factura.to_dict(), archivo, indent=4, ensure_ascii=False)


def guardar_factura_csv(ruta, factura):
    datos = factura.to_dict()

    with open(ruta, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)

        escritor.writerow(["Nombre del cliente", datos["nombre_cliente"]])
        escritor.writerow(["Fecha de compra", datos["fecha_compra"]])
        escritor.writerow([])

        escritor.writerow(["ID", "Nombre", "Cantidad", "Precio individual", "Subtotal"])

        for item in datos["videojuegos"]:
            escritor.writerow([
                item["id"],
                item["nombre"],
                item["cantidad"],
                item["precio_individual"],
                item["subtotal"]
            ])

        escritor.writerow([])
        escritor.writerow(["TOTAL", datos["total_pagar"]])