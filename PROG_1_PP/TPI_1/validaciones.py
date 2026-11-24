"""
Módulo validaciones.

Biblioteca propia con una función de validación para cada dato que se carga
en el programa (Nota 5 del TP): calificaciones, nombres, géneros y legajos.
También incluye funciones para pedir datos por consola que repiten la
pregunta hasta que el usuario ingresa un valor válido.

Funciones del módulo:
    es_numero_entero()
    validar_rango()
    validar_calificacion()
    es_letra()
    validar_nombre()
    validar_genero()
    validar_legajo()
    pedir_entero()
    pedir_calificacion()
    pedir_nombre()
    convertir_genero()
    pedir_genero()
    pedir_legajo()
"""

LETRAS_ESPECIALES = "áéíóúÁÉÍÓÚñÑüÜ"


def es_numero_entero(texto: str) -> bool:
    """
    Verifica si un texto está formado solamente por dígitos (0 al 9).

    Recorre el texto caracter por caracter y compara cada uno contra el
    rango '0'..'9'. Un texto vacío no se considera número.

    Lógica:
        Rechaza el texto vacío. Recorre cada carácter y devuelve False si está fuera de 0 a
        9. Solo devuelve True después de revisar todos los caracteres.

    Parámetros:
        texto (str): Texto ingresado por el usuario.

    Retorna:
        bool: True si el texto no está vacío y todos sus caracteres son
        dígitos; False en caso contrario.

    Ejemplo:
        es_numero_entero("123") -> True; es_numero_entero("12a") -> False
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

    Lógica:
        Compara el número con ambos límites usando and. Los operadores >= y <= incluyen los
        extremos. No convierte el dato ni verifica su tipo por separado.

    Parámetros:
        numero (int): Número a validar.
        minimo (int): Valor mínimo permitido.
        maximo (int): Valor máximo permitido.

    Retorna:
        bool: True si minimo <= numero <= maximo; False en caso contrario.

    Ejemplo:
        validar_rango(5, 1, 10) -> True
    """
    return numero >= minimo and numero <= maximo


def validar_calificacion(calificacion: int) -> bool:
    """
    Verifica que una calificación sea un entero entre 1 y 10.

    Lógica:
        Reutiliza validar_rango con los límites 1 y 10. La conversión a entero se realiza
        antes de llamar a esta función.

    Parámetros:
        calificacion (int): Nota a validar.

    Retorna:
        bool: True si la nota está entre 1 y 10 inclusive; False si no.

    Ejemplo:
        validar_calificacion(7) -> True; validar_calificacion(11) -> False
    """
    return validar_rango(calificacion, 1, 10)


def es_letra(caracter: str) -> bool:
    """
    Verifica si un caracter es una letra (incluye acentos, ñ y ü).

    Lógica:
        Comprueba los rangos de letras minúsculas y mayúsculas. También acepta los
        caracteres incluidos en LETRAS_ESPECIALES mediante in. Devuelve el resultado
        booleano de las condiciones unidas por or.

    Parámetros:
        caracter (str): Un único caracter.

    Retorna:
        bool: True si es una letra mayúscula o minúscula; False si no.

    Ejemplo:
        es_letra("Ñ") -> True; es_letra("3") -> False
    """
    es_minuscula = caracter >= "a" and caracter <= "z"
    es_mayuscula = caracter >= "A" and caracter <= "Z"
    return es_minuscula or es_mayuscula or caracter in LETRAS_ESPECIALES


def validar_nombre(nombre: str) -> bool:
    """
    Verifica que un nombre sea válido.

    Un nombre es válido si tiene al menos 2 caracteres, está formado solo
    por letras y espacios, y contiene al menos una letra.

    Lógica:
        Rechaza textos de menos de dos caracteres. Recorre el nombre y marca tiene_letra
        cuando encuentra una letra. Si encuentra un carácter que no es letra ni espacio
        devuelve False. Al final devuelve tiene_letra para rechazar nombres compuestos solo
        por espacios.

    Parámetros:
        nombre (str): Nombre del estudiante.

    Retorna:
        bool: True si el nombre es válido; False en caso contrario.

    Ejemplo:
        validar_nombre("Ana Gómez") -> True; validar_nombre("Ana 2") -> False
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

    Lógica:
        Compara el género con F, M y X mediante or. Basta que una comparación sea verdadera.
        La conversión de minúsculas se hace en otra función.

    Parámetros:
        genero (str): Género del estudiante.

    Retorna:
        bool: True si el género es 'F', 'M' o 'X'; False en caso contrario.

    Ejemplo:
        validar_genero("F") -> True; validar_genero("f") -> False
    """
    return genero == "F" or genero == "M" or genero == "X"


def validar_legajo(legajo: int, legajos: list, cantidad_cargados: int) -> bool:
    """
    Verifica que un legajo sea un entero de cinco cifras y que no esté repetido.

    Un número de cinco cifras está entre 10000 y 99999. Además se revisan
    los legajos ya cargados (de la posición 0 hasta cantidad_cargados - 1)
    para que no haya dos estudiantes con el mismo legajo.

    Lógica:
        Primero verifica el rango 10000 a 99999. Después recorre solo las posiciones ya
        cargadas y compara los legajos. Devuelve False ante un duplicado y True si supera
        ambas comprobaciones.

    Parámetros:
        legajo (int): Legajo a validar.
        legajos (list): Lista de legajos del programa.
        cantidad_cargados (int): Cuántos legajos de la lista ya están cargados.

    Retorna:
        bool: True si el legajo tiene cinco cifras y no está repetido;
        False en caso contrario.
    """
    if not validar_rango(legajo, 10000, 99999):
        return False
    for i in range(cantidad_cargados):
        if legajos[i] == legajo:
            return False
    return True


def pedir_entero(mensaje: str, minimo: int, maximo: int) -> int:
    """
    Pide un número entero por consola hasta que sea válido y esté en rango.

    Lógica:
        Lee texto con input. Mientras no sea numérico o esté fuera del rango, muestra un
        error y vuelve a pedirlo. or realiza cortocircuito: si el texto no es numérico, no
        se ejecuta int(texto). Finalmente devuelve el entero válido.

    Parámetros:
        mensaje (str): Texto que se muestra al pedir el dato.
        minimo (int): Valor mínimo aceptado.
        maximo (int): Valor máximo aceptado.

    Retorna:
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

    Lógica:
        Lee texto y repite con while hasta que tenga solo dígitos y la nota esté entre 1 y
        10. El cortocircuito de or evita convertir texto inválido. Devuelve int(texto).

    Parámetros:
        mensaje (str): Texto que se muestra al pedir la nota.

    Retorna:
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

    Lógica:
        Pide el nombre con input y usa while para repetir mientras validar_nombre devuelva
        False. No se usa for porque no se sabe cuántos intentos serán necesarios. Devuelve
        el texto válido.

    Parámetros:
        mensaje (str): Texto que se muestra al pedir el nombre.

    Retorna:
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

    Lógica:
        Compara el texto con f, m y x y devuelve la mayúscula correspondiente. Si no
        coincide devuelve el texto original; la validación posterior decide si es aceptable.

    Parámetros:
        texto (str): Género ingresado por el usuario.

    Retorna:
        str: El género en mayúscula, o el texto original si no corresponde.

    Ejemplo:
        convertir_genero("f") -> "F"
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

    Lógica:
        Lee el texto y llama a convertir_genero. Mientras validar_genero sea False, informa
        el error y vuelve a leer y convertir. Devuelve el género válido en mayúscula.

    Parámetros:
        mensaje (str): Texto que se muestra al pedir el género.

    Retorna:
        str: 'F', 'M' o 'X'.
    """
    genero = convertir_genero(input(mensaje))
    while not validar_genero(genero):
        print("  Error: el género debe ser F, M o X.")
        genero = convertir_genero(input(mensaje))
    return genero


def pedir_legajo(mensaje: str, legajos: list, cantidad_cargados: int) -> int:
    """
    Pide un legajo hasta que sea un entero de cinco cifras no repetido.

    Lógica:
        Lee el texto y repite mientras no sea numérico o validar_legajo lo rechace. or evita
        convertir texto inválido. La validación comprueba cinco cifras y duplicados entre
        los registros ya cargados. Devuelve el entero válido.

    Parámetros:
        mensaje (str): Texto que se muestra al pedir el legajo.
        legajos (list): Lista de legajos del programa.
        cantidad_cargados (int): Cuántos legajos ya están cargados.

    Retorna:
        int: El legajo ingresado, ya validado.
    """
    texto = input(mensaje)
    while not es_numero_entero(texto) or not validar_legajo(int(texto), legajos, cantidad_cargados):
        print("  Error: el legajo debe ser un número de 5 cifras y no puede repetirse.")
        texto = input(mensaje)
    return int(texto)
