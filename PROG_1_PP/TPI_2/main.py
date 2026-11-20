"""
TP Lista de Diccionarios - Programa principal.

Procesa los datos de los estudiantes de una institución educativa (hasta
1000) guardados en una lista donde cada elemento es un diccionario con las
claves legajo, nombre, genero, notas y promedio.

El menú está dentro de un while (Nota 8) y usa match (Nota 7).
No se puede usar ninguna opción (salvo cargar o salir) sin antes haber
cargado los datos (Nota 1). Las opciones 4 y 6 además necesitan que los
promedios estén calculados (opción 3).

Este archivo no define funciones: todas están en la biblioteca propia
(módulos funciones y validaciones).
"""

from funciones import (mostrar_menu, opcion_cargar_datos, opcion_mostrar_datos,
                       opcion_calcular_promedios, opcion_ordenar_y_mostrar,
                       opcion_materias_mayor_promedio, opcion_buscar_estudiante,
                       opcion_contar_calificaciones, opcion_salir)
from validaciones import pedir_entero

# Lista de diccionarios (un diccionario por estudiante)
estudiantes = []

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
                estudiantes = opcion_cargar_datos()
                datos_cargados = True
                promedios_calculados = False
            case 2:
                opcion_mostrar_datos(estudiantes)
            case 3:
                promedios_calculados = opcion_calcular_promedios(estudiantes)
            case 4:
                opcion_ordenar_y_mostrar(estudiantes)
            case 5:
                opcion_materias_mayor_promedio(estudiantes)
            case 6:
                opcion_buscar_estudiante(estudiantes)
            case 7:
                opcion_contar_calificaciones(estudiantes)
            case 8:
                opcion_salir()
