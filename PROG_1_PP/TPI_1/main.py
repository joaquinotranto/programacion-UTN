"""
TP Listas y Matrices - Programa principal.

Procesa los datos de 30 estudiantes de una institución educativa usando
una matriz de calificaciones (30 filas x 5 materias) y listas paralelas de
nombres, géneros, legajos y promedios.

El menú está dentro de un while (Nota 8) y usa match (Nota 7).
No se puede usar ninguna opción (salvo cargar o salir) sin antes haber
cargado los datos (Nota 1). Las opciones 4 y 6 además necesitan que los
promedios estén calculados (opción 3).

Este archivo no define funciones: todas están en la biblioteca propia
(módulos funciones y validaciones).
"""

from funciones import (CANTIDAD_ESTUDIANTES, CANTIDAD_MATERIAS, crear_matriz, mostrar_menu,
                       opcion_cargar_datos, opcion_mostrar_datos, opcion_calcular_promedios,
                       opcion_ordenar_y_mostrar, opcion_materias_mayor_promedio,
                       opcion_buscar_estudiante, opcion_contar_calificaciones)
from validaciones import pedir_entero

# Estructuras de datos (listas paralelas a las filas de la matriz)
calificaciones = crear_matriz(CANTIDAD_ESTUDIANTES, CANTIDAD_MATERIAS, 0)
nombres = [""] * CANTIDAD_ESTUDIANTES
generos = [""] * CANTIDAD_ESTUDIANTES
legajos = [0] * CANTIDAD_ESTUDIANTES
promedios = [0.0] * CANTIDAD_ESTUDIANTES

# Banderas de control
datos_cargados = False
promedios_calculados = False
opcion = 0

while opcion != 8:
    mostrar_menu()
    opcion = pedir_entero("Ingrese una opción: ", 1, 8)

    if opcion != 1 and opcion != 8 and not datos_cargados:
        print("\nPrimero tiene que cargar los datos (opción 1).")
    elif (opcion == 4 or opcion == 6) and not promedios_calculados:
        print("\nPrimero tiene que calcular los promedios (opción 3).")
    else:
        match opcion:
            case 1:
                datos_cargados = opcion_cargar_datos(calificaciones, nombres, generos, legajos)
                promedios_calculados = False
            case 2:
                opcion_mostrar_datos(calificaciones, nombres, generos, legajos)
            case 3:
                promedios_calculados = opcion_calcular_promedios(calificaciones, promedios)
            case 4:
                opcion_ordenar_y_mostrar(calificaciones, nombres, generos, legajos, promedios)
            case 5:
                opcion_materias_mayor_promedio(calificaciones)
            case 6:
                opcion_buscar_estudiante(calificaciones, nombres, generos, legajos, promedios)
            case 7:
                opcion_contar_calificaciones(calificaciones)
            case 8:
                print("\nSaliendo del programa. ¡Hasta luego!")
