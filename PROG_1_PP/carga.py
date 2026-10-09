"""
Módulo carga.
Contiene una función para pedir cada dato por consola (validándolo)
y una función que carga los datos de todos los estudiantes.
"""

from constantes import CANTIDAD_ESTUDIANTES
from validaciones import validar_legajo, validar_nombre, validar_genero, validar_nota


def pedir_legajo(legajos_cargados):
    """
    Pide un legajo hasta que sea válido y no esté repetido.

    Parámetros:
        legajos_cargados (list): legajos que ya se cargaron, para no repetir.
    Retorna:
        int: el legajo válido.
    """
    legajo = input("Legajo: ")
    while not validar_legajo(legajo) or int(legajo) in legajos_cargados:
        print("Error: el legajo debe ser un número entero positivo y no puede repetirse.")
        legajo = input("Legajo: ")
    return int(legajo)


def pedir_nombre():
    """
    Pide el apellido y nombre hasta que sea válido (solo letras).

    Retorna:
        str: el apellido y nombre válido.
    """
    nombre = input("Apellido y nombre: ")
    while not validar_nombre(nombre):
        print("Error: el apellido y nombre solo puede tener letras.")
        nombre = input("Apellido y nombre: ")
    return nombre.strip()


def pedir_genero():
    """
    Pide el género hasta que sea 'F', 'M' o 'X'.

    Retorna:
        str: el género en mayúscula.
    """
    genero = input("Género (F/M/X): ")
    while not validar_genero(genero):
        print("Error: el género debe ser F, M o X.")
        genero = input("Género (F/M/X): ")
    return genero.upper()


def pedir_nota(numero_parcial):
    """
    Pide la nota de un parcial hasta que sea un entero entre 1 y 10.

    Parámetros:
        numero_parcial (int): 1 o 2, solo para mostrar en el mensaje.
    Retorna:
        int: la nota válida.
    """
    nota = input(f"Nota del parcial {numero_parcial} (1 a 10): ")
    while not validar_nota(nota):
        print("Error: la nota debe ser un número entero entre 1 y 10.")
        nota = input(f"Nota del parcial {numero_parcial} (1 a 10): ")
    return int(nota)


def cargar_estudiantes():
    """
    Carga por consola los datos de todos los estudiantes en listas paralelas.
    La posición i de cada lista corresponde al mismo estudiante.

    Retorna:
        tuple: (legajos, nombres, generos, notas1, notas2)
    """
    legajos = []
    nombres = []
    generos = []
    notas1 = []
    notas2 = []

    for i in range(CANTIDAD_ESTUDIANTES):
        print(f"\n--- Estudiante {i + 1} de {CANTIDAD_ESTUDIANTES} ---")
        legajos.append(pedir_legajo(legajos))
        nombres.append(pedir_nombre())
        generos.append(pedir_genero())
        notas1.append(pedir_nota(1))
        notas2.append(pedir_nota(2))

    return legajos, nombres, generos, notas1, notas2
