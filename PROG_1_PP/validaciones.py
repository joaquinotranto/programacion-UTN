"""
Módulo: validaciones.py

Descripción:
    Contiene una función de validación para cada dato del estudiante
    (Nota 5 de la consigna): legajo, apellido y nombre, género y notas.
    También contiene dos funciones auxiliares (es_numero y es_letra)
    que usan las validaciones.

Funcionamiento general:
    Todas las funciones reciben el texto que escribió el usuario
    (input siempre devuelve texto) y devuelven True si el dato es
    válido o False si no lo es.
    No se usan métodos de Python: los textos se recorren caracter por
    caracter con un for y se comparan con los operadores <, >, ==.

Funciones:
    es_numero(texto)       -> bool
    es_letra(caracter)     -> bool
    validar_legajo(texto)  -> bool
    validar_nombre(texto)  -> bool
    validar_genero(texto)  -> bool
    validar_nota(texto)    -> bool
"""

from constantes import NOTA_MINIMA, NOTA_MAXIMA


def es_numero(texto):
    """
    Verifica que un texto contenga solamente dígitos (0 a 9).

    Lógica:
        1. Si el texto está vacío (len == 0), no es un número: devuelve False.
        2. Recorre el texto caracter por caracter con un for.
        3. Si encuentra un caracter menor que "0" o mayor que "9",
           no es un dígito: devuelve False.
        4. Si termina de recorrer sin encontrar errores, devuelve True.

    Parámetros:
        texto (str): el texto a verificar.

    Retorna:
        bool: True si todos los caracteres son dígitos, False si no.

    Ejemplos:
        es_numero("123") -> True
        es_numero("12a") -> False
        es_numero("")    -> False
    """
    if len(texto) == 0:
        return False
    for caracter in texto:
        if caracter < "0" or caracter > "9":
            return False
    return True


def es_letra(caracter):
    """
    Verifica si un caracter es una letra.

    Lógica:
        Compara el caracter con los rangos de letras:
        - entre "a" y "z" (minúsculas)
        - entre "A" y "Z" (mayúsculas)
        - o si es una letra con tilde, ñ o ü (se busca con el operador in).
        Si cumple alguna, devuelve True; si no, devuelve False.

    Parámetros:
        caracter (str): un solo caracter.

    Retorna:
        bool: True si es una letra, False si no.

    Ejemplos:
        es_letra("a") -> True
        es_letra("Ñ") -> True
        es_letra("3") -> False
    """
    if caracter >= "a" and caracter <= "z":
        return True
    if caracter >= "A" and caracter <= "Z":
        return True
    if caracter in "áéíóúÁÉÍÓÚñÑüÜ":
        return True
    return False


def validar_legajo(texto):
    """
    Valida que el legajo sea un número entero positivo.

    Lógica:
        1. Verifica con es_numero que el texto tenga solo dígitos.
        2. Si es así, lo convierte a entero con int() y verifica que
           sea mayor a 0.
        El operador and evalúa primero la izquierda: si es_numero da
        False, no se ejecuta int(), y así se evita un error al
        convertir un texto con letras.

    Parámetros:
        texto (str): el legajo tal como lo escribió el usuario.

    Retorna:
        bool: True si es un entero mayor a 0, False si no.

    Ejemplos:
        validar_legajo("1001") -> True
        validar_legajo("0")    -> False
        validar_legajo("abc")  -> False
    """
    return es_numero(texto) and int(texto) > 0


def validar_nombre(texto):
    """
    Valida que el apellido y nombre tenga solo letras y espacios.

    Lógica:
        1. Empieza suponiendo que no hay ninguna letra (tiene_letra = False).
        2. Recorre el texto caracter por caracter.
        3. Los espacios se ignoran (se permiten entre palabras).
        4. Si un caracter no es espacio y tampoco es letra, devuelve False.
        5. Si es letra, marca tiene_letra = True.
        6. Al final devuelve tiene_letra: así se rechaza un texto vacío
           o que tenga solo espacios.

    Parámetros:
        texto (str): el apellido y nombre tal como lo escribió el usuario.

    Retorna:
        bool: True si tiene al menos una letra y solo letras/espacios.

    Ejemplos:
        validar_nombre("Gomez Ana") -> True
        validar_nombre("Ana 2")     -> False
        validar_nombre("   ")       -> False
    """
    tiene_letra = False
    for caracter in texto:
        if caracter != " ":
            if not es_letra(caracter):
                return False
            tiene_letra = True
    return tiene_letra


def validar_genero(texto):
    """
    Valida que el género sea F, M o X (acepta también minúsculas).

    Lógica:
        Verifica con el operador in si el texto está dentro de la lista
        de valores permitidos: F, M, X, f, m, x.

    Parámetros:
        texto (str): el género tal como lo escribió el usuario.

    Retorna:
        bool: True si es un género válido, False si no.

    Ejemplos:
        validar_genero("F") -> True
        validar_genero("m") -> True
        validar_genero("Z") -> False
    """
    return texto in ["F", "M", "X", "f", "m", "x"]


def validar_nota(texto):
    """
    Valida que la nota sea un número entero entre 1 y 10 (incluidos).

    Lógica:
        1. Verifica con es_numero que el texto tenga solo dígitos.
        2. Si es así, lo convierte a entero y verifica que sea mayor o
           igual a NOTA_MINIMA (1) y menor o igual a NOTA_MAXIMA (10).
        Se usa la misma función para la nota del parcial 1 y del
        parcial 2, porque las dos tienen la misma regla.

    Parámetros:
        texto (str): la nota tal como la escribió el usuario.

    Retorna:
        bool: True si es un entero entre 1 y 10, False si no.

    Ejemplos:
        validar_nota("7")  -> True
        validar_nota("11") -> False
        validar_nota("a")  -> False
    """
    return es_numero(texto) and int(texto) >= NOTA_MINIMA and int(texto) <= NOTA_MAXIMA
