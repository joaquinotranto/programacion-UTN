"""
Módulo calculos.
Funciones para calcular promedios, ordenar, buscar el mayor promedio
y buscar un estudiante por legajo.
"""


def calcular_promedio(nota1, nota2):
    """
    Calcula el promedio de dos notas, redondeado a 2 decimales.

    Parámetros:
        nota1 (int), nota2 (int): notas entre 1 y 10.
    Retorna:
        float: promedio entre 1.00 y 10.00.
    """
    return round((nota1 + nota2) / 2, 2)


def calcular_promedios(notas1, notas2):
    """
    Calcula el promedio de cada estudiante y los guarda en una lista nueva.

    Parámetros:
        notas1, notas2 (list): notas del primer y segundo parcial.
    Retorna:
        list: lista de promedios, paralela a las demás.
    """
    promedios = []
    for i in range(len(notas1)):
        promedios.append(calcular_promedio(notas1[i], notas2[i]))
    return promedios


def intercambiar(lista, i, j):
    """
    Intercambia los elementos de las posiciones i y j de una lista.

    Parámetros:
        lista (list): lista a modificar.
        i, j (int): posiciones a intercambiar.
    """
    auxiliar = lista[i]
    lista[i] = lista[j]
    lista[j] = auxiliar


def ordenar_por_promedio(legajos, nombres, generos, notas1, notas2, promedios, orden):
    """
    Ordena los estudiantes por promedio usando el método burbuja.
    Trabaja sobre copias, así las listas originales no cambian de orden.
    Cada vez que se intercambian dos promedios, se intercambian también los
    datos de todas las listas, para que sigan siendo paralelas.

    Parámetros:
        legajos, nombres, generos, notas1, notas2, promedios (list): listas paralelas.
        orden (str): "ASC" para menor a mayor, "DESC" para mayor a menor.
    Retorna:
        tuple: las seis listas ordenadas.
    """
    leg = legajos[:]
    nom = nombres[:]
    gen = generos[:]
    n1 = notas1[:]
    n2 = notas2[:]
    prom = promedios[:]

    cantidad = len(prom)
    for i in range(cantidad - 1):
        for j in range(cantidad - 1 - i):
            if orden == "ASC":
                hay_que_cambiar = prom[j] > prom[j + 1]
            else:
                hay_que_cambiar = prom[j] < prom[j + 1]

            if hay_que_cambiar:
                intercambiar(leg, j, j + 1)
                intercambiar(nom, j, j + 1)
                intercambiar(gen, j, j + 1)
                intercambiar(n1, j, j + 1)
                intercambiar(n2, j, j + 1)
                intercambiar(prom, j, j + 1)

    return leg, nom, gen, n1, n2, prom


def obtener_mayor_promedio(promedios):
    """
    Busca el valor del mayor promedio recorriendo la lista.

    Parámetros:
        promedios (list): lista de promedios.
    Retorna:
        float: el mayor promedio.
    """
    mayor = promedios[0]
    for promedio in promedios:
        if promedio > mayor:
            mayor = promedio
    return mayor


def buscar_por_legajo(legajos, legajo_buscado):
    """
    Busca la posición de un legajo en la lista.

    Parámetros:
        legajos (list): lista de legajos.
        legajo_buscado (int): legajo a buscar.
    Retorna:
        int: la posición si lo encuentra, o -1 si no existe.
    """
    for i in range(len(legajos)):
        if legajos[i] == legajo_buscado:
            return i
    return -1
