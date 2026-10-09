"""
Módulo opciones.
Cada opción del menú es una función (Nota 3 de la consigna).
"""

from carga import cargar_estudiantes
from datos_prueba import obtener_datos_prueba
from mostrar import mostrar_estudiantes
from calculos import (calcular_promedios, ordenar_por_promedio,
                      obtener_mayor_promedio, buscar_por_legajo)
from validaciones import validar_legajo


def opcion_cargar_datos():
    """
    Opción 1: carga los datos de los estudiantes.
    Permite elegir carga manual o datos de prueba hardcodeados.

    Retorna:
        tuple: (legajos, nombres, generos, notas1, notas2)
    """
    tipo = input("¿Carga manual (M) o datos de prueba (P)?: ").upper()
    while tipo != "M" and tipo != "P":
        print("Error: ingresá M o P.")
        tipo = input("¿Carga manual (M) o datos de prueba (P)?: ").upper()

    if tipo == "M":
        datos = cargar_estudiantes()
    else:
        datos = obtener_datos_prueba()

    print("Datos cargados correctamente.")
    return datos


def opcion_mostrar_datos(legajos, nombres, generos, notas1, notas2):
    """
    Opción 2: muestra el informe con todos los estudiantes.
    """
    mostrar_estudiantes("LISTADO DE ESTUDIANTES", legajos, nombres, generos, notas1, notas2)


def opcion_calcular_promedios(notas1, notas2):
    """
    Opción 3: calcula el promedio de cada estudiante.

    Retorna:
        list: lista de promedios.
    """
    promedios = calcular_promedios(notas1, notas2)
    print("Promedios calculados correctamente.")
    return promedios


def opcion_mostrar_ordenados(legajos, nombres, generos, notas1, notas2, promedios):
    """
    Opción 4: muestra los estudiantes ordenados por promedio de mayor a menor.
    """
    leg, nom, gen, n1, n2, prom = ordenar_por_promedio(
        legajos, nombres, generos, notas1, notas2, promedios, "DESC")
    mostrar_estudiantes("ESTUDIANTES ORDENADOS POR PROMEDIO (DESC)",
                        leg, nom, gen, n1, n2, prom)


def opcion_mostrar_mayor_promedio(legajos, nombres, generos, notas1, notas2, promedios):
    """
    Opción 5: muestra el/los estudiante/s con el mayor promedio.
    Arma listas nuevas solo con los que tienen el mayor promedio
    y reutiliza mostrar_estudiantes.
    """
    mayor = obtener_mayor_promedio(promedios)

    leg = []
    nom = []
    gen = []
    n1 = []
    n2 = []
    prom = []
    for i in range(len(promedios)):
        if promedios[i] == mayor:
            leg.append(legajos[i])
            nom.append(nombres[i])
            gen.append(generos[i])
            n1.append(notas1[i])
            n2.append(notas2[i])
            prom.append(promedios[i])

    mostrar_estudiantes("ESTUDIANTE/S CON MAYOR PROMEDIO", leg, nom, gen, n1, n2, prom)


def opcion_buscar_por_legajo(legajos, nombres, generos, notas1, notas2):
    """
    Opción 6: pide un legajo, lo busca y muestra los datos del estudiante.
    Reutiliza mostrar_estudiantes pasando listas de un solo elemento.
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
    """
    print("Saliendo del programa. ¡Hasta luego!")
