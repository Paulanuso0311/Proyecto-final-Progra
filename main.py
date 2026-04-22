from modelos.videojuegos import videojuego
from modelos.juego_ps5 import JuegoPS5
from modelos.juego_xbox import JuegoXbox
from modelos.juego_nintendo import JuegoNintendo
from modelos.carrito import Carrito
from modelos.factura import Factura

from utilidades.lector_archivos import cargar_json, cargar_csv
from utilidades.escritor_archivos import (
    guardar_catalogo_json,
    guardar_catalogo_csv,
    guardar_factura_json,
    guardar_factura_csv
)

from servicios.busquedas import (
    buscar_por_id,
    buscar_por_nombre,
    buscar_por_categoria,
    buscar_por_consola
)


def mostrar_menu():
    print("\n" + "=" * 60)
    print("        TIENDA DE VIDEOJUEGOS - MENU PRINCIPAL")
    print("=" * 60)
    print("-------------- PRUEBAS TECNICAS --------------")
    print("1. Probar clase base")
    print("2. Probar clases hijas")
    print("3. Probar carga de JSON")
    print("4. Probar carga de CSV")
    print("-------------- FUNCIONALIDADES ---------------")
    print("5. Mostrar catálogo")
    print("6. Buscar videojuego por ID")
    print("7. Buscar videojuego por nombre")
    print("8. Buscar videojuego por categoría")
    print("9. Buscar videojuego por consola")
    print("10. Agregar videojuego al catálogo")
    print("11. Agregar videojuego al carrito")
    print("12. Ver carrito")
    print("13. Eliminar videojuego del carrito")
    print("14. Generar factura")
    print("15. Guardar catálogo")
    print("16. Salir")
    print("=" * 60)


def mostrar_resultados_formato_catalogo(lista_juegos, titulo="RESULTADOS"):
    print(f"\n{titulo}\n")

    if not lista_juegos:
        print("No se encontraron resultados.")
        return

    datos = []
    for juego in lista_juegos:
        datos.append({
            "ID": str(juego.id),
            "Nombre": juego.nombre,
            "Categoría": juego.categoria,
            "Precio": f"{juego.precio:.2f}",
            "ESRB": juego.esrb,
            "Stock": str(juego.stock),
            "Consola": juego.consola
        })

    columnas = ["ID", "Nombre", "Categoría", "Precio", "ESRB", "Stock", "Consola"]

    anchos = {}
    for col in columnas:
        ancho_max = len(col)
        for fila in datos:
            if len(fila[col]) > ancho_max:
                ancho_max = len(fila[col])
        anchos[col] = ancho_max

    encabezado = (
        f"{'ID':<{anchos['ID']}}  "
        f"{'Nombre':<{anchos['Nombre']}}  "
        f"{'Categoría':<{anchos['Categoría']}}  "
        f"{'Precio':>{anchos['Precio']}}  "
        f"{'ESRB':<{anchos['ESRB']}}  "
        f"{'Stock':>{anchos['Stock']}}  "
        f"{'Consola':<{anchos['Consola']}}"
    )
    print(encabezado)
    print("-" * len(encabezado))

    for fila in datos:
        print(
            f"{fila['ID']:<{anchos['ID']}}  "
            f"{fila['Nombre']:<{anchos['Nombre']}}  "
            f"{fila['Categoría']:<{anchos['Categoría']}}  "
            f"{fila['Precio']:>{anchos['Precio']}}  "
            f"{fila['ESRB']:<{anchos['ESRB']}}  "
            f"{fila['Stock']:>{anchos['Stock']}}  "
            f"{fila['Consola']:<{anchos['Consola']}}"
        )


def comparar_juegos(juego_a, juego_b):
    return (
        juego_a.id == juego_b.id and
        juego_a.nombre == juego_b.nombre and
        juego_a.categoria == juego_b.categoria and
        juego_a.precio == juego_b.precio and
        juego_a.esrb == juego_b.esrb and
        juego_a.stock == juego_b.stock and
        juego_a.consola == juego_b.consola
    )


def prueba_clase_base():
    print("\nPRUEBA CLASE BASE CONTRA CATÁLOGO")

    catalogo = cargar_json("datos/catalogo.json")
    if not catalogo:
        print("No se pudo cargar el catálogo.")
        return

    id_prueba = 1
    juego_real = buscar_por_id(catalogo, id_prueba)

    if not juego_real:
        print("No se encontró el juego en el catálogo.")
        return

    juego = videojuego(
        juego_real.id,
        juego_real.nombre,
        juego_real.categoria,
        juego_real.precio,
        juego_real.esrb,
        juego_real.stock,
        juego_real.consola
    )

    mostrar_resultados_formato_catalogo([juego_real], "REGISTRO ORIGINAL DEL CATÁLOGO")
    mostrar_resultados_formato_catalogo([juego], "OBJETO CREADO CON LA CLASE BASE")

    print("\nRESULTADO DE LA COMPARACIÓN:")
    print("COINCIDE CON EL CATÁLOGO" if comparar_juegos(juego, juego_real) else "NO COINCIDE CON EL CATÁLOGO")


def prueba_clases_hijas():
    print("\nPRUEBA CLASES HIJAS CONTRA CATÁLOGO")

    catalogo = cargar_json("datos/catalogo.json")
    if not catalogo:
        print("No se pudo cargar el catálogo.")
        return

    ids_prueba = [1, 6, 13]

    for id_prueba in ids_prueba:
        juego_real = buscar_por_id(catalogo, id_prueba)

        if not juego_real:
            print(f"No se encontró el juego con ID {id_prueba}.")
            continue

        if juego_real.consola == "PS5":
            juego = JuegoPS5(
                juego_real.id,
                juego_real.nombre,
                juego_real.categoria,
                juego_real.precio,
                juego_real.esrb,
                juego_real.stock
            )
        elif juego_real.consola == "XBOX":
            juego = JuegoXbox(
                juego_real.id,
                juego_real.nombre,
                juego_real.categoria,
                juego_real.precio,
                juego_real.esrb,
                juego_real.stock
            )
        elif juego_real.consola == "Nintendo":
            juego = JuegoNintendo(
                juego_real.id,
                juego_real.nombre,
                juego_real.categoria,
                juego_real.precio,
                juego_real.esrb,
                juego_real.stock
            )
        else:
            print(f"La consola del juego con ID {id_prueba} no es válida.")
            continue

        mostrar_resultados_formato_catalogo([juego_real], f"REGISTRO ORIGINAL ID {id_prueba}")
        mostrar_resultados_formato_catalogo([juego], f"OBJETO HIJO GENERADO ID {id_prueba}")

        print("RESULTADO:", "COINCIDE" if comparar_juegos(juego, juego_real) else "NO COINCIDE")
        print("-" * 80)


def prueba_carga_json():
    print("\nPRUEBA CARGA JSON")
    catalogo = cargar_json("datos/catalogo.json")
    mostrar_resultados_formato_catalogo(catalogo[:5], "PRIMEROS 5 REGISTROS JSON")


def prueba_carga_csv():
    print("\nPRUEBA CARGA CSV")
    catalogo = cargar_csv("datos/catalogo.csv")
    mostrar_resultados_formato_catalogo(catalogo[:5], "PRIMEROS 5 REGISTROS CSV")


def mostrar_catalogo(catalogo):
    mostrar_resultados_formato_catalogo(catalogo, "CATÁLOGO DE VIDEOJUEGOS")


def opcion_buscar_id(catalogo):
    try:
        id_juego = int(input("Ingrese el ID del videojuego: "))
        resultado = buscar_por_id(catalogo, id_juego)

        if resultado:
            mostrar_resultados_formato_catalogo([resultado], "RESULTADO DE BÚSQUEDA POR ID")
        else:
            print("No se encontró un videojuego con ese ID.")
    except ValueError:
        print("Debe ingresar un número válido.")


def opcion_buscar_nombre(catalogo):
    texto = input("Ingrese el nombre o parte del nombre: ")
    resultados = buscar_por_nombre(catalogo, texto)

    if resultados:
        mostrar_resultados_formato_catalogo(resultados, "RESULTADOS DE BÚSQUEDA POR NOMBRE")
    else:
        print("No se encontraron coincidencias.")


def opcion_buscar_categoria(catalogo):
    categoria = input("Ingrese la categoría: ")
    resultados = buscar_por_categoria(catalogo, categoria)

    if resultados:
        mostrar_resultados_formato_catalogo(resultados, "RESULTADOS DE BÚSQUEDA POR CATEGORÍA")
    else:
        print("No se encontraron juegos en esa categoría.")

def opcion_buscar_consola(catalogo):
    consola = input("Ingrese la consola (PS5, XBOX, Nintendo): ")
    resultados = buscar_por_consola(catalogo, consola)

    if resultados:
        mostrar_resultados_formato_catalogo(resultados, "RESULTADOS DE BÚSQUEDA POR CONSOLA")
    else:
        print("No se encontraron juegos para esa consola.")


def agregar_videojuego_catalogo(catalogo):
    print("\nAGREGAR VIDEOJUEGO")

    try:
        identificador = int(input("ID: "))

        if buscar_por_id(catalogo, identificador):
            print("Ya existe un videojuego con ese ID.")
            return

        nombre = input("Nombre: ").strip()
        categoria = input("Categoría: ").strip()
        precio = float(input("Precio: "))
        esrb = input("ESRB: ").strip()
        stock = int(input("Stock: "))

        consola = input("Consola (PS5, XBOX, Nintendo): ").strip().upper()

        if consola == "PS5":
            juego = JuegoPS5(identificador, nombre, categoria, precio, esrb, stock)
        elif consola == "XBOX":
            juego = JuegoXbox(identificador, nombre, categoria, precio, esrb, stock)
        elif consola == "NINTENDO":
            juego = JuegoNintendo(identificador, nombre, categoria, precio, esrb, stock)
        else:
            print("Consola inválida.")
            return

        catalogo.append(juego)
        print("Videojuego agregado correctamente.")
        mostrar_resultados_formato_catalogo([juego], "VIDEOJUEGO AGREGADO")

    except ValueError as e:
        print(f"Error al agregar videojuego: {e}")


def agregar_al_carrito(catalogo, carrito):
    print("\nAGREGAR AL CARRITO")

    try:
        id_juego = int(input("Ingrese el ID del videojuego: "))
        juego = buscar_por_id(catalogo, id_juego)

        if not juego:
            print("No existe un videojuego con ese ID.")
            return

        cantidad = int(input("Ingrese la cantidad: "))

        if cantidad > juego.stock:
            print("No hay suficiente stock disponible.")
            return

        carrito.agregar_juego(juego, cantidad)
        juego.stock -= cantidad
        print("Videojuego agregado al carrito.")

    except ValueError as e:
        print(f"Error: {e}")


def ver_carrito(carrito):
    carrito.mostrar_carrito()


def eliminar_del_carrito(catalogo, carrito):
    print("\nELIMINAR DEL CARRITO")

    try:
        id_juego = int(input("Ingrese el ID del videojuego a eliminar: "))

        for item in carrito.items:
            if item["juego"].id == id_juego:
                item["juego"].stock += item["cantidad"]
                break

        eliminado = carrito.eliminar_juego(id_juego)

        if eliminado:
            print("Videojuego eliminado del carrito.")
        else:
            print("Ese videojuego no está en el carrito.")

    except ValueError:
        print("Debe ingresar un número válido.")


def generar_factura(carrito):
    print("\nGENERAR FACTURA")

    if carrito.esta_vacio():
        print("No se puede generar factura porque el carrito está vacío.")
        return

    nombre_cliente = input("Ingrese el nombre del cliente: ").strip()
    nombre_archivo = input("Ingrese el nombre del archivo (sin extensión): ").strip()
    formato = input("Ingrese el formato (json/csv): ").strip().lower()

    factura = Factura(nombre_cliente, carrito)

    if formato == "json":
        guardar_factura_json(f"{nombre_archivo}.json", factura)
        print("Factura guardada en JSON.")
    elif formato == "csv":
        guardar_factura_csv(f"{nombre_archivo}.csv", factura)
        print("Factura guardada en CSV.")
    else:
        print("Formato no válido.")


def guardar_catalogo(catalogo):
    nombre_archivo = input("Ingrese el nombre del archivo (sin extensión): ").strip()
    formato = input("Ingrese el formato para guardar el catálogo (json/csv): ").strip().lower()

    if formato == "json":
        guardar_catalogo_json(f"{nombre_archivo}.json", catalogo)
        print("Catálogo guardado en JSON.")
    elif formato == "csv":
        guardar_catalogo_csv(f"{nombre_archivo}.csv", catalogo)
        print("Catálogo guardado en CSV.")
    else:
        print("Formato no válido.")


def main():
    catalogo = cargar_json("datos/catalogo.json")
    carrito = Carrito()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            prueba_clase_base()
        elif opcion == "2":
            prueba_clases_hijas()
        elif opcion == "3":
            prueba_carga_json()
        elif opcion == "4":
            prueba_carga_csv()
        elif opcion == "5":
            mostrar_catalogo(catalogo)
        elif opcion == "6":
            opcion_buscar_id(catalogo)
        elif opcion == "7":
            opcion_buscar_nombre(catalogo)
        elif opcion == "8":
            opcion_buscar_categoria(catalogo)
        elif opcion == "9":
            opcion_buscar_consola(catalogo)
        elif opcion == "10":
            agregar_videojuego_catalogo(catalogo)
        elif opcion == "11":
            agregar_al_carrito(catalogo, carrito)
        elif opcion == "12":
            ver_carrito(carrito)
        elif opcion == "13":
            eliminar_del_carrito(catalogo, carrito)
        elif opcion == "14":
            generar_factura(carrito)
        elif opcion == "15":
            guardar_catalogo(catalogo)
        elif opcion == "16":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()