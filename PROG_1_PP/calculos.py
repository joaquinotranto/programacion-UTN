"""
Módulo: calculos.py

Descripción:
    Contiene las funciones de cálculo del programa: calcular promedios,
    copiar listas, intercambiar elementos, ordenar por promedio (método
    burbuja), buscar el mayor promedio y buscar un estudiante por legajo.

Funciones:
    calcular_promedio(nota1, nota2)          -> float
    calcular_promedios(notas1, notas2)       -> list
    copiar_lista(lista)                      -> list
    intercambiar(lista, i, j)                -> None
    ordenar_por_promedio(..., orden)         -> tuple de 6 listas
    obtener_mayor_promedio(promedios)        -> float
    buscar_por_legajo(legajos, legajo)       -> int
"""


def calcular_promedio(nota1, nota2):
    """
    Calcula el promedio de dos notas.

    Lógica:
        Suma las dos notas, divide por 2 y redondea el resultado a 2
        decimales con round(). La división / siempre da un número real
        (float). Como las notas están entre 1 y 10, el promedio queda
        entre 1.00 y 10.00.

    Parámetros:
        nota1 (int): nota del parcial 1.
        nota2 (int): nota del parcial 2.

    Retorna:
        float: el promedio con 2 decimales.

    Ejemplo:
        calcular_promedio(7, 8) -> 7.5
    """
    return round((nota1 + nota2) / 2, 2)


def calcular_promedios(notas1, notas2):
    """
    Calcula el promedio de cada estudiante y los guarda en una lista
    nueva, paralela a las demás.

    Lógica:
        1. Crea la lista promedios con tantos ceros como estudiantes
           ([0] * len(notas1)).
        2. Con un for recorre cada posición i.
        3. En cada vuelta calcula el promedio del estudiante i con
           calcular_promedio y lo guarda en promedios[i].
        4. Devuelve la lista.

    Parámetros:
        notas1 (list): notas del parcial 1.
        notas2 (list): notas del parcial 2.

    Retorna:
        list: los promedios, en el mismo orden que los estudiantes.
    """
    promedios = [0] * len(notas1)
    for i in range(len(notas1)):
        promedios[i] = calcular_promedio(notas1[i], notas2[i])
    return promedios


def copiar_lista(lista):
    """
    Crea una copia de una lista, elemento por elemento.

    Lógica:
        1. Crea una lista nueva del mismo tamaño ([0] * len(lista)).
        2. Con un for copia cada elemento de la lista original en la
           misma posición de la lista nueva.
        Se usa para ordenar sin modificar las listas originales. Si se
        hiciera copia = lista, las dos variables serían la MISMA lista
        y al ordenar se desordenaría la original.

    Parámetros:
        lista (list): la lista a copiar.

    Retorna:
        list: una lista nueva con los mismos elementos.
    """
    copia = [0] * len(lista)
    for i in range(len(lista)):
        copia[i] = lista[i]
    return copia


def intercambiar(lista, i, j):
    """
    Intercambia los elementos de las posiciones i y j de una lista.

    Lógica:
        Usa una variable auxiliar, como cuando se pasa el contenido de
        dos vasos usando un tercer vaso vacío:
        1. Guarda lista[i] en auxiliar.
        2. Pone lista[j] en la posición i.
        3. Pone auxiliar (el valor viejo de i) en la posición j.
        Modifica la lista que recibe, por eso no necesita return.

    Parámetros:
        lista (list): la lista a modificar.
        i (int): primera posición.
        j (int): segunda posición.

    Retorna:
        No retorna nada (modifica la lista recibida).
    """
    auxiliar = lista[i]
    lista[i] = lista[j]
    lista[j] = auxiliar


def ordenar_por_promedio(legajos, nombres, generos, notas1, notas2, promedios, orden):
    """
    Ordena los estudiantes por promedio usando el método burbuja.

    Método burbuja:
        Compara cada elemento con el siguiente y, si están en el orden
        incorrecto, los intercambia. Se hacen varias pasadas; en cada
        pasada el valor más grande (o más chico) queda en su lugar al
        final, como una burbuja que sube.

    Lógica:
        1. Copia las 6 listas con copiar_lista, para no desordenar las
           originales.
        2. El for de afuera (i) hace las pasadas: cantidad - 1 pasadas.
        3. El for de adentro (j) compara de a pares: posición j con j+1.
           Se resta i porque los últimos i elementos ya están ordenados.
        4. Si orden es "ASC" (menor a mayor), hay que cambiar cuando el
           de la izquierda es mayor. Si es "DESC" (mayor a menor),
           cuando el de la izquierda es menor.
        5. Si hay que cambiar, intercambia las posiciones j y j+1 en
           LAS 6 LISTAS, para que sigan siendo paralelas (si solo se
           cambiara el promedio, quedaría al lado del nombre de otro).
        6. Devuelve las 6 listas ordenadas.

    Parámetros:
        legajos, nombres, generos, notas1, notas2, promedios (list):
            listas paralelas.
        orden (str): "ASC" para menor a mayor, "DESC" para mayor a menor.

    Retorna:
        tuple: las 6 listas ordenadas (leg, nom, gen, n1, n2, prom).
    """
    leg = copiar_lista(legajos)
    nom = copiar_lista(nombres)
    gen = copiar_lista(generos)
    n1 = copiar_lista(notas1)
    n2 = copiar_lista(notas2)
    prom = copiar_lista(promedios)

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
    Busca el valor del mayor promedio.

    Lógica:
        1. Supone que el mayor es el primero (promedios[0]).
        2. Con un for recorre todos los promedios.
        3. Si encuentra uno más grande que el mayor actual, lo guarda
           como nuevo mayor.
        4. Al terminar, devuelve el mayor.

    Parámetros:
        promedios (list): lista de promedios.

    Retorna:
        float: el mayor promedio.
    """
    mayor = promedios[0]
    for i in range(len(promedios)):
        if promedios[i] > mayor:
            mayor = promedios[i]
    return mayor


def buscar_por_legajo(legajos, legajo_buscado):
    """
    Busca en qué posición está un legajo (búsqueda secuencial).

    Lógica:
        1. Con un for recorre la lista de legajos posición por posición.
        2. Si el legajo de la posición i es igual al buscado, devuelve
           i y la función termina.
        3. Si termina de recorrer y no lo encontró, devuelve -1.
        Se devuelve la posición porque con ella se obtienen todos los
        datos del estudiante en las listas paralelas. Se usa -1 porque
        ninguna posición real es negativa.

    Parámetros:
        legajos (list): lista de legajos.
        legajo_buscado (int): el legajo a buscar.

    Retorna:
        int: la posición del legajo, o -1 si no existe.
    """
    for i in range(len(legajos)):
        if legajos[i] == legajo_buscado:
            return i
    return -1
