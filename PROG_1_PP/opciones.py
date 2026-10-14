"""
Módulo: opciones.py

Descripción:
    Contiene una función por cada opción del menú (Nota 3 de la
    consigna). Cada función usa las funciones de los otros módulos
    (carga, calculos, mostrar, validaciones).

Funciones:
    opcion_cargar_datos()               -> opción 1
    opcion_mostrar_datos(...)           -> opción 2
    opcion_calcular_promedios(...)      -> opción 3
    opcion_mostrar_ordenados(...)       -> opción 4
    opcion_mostrar_mayor_promedio(...)  -> opción 5
    opcion_buscar_por_legajo(...)       -> opción 6
    opcion_salir()                      -> opción 7
"""

from carga import cargar_estudiantes
from datos_prueba import obtener_datos_prueba
from mostrar import mostrar_estudiantes
from calculos import (calcular_promedios, ordenar_por_promedio,
                      obtener_mayor_promedio, buscar_por_legajo)
from validaciones import validar_legajo


def opcion_cargar_datos():
    """
    Opción 1: carga los datos de los 30 estudiantes.

    Lógica:
        1. Pregunta si se quiere carga manual (M) o datos de prueba (P).
        2. Mientras la respuesta no sea M, m, P o p, muestra un error y
           vuelve a preguntar.
        3. Si es M, pide los datos por teclado con cargar_estudiantes.
        4. Si es P, usa los datos hardcodeados de obtener_datos_prueba
           (Nota 0).
        5. Devuelve las 5 listas cargadas.

    Parámetros:
        No recibe parámetros.

    Retorna:
        tuple: (legajos, nombres, generos, notas1, notas2)
    """
    tipo = input("¿Carga manual (M) o datos de prueba (P)?: ")
    while tipo not in ["M", "m", "P", "p"]:
        print("Error: ingresá M o P.")
        tipo = input("¿Carga manual (M) o datos de prueba (P)?: ")

    if tipo == "M" or tipo == "m":
        datos = cargar_estudiantes()
    else:
        datos = obtener_datos_prueba()

    print("Datos cargados correctamente.")
    return datos


def opcion_mostrar_datos(legajos, nombres, generos, notas1, notas2):
    """
    Opción 2: muestra el informe con todos los estudiantes.

    Lógica:
        Llama a mostrar_estudiantes con el título "LISTADO DE
        ESTUDIANTES" y las 5 listas, sin promedios.

    Parámetros:
        legajos, nombres, generos, notas1, notas2 (list): listas paralelas.

    Retorna:
        No retorna nada (solo muestra).
    """
    mostrar_estudiantes("LISTADO DE ESTUDIANTES", legajos, nombres, generos, notas1, notas2)


def opcion_calcular_promedios(notas1, notas2):
    """
    Opción 3: calcula el promedio de cada estudiante.

    Lógica:
        Llama a calcular_promedios, muestra un mensaje de confirmación
        y devuelve la lista de promedios para que main la guarde.

    Parámetros:
        notas1 (list): notas del parcial 1.
        notas2 (list): notas del parcial 2.

    Retorna:
        list: lista de promedios (paralela a las demás).
    """
    promedios = calcular_promedios(notas1, notas2)
    print("Promedios calculados correctamente.")
    return promedios


def opcion_mostrar_ordenados(legajos, nombres, generos, notas1, notas2, promedios):
    """
    Opción 4: muestra los estudiantes ordenados por promedio de mayor
    a menor (DESC).

    Lógica:
        1. Llama a ordenar_por_promedio con orden "DESC", que devuelve
           copias de las 6 listas ordenadas (las originales no cambian).
        2. Muestra esas listas ordenadas con mostrar_estudiantes
           (reutiliza la función del punto 2).

    Parámetros:
        legajos, nombres, generos, notas1, notas2, promedios (list):
            listas paralelas.

    Retorna:
        No retorna nada (solo muestra).
    """
    leg, nom, gen, n1, n2, prom = ordenar_por_promedio(
        legajos, nombres, generos, notas1, notas2, promedios, "DESC")
    mostrar_estudiantes("ESTUDIANTES ORDENADOS POR PROMEDIO (DESC)",
                        leg, nom, gen, n1, n2, prom)


def opcion_mostrar_mayor_promedio(legajos, nombres, generos, notas1, notas2, promedios):
    """
    Opción 5: muestra el o los estudiantes con el mayor promedio.

    Lógica:
        1. Obtiene el valor del mayor promedio con obtener_mayor_promedio.
        2. Recorre los promedios y cuenta cuántos estudiantes tienen
           ese valor (puede haber empate).
        3. Crea 6 listas nuevas con ese tamaño ([0] * cantidad).
        4. Vuelve a recorrer y copia en esas listas los datos de los
           estudiantes que tienen el mayor promedio. La variable
           posicion indica en qué lugar de las listas nuevas se guarda.
        5. Muestra las listas nuevas con mostrar_estudiantes
           (reutiliza la función del punto 2).

    Parámetros:
        legajos, nombres, generos, notas1, notas2, promedios (list):
            listas paralelas.

    Retorna:
        No retorna nada (solo muestra).
    """
    mayor = obtener_mayor_promedio(promedios)

    cantidad = 0
    for i in range(len(promedios)):
        if promedios[i] == mayor:
            cantidad = cantidad + 1

    leg = [0] * cantidad
    nom = [""] * cantidad
    gen = [""] * cantidad
    n1 = [0] * cantidad
    n2 = [0] * cantidad
    prom = [0] * cantidad

    posicion = 0
    for i in range(len(promedios)):
        if promedios[i] == mayor:
            leg[posicion] = legajos[i]
            nom[posicion] = nombres[i]
            gen[posicion] = generos[i]
            n1[posicion] = notas1[i]
            n2[posicion] = notas2[i]
            prom[posicion] = promedios[i]
            posicion = posicion + 1

    mostrar_estudiantes("ESTUDIANTE/S CON MAYOR PROMEDIO", leg, nom, gen, n1, n2, prom)


def opcion_buscar_por_legajo(legajos, nombres, generos, notas1, notas2):
    """
    Opción 6: busca un estudiante por su legajo y muestra sus datos.

    Lógica:
        1. Pide el legajo a buscar y lo valida con validar_legajo
           (mientras no sea válido, lo vuelve a pedir).
        2. Busca su posición con buscar_por_legajo.
        3. Si la posición es -1, el legajo no existe: muestra un mensaje.
        4. Si existe, arma listas de un solo elemento con los datos de
           esa posición ([legajos[posicion]], etc.) y las muestra con
           mostrar_estudiantes (reutiliza la función del punto 2).

    Parámetros:
        legajos, nombres, generos, notas1, notas2 (list): listas paralelas.

    Retorna:
        No retorna nada (solo muestra).
    """
    texto = input("Ingresá el legajo a buscar: ")
    while not validar_legajo(texto):
        print("Error: el legajo debe ser un número entero positivo.")
        texto = input("Ingresá el legajo a buscar: ")

    posicion = buscar_por_legajo(legajos, int(texto))

    if posicion == -1:
        print("No se encontró ningún estudiante con ese legajo.")
    else:
        mostrar_estudiantes("DATOS DEL ESTUDIANTE",
                            [legajos[posicion]], [nombres[posicion]],
                            [generos[posicion]], [notas1[posicion]],
                            [notas2[posicion]])


def opcion_salir():
    """
    Opción 7: muestra un mensaje de despedida.

    Lógica:
        Solo imprime el mensaje. El programa termina porque el while
        de main.py deja de repetirse cuando la opción es "7".

    Parámetros:
        No recibe parámetros.

    Retorna:
        No retorna nada.
    """
    print("Saliendo del programa. ¡Hasta luego!")
