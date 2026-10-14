"""
Módulo: carga.py

Descripción:
    Se encarga de pedir los datos de los estudiantes por consola.
    Tiene una función para pedir cada dato (legajo, nombre, género y
    nota) y una función que carga los datos de todos los estudiantes.

Funcionamiento general:
    Cada función "pedir_..." pide el dato con input() y, mientras el
    dato NO sea válido (según las funciones de validaciones.py),
    muestra un mensaje de error y lo vuelve a pedir con un ciclo while.
    Se usa while y no for porque no se sabe cuántas veces se va a
    equivocar el usuario.

Funciones:
    pasar_a_mayuscula(letra)          -> str
    pedir_legajo(legajos_cargados)    -> int
    pedir_nombre()                    -> str
    pedir_genero()                    -> str
    pedir_nota(numero_parcial)        -> int
    cargar_estudiantes()              -> tuple de 5 listas
"""

from constantes import CANTIDAD_ESTUDIANTES
from validaciones import validar_legajo, validar_nombre, validar_genero, validar_nota


def pasar_a_mayuscula(letra):
    """
    Convierte una letra de género en minúscula (f, m, x) a mayúscula.

    Lógica:
        Compara la letra con "f", "m" y "x". Si coincide con alguna,
        devuelve su versión en mayúscula. Si no, la devuelve igual
        (porque ya estaba en mayúscula).

    Parámetros:
        letra (str): una letra de género (F, M, X, f, m o x).

    Retorna:
        str: la letra en mayúscula.

    Ejemplos:
        pasar_a_mayuscula("f") -> "F"
        pasar_a_mayuscula("M") -> "M"
    """
    if letra == "f":
        return "F"
    if letra == "m":
        return "M"
    if letra == "x":
        return "X"
    return letra


def pedir_legajo(legajos_cargados):
    """
    Pide un legajo por consola hasta que sea válido y no esté repetido.

    Lógica:
        1. Pide el legajo con input().
        2. Mientras no sea válido (validar_legajo da False) o ya esté
           en la lista de legajos cargados (operador in), muestra un
           error y lo vuelve a pedir.
        3. Cuando es válido, lo convierte a entero y lo devuelve.
        Que no se repita es importante para que la búsqueda por legajo
        (opción 6) encuentre a un solo estudiante.

    Parámetros:
        legajos_cargados (list): legajos que ya se cargaron.

    Retorna:
        int: el legajo válido y no repetido.
    """
    legajo = input("Legajo: ")
    while not validar_legajo(legajo) or int(legajo) in legajos_cargados:
        print("Error: el legajo debe ser un número entero positivo y no puede repetirse.")
        legajo = input("Legajo: ")
    return int(legajo)


def pedir_nombre():
    """
    Pide el apellido y nombre por consola hasta que sea válido.

    Lógica:
        1. Pide el nombre con input().
        2. Mientras validar_nombre devuelva False, muestra un error y
           lo vuelve a pedir.
        3. Cuando es válido, lo devuelve.

    Parámetros:
        No recibe parámetros.

    Retorna:
        str: el apellido y nombre válido (solo letras y espacios).
    """
    nombre = input("Apellido y nombre: ")
    while not validar_nombre(nombre):
        print("Error: el apellido y nombre solo puede tener letras.")
        nombre = input("Apellido y nombre: ")
    return nombre


def pedir_genero():
    """
    Pide el género por consola hasta que sea F, M o X.

    Lógica:
        1. Pide el género con input().
        2. Mientras validar_genero devuelva False, muestra un error y
           lo vuelve a pedir.
        3. Cuando es válido, lo pasa a mayúscula con pasar_a_mayuscula
           (así siempre se guarda igual) y lo devuelve.

    Parámetros:
        No recibe parámetros.

    Retorna:
        str: "F", "M" o "X".
    """
    genero = input("Género (F/M/X): ")
    while not validar_genero(genero):
        print("Error: el género debe ser F, M o X.")
        genero = input("Género (F/M/X): ")
    return pasar_a_mayuscula(genero)


def pedir_nota(numero_parcial):
    """
    Pide la nota de un parcial por consola hasta que sea válida.

    Lógica:
        1. Pide la nota con input(). El mensaje muestra el número de
           parcial usando un f-string.
        2. Mientras validar_nota devuelva False, muestra un error y la
           vuelve a pedir.
        3. Cuando es válida, la convierte a entero y la devuelve.

    Parámetros:
        numero_parcial (int): 1 o 2. Solo se usa para el mensaje, así
            la misma función sirve para los dos parciales.

    Retorna:
        int: la nota válida (entre 1 y 10).
    """
    nota = input(f"Nota del parcial {numero_parcial} (1 a 10): ")
    while not validar_nota(nota):
        print("Error: la nota debe ser un número entero entre 1 y 10.")
        nota = input(f"Nota del parcial {numero_parcial} (1 a 10): ")
    return int(nota)


def cargar_estudiantes():
    """
    Carga por consola los datos de todos los estudiantes en 5 listas
    paralelas (la misma posición corresponde al mismo estudiante).

    Lógica:
        1. Crea las 5 listas con su tamaño fijo usando [valor] * cantidad.
           Por ejemplo, [0] * 30 crea una lista con 30 ceros.
        2. Con un for recorre las posiciones de 0 a 29.
        3. En cada vuelta pide los 5 datos de un estudiante y los guarda
           en la posición i de cada lista (lista[i] = dato).
           Así las 5 listas se completan juntas y quedan paralelas.
        4. Devuelve las 5 listas.

    Parámetros:
        No recibe parámetros.

    Retorna:
        tuple: (legajos, nombres, generos, notas1, notas2)
    """
    legajos = [0] * CANTIDAD_ESTUDIANTES
    nombres = [""] * CANTIDAD_ESTUDIANTES
    generos = [""] * CANTIDAD_ESTUDIANTES
    notas1 = [0] * CANTIDAD_ESTUDIANTES
    notas2 = [0] * CANTIDAD_ESTUDIANTES

    for i in range(CANTIDAD_ESTUDIANTES):
        print(f"\n--- Estudiante {i + 1} de {CANTIDAD_ESTUDIANTES} ---")
        legajos[i] = pedir_legajo(legajos)
        nombres[i] = pedir_nombre()
        generos[i] = pedir_genero()
        notas1[i] = pedir_nota(1)
        notas2[i] = pedir_nota(2)

    return legajos, nombres, generos, notas1, notas2
