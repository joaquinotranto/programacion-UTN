"""
Módulo: menu.py

Descripción:
    Contiene la función que muestra el menú de opciones por consola
    (Nota 2 de la consigna). Está en un módulo aparte para que main.py
    no tenga funciones propias.

Funciones:
    mostrar_menu() -> None
"""


def mostrar_menu():
    """
    Muestra por consola las 7 opciones del menú.

    Lógica:
        Imprime un título y una línea por cada opción con print().

    Parámetros:
        No recibe parámetros.

    Retorna:
        No retorna nada (solo imprime).
    """
    print("\n========== MENÚ ==========")
    print("1 - Cargar datos")
    print("2 - Mostrar todos los estudiantes")
    print("3 - Calcular promedios")
    print("4 - Mostrar estudiantes ordenados por promedio (DESC)")
    print("5 - Mostrar estudiante/s con mayor promedio")
    print("6 - Buscar estudiante por legajo")
    print("7 - Salir")
