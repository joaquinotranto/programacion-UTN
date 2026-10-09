"""
Programa principal.
Muestra el menú y llama a la función de cada opción.
Para ejecutarlo: python main.py
"""

from opciones import (opcion_cargar_datos, opcion_mostrar_datos,
                      opcion_calcular_promedios, opcion_mostrar_ordenados,
                      opcion_mostrar_mayor_promedio, opcion_buscar_por_legajo,
                      opcion_salir)


def mostrar_menu():
    """
    Muestra las opciones del menú por consola.
    """
    print("\n========== MENÚ ==========")
    print("1 - Cargar datos")
    print("2 - Mostrar todos los estudiantes")
    print("3 - Calcular promedios")
    print("4 - Mostrar estudiantes ordenados por promedio (DESC)")
    print("5 - Mostrar estudiante/s con mayor promedio")
    print("6 - Buscar estudiante por legajo")
    print("7 - Salir")


def main():
    """
    Función principal: guarda las listas y repite el menú hasta elegir salir.
    No deja usar las opciones 2 a 6 si antes no se cargaron los datos (Nota 1).
    """
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
            promedios = []  # si se recargan los datos, los promedios viejos ya no sirven

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


main()
