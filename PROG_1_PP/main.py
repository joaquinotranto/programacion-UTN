"""
Módulo: main.py  (programa principal)

Descripción:
    Es el archivo que se ejecuta para iniciar el programa
    (python main.py). Gestiona los datos de 30 estudiantes (legajo,
    apellido y nombre, género y notas de dos parciales) guardados en
    listas paralelas: la misma posición en cada lista corresponde al
    mismo estudiante.

    Este archivo NO define funciones: solo importa las funciones de
    los otros módulos y controla el flujo del menú.

Funcionamiento:
    1. Crea las 6 listas vacías: legajos, nombres, generos, notas1,
       notas2 y promedios.
    2. Con un ciclo while muestra el menú (mostrar_menu, del módulo
       menu.py) y pide una opción, hasta que se elija la 7 (Salir).
       La opción se compara como texto ("1", "2", ...) porque input()
       siempre devuelve texto; así, si se escribe cualquier otra cosa,
       el programa no se rompe y muestra "Opción inválida".
    3. Según la opción, llama a la función correspondiente del módulo
       opciones.py (una función por opción, Nota 3).

Validaciones del menú:
    - Nota 1: no se puede acceder a las opciones 2 a 6 sin antes haber
      cargado los datos. Se controla preguntando si la lista de legajos
      está vacía (len(legajos) == 0).
    - Las opciones 4 y 5 necesitan los promedios, por eso también se
      controla que la lista de promedios no esté vacía.
    - Si se vuelven a cargar los datos (opción 1), se vacía la lista de
      promedios, porque los promedios anteriores ya no corresponden.

Módulos que utiliza:
    menu.py, opciones.py (que a su vez usa carga.py, validaciones.py,
    mostrar.py, calculos.py, datos_prueba.py y constantes.py).
"""

from menu import mostrar_menu
from opciones import (opcion_cargar_datos, opcion_mostrar_datos,
                      opcion_calcular_promedios, opcion_mostrar_ordenados,
                      opcion_mostrar_mayor_promedio, opcion_buscar_por_legajo,
                      opcion_salir)

legajos = []
nombres = []
generos = []
notas1 = []
notas2 = []
promedios = []

opcion = ""
while opcion != "7":
    mostrar_menu()
    opcion = input("Elegí una opción: ")

    if opcion == "1":
        legajos, nombres, generos, notas1, notas2 = opcion_cargar_datos()
        promedios = []

    elif opcion == "7":
        opcion_salir()

    elif opcion in ["2", "3", "4", "5", "6"]:
        if len(legajos) == 0:
            print("Primero tenés que cargar los datos (opción 1).")

        elif opcion == "2":
            opcion_mostrar_datos(legajos, nombres, generos, notas1, notas2)

        elif opcion == "3":
            promedios = opcion_calcular_promedios(notas1, notas2)

        elif opcion == "6":
            opcion_buscar_por_legajo(legajos, nombres, generos, notas1, notas2)

        elif len(promedios) == 0:
            print("Primero tenés que calcular los promedios (opción 3).")

        elif opcion == "4":
            opcion_mostrar_ordenados(legajos, nombres, generos, notas1, notas2, promedios)

        elif opcion == "5":
            opcion_mostrar_mayor_promedio(legajos, nombres, generos, notas1, notas2, promedios)

    else:
        print("Opción inválida. Elegí un número del 1 al 7.")
