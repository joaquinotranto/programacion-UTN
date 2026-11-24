"""
Programa principal del TPI 3.

Administra el menú de estudiantes y coordina las funciones de la biblioteca.

Funcionamiento:
    Inicializa las estructuras y las banderas de carga y promedios.
    El while repite el menú hasta la opción 10. Se valida la opción
    y se impide operar sin datos o sin promedios cuando corresponde.
    match/case selecciona la función de cada opción. Al cargar nuevos
    datos se reinicia el estado de los promedios.
"""

from funciones import *
from validaciones import pedir_entero

estudiantes = []
datos_cargados = False
promedios_calculados = False
opcion = 0

while opcion != 10:
    mostrar_menu()
    opcion = pedir_entero("Ingrese una opción: ", 1, 10)
    if opcion not in (1, 2, 10) and not datos_cargados:
        print("Primero debe cargar los datos.")
    elif opcion in (5, 7) and not promedios_calculados:
        print("Primero debe calcular los promedios (opción 4).")
    else:
        match opcion:
            case 1:
                nuevos = opcion_cargar_csv()
                if len(nuevos) > 0:
                    estudiantes = nuevos
                    datos_cargados = True
                    promedios_calculados = False
            case 2:
                estudiantes = opcion_cargar_datos()
                datos_cargados = len(estudiantes) > 0
                promedios_calculados = False
            case 3:
                opcion_mostrar_datos(estudiantes)
            case 4:
                promedios_calculados = opcion_calcular_promedios(estudiantes)
            case 5:
                opcion_ordenar_y_mostrar(estudiantes)
            case 6:
                opcion_materias_mayor_promedio(estudiantes)
            case 7:
                opcion_buscar_estudiante(estudiantes)
            case 8:
                opcion_contar_calificaciones(estudiantes)
            case 9:
                opcion_guardar_json(estudiantes)
            case 10:
                opcion_salir()
