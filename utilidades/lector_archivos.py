import json
import csv
from modelos.juego_ps5 import JuegoPS5
from modelos.juego_xbox import JuegoXbox
from modelos.juego_nintendo import JuegoNintendo


def leer_csv(ruta):
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            return list(lector)
    except FileNotFoundError:
        print(f"Error: El archivo '{ruta}' no se encontró.")
        return None


def leer_json(ruta):
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print(f"Error: El archivo '{ruta}' no se encontró.")
        return None
    except json.JSONDecodeError:
        print(f"Error: El archivo '{ruta}' no contiene un JSON válido.")
        return None


def cargar_json(ruta):
    datos = leer_json(ruta)

    if datos is None:
        return []

    catalogo = []

    for item in datos:
        try:
            id_juego = int(item["id"])
            nombre = item["nombre"]
            categoria = item["categoria"]
            precio = float(item["precio"])
            esrb = item["esrb"]
            stock = int(item["stock"])
            consola = item["consola"]

            if consola == "PS5":
                juego = JuegoPS5(id_juego, nombre, categoria, precio, esrb, stock)
            elif consola == "XBOX":
                juego = JuegoXbox(id_juego, nombre, categoria, precio, esrb, stock)
            elif consola == "Nintendo":
                juego = JuegoNintendo(id_juego, nombre, categoria, precio, esrb, stock)
            else:
                continue

            catalogo.append(juego)
        except (ValueError, KeyError):
            print(f"Registro inválido en JSON: {item}")

    return catalogo


def cargar_csv(ruta):
    datos = leer_csv(ruta)

    if datos is None:
        return []

    catalogo = []

    for item in datos:
        try:
            id_juego = int(item["id"])
            nombre = item["nombre"]
            categoria = item["categoria"]
            precio = float(item["precio"])
            esrb = item["esrb"]
            stock = int(item["stock"])
            consola = item["consola"]

            if consola == "PS5":
                juego = JuegoPS5(id_juego, nombre, categoria, precio, esrb, stock)
            elif consola == "XBOX":
                juego = JuegoXbox(id_juego, nombre, categoria, precio, esrb, stock)
            elif consola == "Nintendo":
                juego = JuegoNintendo(id_juego, nombre, categoria, precio, esrb, stock)
            else:
                continue

            catalogo.append(juego)
        except (ValueError, KeyError):
            print(f"Registro inválido en CSV: {item}")

    return catalogo