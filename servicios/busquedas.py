def buscar_por_id(catalogo, id_juego):
    for juego in catalogo:
        if juego.id == id_juego:
            return juego
    return None


def buscar_por_nombre(catalogo, texto):
    resultados = []

    for juego in catalogo:
        if texto.lower() in juego.nombre.lower():
            resultados.append(juego)

    return resultados


def buscar_por_categoria(catalogo, categoria):
    resultados = []

    for juego in catalogo:
        if juego.categoria.lower() == categoria.lower():
            resultados.append(juego)

    return resultados


def buscar_por_consola(catalogo, consola):
    resultados = []

    for juego in catalogo:
        if juego.consola.lower() == consola.lower():
            resultados.append(juego)

    return resultados