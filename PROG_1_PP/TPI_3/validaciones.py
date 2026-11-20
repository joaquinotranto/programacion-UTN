"""
Módulo validaciones.

Biblioteca propia con una función de validación para cada dato que se carga
en el programa (Nota 5 del TP): legajo, nombre, género y notas.
También incluye funciones para pedir datos por consola que repiten la
pregunta hasta que el usuario ingresa un valor válido.

"""

LETRAS_ESPECIALES = "áéíóúÁÉÍÓÚñÑüÜ"


def es_numero_entero(texto: str) -> bool:
    """
    Verifica si un texto está formado solamente por dígitos (0 al 9).

    Recorre el texto caracter por caracter y compara cada uno contra el
    rango '0'..'9'. Un texto vacío no se considera número.

    Args:
        texto (str): Texto ingresado por el usuario.

    Returns:
        bool: True si el texto no está vacío y todos sus caracteres son
        dígitos; False en caso contrario.
    """
    if len(texto) == 0:
        return False
    for caracter in texto:
        if caracter < "0" or caracter > "9":
            return False
    return True


def validar_rango(numero: int, minimo: int, maximo: int) -> bool:
    """
    Verifica que un número entero esté dentro de un rango (incluye los bordes).

    Args:
        numero (int): Número a validar.
        minimo (int): Valor mínimo permitido.
        maximo (int): Valor máximo permitido.

    Returns:
        bool: True si minimo <= numero <= maximo; False en caso contrario.
    """
    return numero >= minimo and numero <= maximo


def validar_calificacion(calificacion: int) -> bool:
    """
    Verifica que una calificación sea un entero entre 1 y 10.

    Args:
        calificacion (int): Nota a validar.

    Returns:
        bool: True si la nota está entre 1 y 10 inclusive; False si no.
    """
    return validar_rango(calificacion, 1, 10)


def validar_notas(notas: list) -> bool:
    """
    Verifica que las notas de un estudiante sean una lista de cinco (5)
    calificaciones enteras entre 1 y 10.

    Args:
        notas (list): Lista de calificaciones del estudiante.

    Returns:
        bool: True si la lista tiene 5 elementos y todos son notas válidas;
        False en caso contrario.
    """
    if len(notas) != 5:
        return False
    for nota in notas:
        if not validar_calificacion(nota):
            return False
    return True


def es_letra(caracter: str) -> bool:
    """
    Verifica si un caracter es una letra (incluye acentos, ñ y ü).

    Args:
        caracter (str): Un único caracter.

    Returns:
        bool: True si es una letra mayúscula o minúscula; False si no.
    """
    es_minuscula = caracter >= "a" and caracter <= "z"
    es_mayuscula = caracter >= "A" and caracter <= "Z"
    return es_minuscula or es_mayuscula or caracter in LETRAS_ESPECIALES


def validar_nombre(nombre: str) -> bool:
    """
    Verifica que un nombre sea válido.

    Un nombre es válido si tiene al menos 2 caracteres, está formado solo
    por letras y espacios, y contiene al menos una letra.

    Args:
        nombre (str): Nombre del estudiante.

    Returns:
        bool: True si el nombre es válido; False en caso contrario.
    """
    if len(nombre) < 2:
        return False
    tiene_letra = False
    for caracter in nombre:
        if es_letra(caracter):
            tiene_letra = True
        elif caracter != " ":
            return False
    return tiene_letra


def validar_genero(genero: str) -> bool:
    """
    Verifica que el género sea 'F', 'M' o 'X' (en mayúscula).

    Args:
        genero (str): Género del estudiante.

    Returns:
        bool: True si el género es 'F', 'M' o 'X'; False en caso contrario.
    """
    return genero == "F" or genero == "M" or genero == "X"


def validar_legajo(legajo: int, estudiantes: list, cantidad_cargados: int) -> bool:
    """
    Verifica que un legajo sea un entero de cinco cifras y que no esté repetido.

    Un número de cinco cifras está entre 10000 y 99999. Además se revisan
    los estudiantes ya cargados (de la posición 0 hasta cantidad_cargados - 1)
    comparando la clave "legajo" de cada diccionario, para que no haya dos
    estudiantes con el mismo legajo.

    Args:
        legajo (int): Legajo a validar.
        estudiantes (list): Lista de diccionarios de estudiantes.
        cantidad_cargados (int): Cuántos estudiantes de la lista ya están cargados.

    Returns:
        bool: True si el legajo tiene cinco cifras y no está repetido;
        False en caso contrario.
    """
    if not validar_rango(legajo, 10000, 99999):
        return False
    for i in range(cantidad_cargados):
        if estudiantes[i]["legajo"] == legajo:
            return False
    return True


def pedir_entero(mensaje: str, minimo: int, maximo: int) -> int:
    """
    Pide un número entero por consola hasta que sea válido y esté en rango.

    Args:
        mensaje (str): Texto que se muestra al pedir el dato.
        minimo (int): Valor mínimo aceptado.
        maximo (int): Valor máximo aceptado.

    Returns:
        int: El número ingresado, ya validado.
    """
    texto = input(mensaje)
    while not es_numero_entero(texto) or not validar_rango(int(texto), minimo, maximo):
        print(f"  Error: ingrese un número entero entre {minimo} y {maximo}.")
        texto = input(mensaje)
    return int(texto)


def pedir_calificacion(mensaje: str) -> int:
    """
    Pide una calificación por consola hasta que sea un entero entre 1 y 10.

    Args:
        mensaje (str): Texto que se muestra al pedir la nota.

    Returns:
        int: La calificación ingresada, ya validada.
    """
    texto = input(mensaje)
    while not es_numero_entero(texto) or not validar_calificacion(int(texto)):
        print("  Error: la calificación debe ser un entero entre 1 y 10.")
        texto = input(mensaje)
    return int(texto)


def pedir_nombre(mensaje: str) -> str:
    """
    Pide el nombre de un estudiante hasta que sea válido.

    Args:
        mensaje (str): Texto que se muestra al pedir el nombre.

    Returns:
        str: El nombre ingresado, ya validado.
    """
    nombre = input(mensaje)
    while not validar_nombre(nombre):
        print("  Error: el nombre solo puede tener letras y espacios (mínimo 2 caracteres).")
        nombre = input(mensaje)
    return nombre


def convertir_genero(texto: str) -> str:
    """
    Convierte 'f', 'm' o 'x' en minúscula a su versión en mayúscula.

    Se hace con comparaciones para no usar el método upper(). Si el texto
    no es una de esas letras, se devuelve igual que vino.

    Args:
        texto (str): Género ingresado por el usuario.

    Returns:
        str: El género en mayúscula, o el texto original si no corresponde.
    """
    if texto == "f":
        return "F"
    if texto == "m":
        return "M"
    if texto == "x":
        return "X"
    return texto


def pedir_genero(mensaje: str) -> str:
    """
    Pide el género de un estudiante hasta que sea 'F', 'M' o 'X'.

    Acepta también las letras en minúscula y las convierte a mayúscula.

    Args:
        mensaje (str): Texto que se muestra al pedir el género.

    Returns:
        str: 'F', 'M' o 'X'.
    """
    genero = convertir_genero(input(mensaje))
    while not validar_genero(genero):
        print("  Error: el género debe ser F, M o X.")
        genero = convertir_genero(input(mensaje))
    return genero


def pedir_legajo(mensaje: str, estudiantes: list, cantidad_cargados: int) -> int:
    """
    Pide un legajo hasta que sea un entero de cinco cifras no repetido.

    Args:
        mensaje (str): Texto que se muestra al pedir el legajo.
        estudiantes (list): Lista de diccionarios de estudiantes.
        cantidad_cargados (int): Cuántos estudiantes ya están cargados.

    Returns:
        int: El legajo ingresado, ya validado.
    """
    texto = input(mensaje)
    while not es_numero_entero(texto) or not validar_legajo(int(texto), estudiantes, cantidad_cargados):
        print("  Error: el legajo debe ser un número de 5 cifras y no puede repetirse.")
        texto = input(mensaje)
    return int(texto)
