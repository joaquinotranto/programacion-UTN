"""
Módulo validaciones.
Contiene una función de validación para cada dato del estudiante.
Todas reciben el texto que escribió el usuario (input siempre devuelve texto)
y devuelven True si el dato es válido o False si no lo es.
"""

from constantes import GENEROS_VALIDOS, NOTA_MINIMA, NOTA_MAXIMA


def validar_legajo(texto):
    """
    Valida que el legajo sea un número entero positivo.

    Parámetros:
        texto (str): lo que ingresó el usuario.
    Retorna:
        bool: True si es un entero mayor a 0, False en caso contrario.
    """
    return texto.isdigit() and int(texto) > 0


def validar_nombre(texto):
    """
    Valida que el apellido y nombre tenga solo letras (se permiten espacios
    entre las palabras, por ejemplo "Gomez Ana").

    Parámetros:
        texto (str): lo que ingresó el usuario.
    Retorna:
        bool: True si tiene solo letras y no está vacío, False en caso contrario.
    """
    sin_espacios = texto.replace(" ", "")
    return len(sin_espacios) > 0 and sin_espacios.isalpha()


def validar_genero(texto):
    """
    Valida que el género sea 'F', 'M' o 'X' (acepta minúsculas).

    Parámetros:
        texto (str): lo que ingresó el usuario.
    Retorna:
        bool: True si el género es válido, False en caso contrario.
    """
    return texto.upper() in GENEROS_VALIDOS


def validar_nota(texto):
    """
    Valida que la nota sea un número entero entre 1 y 10.

    Parámetros:
        texto (str): lo que ingresó el usuario.
    Retorna:
        bool: True si la nota es válida, False en caso contrario.
    """
    return texto.isdigit() and NOTA_MINIMA <= int(texto) <= NOTA_MAXIMA
