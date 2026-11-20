"""
Módulo funciones.

Biblioteca propia con las funciones del TPI 3: listas de diccionarios y archivos.

Los estudiantes se guardan en una lista donde cada elemento es un
diccionario con estas claves:
    "legajo"   -> int de 5 cifras
    "nombre"   -> str
    "genero"   -> 'F', 'M' o 'X'
    "notas"    -> lista de 5 calificaciones enteras entre 1 y 10
    "promedio" -> float (se calcula mediante la opción de promedios)

Como no hay una lista de materias, la nota de la posición j de la lista
"notas" corresponde a la materia MAT_(j + 1).

"""

import csv
import json


from validaciones import pedir_entero, pedir_calificacion, pedir_nombre, pedir_genero, pedir_legajo
from datos_prueba import ESTUDIANTES_PRUEBA

MAXIMO_ESTUDIANTES = 1000
CANTIDAD_MATERIAS = 5


# ---------------------------------------------------------------------------
# Menú
# ---------------------------------------------------------------------------

def crear_estudiante(legajo: int, nombre: str, genero: str, notas: list) -> dict:
    """
    Crea el diccionario de un estudiante con todas sus claves.

    El promedio arranca en None porque todavía no fue calculado.

    Args:
        legajo (int): Legajo de 5 cifras.
        nombre (str): Nombre del estudiante.
        genero (str): 'F', 'M' o 'X'.
        notas (list): Lista de 5 calificaciones entre 1 y 10.

    Returns:
        dict: Diccionario con las claves legajo, nombre, genero, notas y promedio.
    """
    return {
        "legajo": legajo,
        "nombre": nombre,
        "genero": genero,
        "notas": notas,
        "promedio": None,
    }


def cargar_estudiante_manual(estudiantes: list, indice: int) -> dict:
    """
    Pide por consola todos los datos de un estudiante, validando cada uno,
    y devuelve el diccionario armado.

    Args:
        estudiantes (list): Lista de estudiantes (se usa para verificar que
            el legajo no esté repetido entre los ya cargados).
        indice (int): Posición del estudiante que se está cargando
            (también es la cantidad de estudiantes ya cargados).

    Returns:
        dict: Diccionario del estudiante cargado.
    """
    print(f"\n--- Estudiante {indice + 1} ---")
    legajo = pedir_legajo("Legajo (5 cifras): ", estudiantes, indice)
    nombre = pedir_nombre("Nombre: ")
    genero = pedir_genero("Género (F/M/X): ")
    notas = [0] * CANTIDAD_MATERIAS
    for j in range(CANTIDAD_MATERIAS):
        notas[j] = pedir_calificacion(f"Nota MAT_{j + 1}: ")
    return crear_estudiante(legajo, nombre, genero, notas)


def cargar_datos_manual() -> list:
    """
    Carga manual: pide la cantidad de estudiantes (1 a 1000) y después los
    datos de cada uno.

    La lista se crea con el tamaño elegido y se completa por posición, sin
    usar append.

    Returns:
        list: Lista de diccionarios con los estudiantes cargados.
    """
    cantidad = pedir_entero(f"¿Cuántos estudiantes desea cargar? (1 a {MAXIMO_ESTUDIANTES}): ",
                            1, MAXIMO_ESTUDIANTES)
    estudiantes = [None] * cantidad
    for i in range(cantidad):
        estudiantes[i] = cargar_estudiante_manual(estudiantes, i)
    return estudiantes


def cargar_datos_prueba() -> list:
    """
    Carga los 1000 estudiantes hardcodeados del módulo datos_prueba.

    Arma un diccionario nuevo para cada estudiante (con la clave promedio
    en None) y copia también la lista de notas, para no modificar los datos
    originales del módulo.

    Returns:
        list: Lista de diccionarios con los estudiantes de prueba.
    """
    cantidad = len(ESTUDIANTES_PRUEBA)
    estudiantes = [None] * cantidad
    for i in range(cantidad):
        original = ESTUDIANTES_PRUEBA[i]
        notas = [0] * CANTIDAD_MATERIAS
        for j in range(CANTIDAD_MATERIAS):
            notas[j] = original["notas"][j]
        estudiantes[i] = crear_estudiante(original["legajo"], original["nombre"],
                                          original["genero"], notas)
    return estudiantes


def opcion_cargar_datos() -> list:
    """
    Opción 1 del menú: carga los datos en la lista de diccionarios.

    Permite elegir entre la carga manual (validando cada dato) o la carga
    de los 1000 estudiantes de prueba hardcodeados.

    Returns:
        list: Lista de diccionarios con los estudiantes cargados.
    """
    print("\n1 - Carga manual")
    print("2 - Cargar datos de prueba (1000 estudiantes)")
    tipo_carga = pedir_entero("Elija el tipo de carga: ", 1, 2)

    if tipo_carga == 1:
        estudiantes = cargar_datos_manual()
    else:
        estudiantes = cargar_datos_prueba()

    print(f"\nSe cargaron {len(estudiantes)} estudiantes correctamente.")
    return estudiantes


# ---------------------------------------------------------------------------
# Opción 2: mostrar datos
# ---------------------------------------------------------------------------

def mostrar_encabezado() -> None:
    """
    Muestra el encabezado de la tabla, con cada clave al lado de la otra:
    LEGAJO | NOMBRE | GENERO | N1 | N2 | N3 | N4 | N5 | PROM

    Returns:
        None
    """
    encabezado = f"{'LEGAJO':<6} | {'NOMBRE':<22} | {'GENERO':<6}"
    for j in range(CANTIDAD_MATERIAS):
        encabezado += f" | {'N' + str(j + 1):>2}"
    encabezado += f" | {'PROM':>5}"
    print(encabezado)
    print("-" * len(encabezado))


def mostrar_estudiante(estudiante: dict) -> None:
    """
    Muestra en una línea todos los datos de UN estudiante (mostrar uno):
    legajo, nombre, género, las 5 notas y el promedio.

    Si el promedio todavía no se calculó (vale None), muestra un guion.

    Args:
        estudiante (dict): Diccionario del estudiante.

    Returns:
        None
    """
    linea = f"{estudiante['legajo']:<6} | {estudiante['nombre']:<22} | {estudiante['genero']:<6}"
    for nota in estudiante["notas"]:
        linea += f" | {nota:>2}"
    if estudiante["promedio"] is None:
        linea += f" | {'-':>5}"
    else:
        linea += f" | {estudiante['promedio']:>5.2f}"
    print(linea)


def mostrar_estudiantes(estudiantes: list) -> None:
    """
    Muestra TODOS los estudiantes (mostrar todos): imprime el encabezado y
    recorre la lista con un for, llamando a mostrar_estudiante() para cada
    diccionario (Nota 6 del TP).

    Args:
        estudiantes (list): Lista de diccionarios de estudiantes.

    Returns:
        None
    """
    mostrar_encabezado()
    for estudiante in estudiantes:
        mostrar_estudiante(estudiante)


def opcion_mostrar_datos(estudiantes: list) -> None:
    """
    Opción 2 del menú: muestra la lista de diccionarios completa.

    Args:
        estudiantes (list): Lista de diccionarios de estudiantes.

    Returns:
        None
    """
    print("\n--- DATOS DE LOS ESTUDIANTES ---\n")
    mostrar_estudiantes(estudiantes)


# ---------------------------------------------------------------------------
# Opción 3: promedios
# ---------------------------------------------------------------------------

def calcular_promedio(notas: list) -> float:
    """
    Calcula el promedio de una lista de calificaciones.

    Suma todas las notas recorriendo la lista y divide por la cantidad.

    Args:
        notas (list): Lista de calificaciones del estudiante.

    Returns:
        float: Promedio de las notas. Si la lista está vacía devuelve 0.
    """
    if len(notas) == 0:
        return 0
    suma = 0
    for nota in notas:
        suma += nota
    return suma / len(notas)


def opcion_calcular_promedios(estudiantes: list) -> bool:
    """
    Opción 3 del menú: calcula el promedio de cada estudiante y lo guarda
    en la clave "promedio" de su diccionario.

    Args:
        estudiantes (list): Lista de diccionarios (se modifica).

    Returns:
        bool: True cuando los promedios quedaron calculados.
    """
    for estudiante in estudiantes:
        estudiante["promedio"] = calcular_promedio(estudiante["notas"])
    print("\nPromedios calculados correctamente.")
    return True


# ---------------------------------------------------------------------------
# Opción 4: ordenamiento
# ---------------------------------------------------------------------------

def ordenar_por_promedio(estudiantes: list, criterio: str) -> None:
    """
    Ordena la lista de estudiantes por la clave "promedio" usando el
    método burbuja.

    Como cada estudiante es un diccionario con todos sus datos, al
    intercambiar dos posiciones de la lista se mueve el estudiante entero.

    Args:
        estudiantes (list): Lista de diccionarios (se modifica).
        criterio (str): "ASC" para ordenar de menor a mayor,
            "DESC" para ordenar de mayor a menor.

    Returns:
        None
    """
    n = len(estudiantes)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            actual = estudiantes[j]["promedio"]
            siguiente = estudiantes[j + 1]["promedio"]
            if criterio == "ASC":
                hay_que_intercambiar = actual > siguiente
            else:
                hay_que_intercambiar = actual < siguiente

            if hay_que_intercambiar:
                auxiliar = estudiantes[j]
                estudiantes[j] = estudiantes[j + 1]
                estudiantes[j + 1] = auxiliar


def opcion_ordenar_y_mostrar(estudiantes: list) -> None:
    """
    Opción 4 del menú: pregunta si se ordena de forma ascendente o
    descendente, ordena a los estudiantes por promedio y los muestra.

    Args:
        estudiantes (list): Lista de diccionarios (se modifica).

    Returns:
        None
    """
    print("\n1 - Ascendente (ASC)")
    print("2 - Descendente (DESC)")
    eleccion = pedir_entero("Elija el orden: ", 1, 2)
    if eleccion == 1:
        criterio = "ASC"
    else:
        criterio = "DESC"

    ordenar_por_promedio(estudiantes, criterio)
    print(f"\n--- ESTUDIANTES ORDENADOS POR PROMEDIO ({criterio}) ---\n")
    mostrar_estudiantes(estudiantes)


# ---------------------------------------------------------------------------
# Opción 5: materias con mayor promedio
# ---------------------------------------------------------------------------

def calcular_promedio_materia(estudiantes: list, indice_materia: int) -> float:
    """
    Calcula el promedio general de una materia: suma la nota de esa
    materia de todos los estudiantes y la divide por la cantidad.

    Args:
        estudiantes (list): Lista de diccionarios de estudiantes.
        indice_materia (int): Posición de la materia en la lista "notas" (0 a 4).

    Returns:
        float: Promedio general de la materia.
    """
    suma = 0
    for estudiante in estudiantes:
        suma += estudiante["notas"][indice_materia]
    return suma / len(estudiantes)


def calcular_promedios_materias(estudiantes: list) -> list:
    """
    Calcula el promedio general de cada una de las 5 materias.

    Args:
        estudiantes (list): Lista de diccionarios de estudiantes.

    Returns:
        list: Lista de 5 elementos; en la posición j está el promedio de MAT_(j + 1).
    """
    promedios_materias = [0] * CANTIDAD_MATERIAS
    for j in range(CANTIDAD_MATERIAS):
        promedios_materias[j] = calcular_promedio_materia(estudiantes, j)
    return promedios_materias


def buscar_maximo(lista: list) -> float:
    """
    Busca el valor más grande de una lista (sin usar max()).

    Args:
        lista (list): Lista de números (no vacía).

    Returns:
        float: El mayor valor de la lista.
    """
    maximo = lista[0]
    for valor in lista:
        if valor > maximo:
            maximo = valor
    return maximo


def mostrar_materia(indice_materia: int, promedio: float) -> None:
    """
    Muestra UNA materia con su promedio (mostrar uno).

    El nombre se arma como MAT_ más el índice de la materia más uno.

    Args:
        indice_materia (int): Posición de la materia (0 a 4).
        promedio (float): Promedio general de la materia.

    Returns:
        None
    """
    print(f"MAT_{indice_materia + 1}  -  Promedio: {promedio:.2f}")


def mostrar_materias_mayor_promedio(promedios_materias: list) -> None:
    """
    Recorre TODAS las materias (mostrar todos) y llama a mostrar_materia()
    para cada una que tenga el mayor promedio general. Si hay empate, se
    muestran todas las empatadas.

    Args:
        promedios_materias (list): Promedio general de cada materia.

    Returns:
        None
    """
    maximo = buscar_maximo(promedios_materias)
    for j in range(len(promedios_materias)):
        if promedios_materias[j] == maximo:
            mostrar_materia(j, promedios_materias[j])


def opcion_materias_mayor_promedio(estudiantes: list) -> None:
    """
    Opción 5 del menú: muestra la/s materia/s con mayor promedio general.

    Args:
        estudiantes (list): Lista de diccionarios de estudiantes.

    Returns:
        None
    """
    promedios_materias = calcular_promedios_materias(estudiantes)
    print("\n--- MATERIA/S CON MAYOR PROMEDIO GENERAL ---\n")
    mostrar_materias_mayor_promedio(promedios_materias)


# ---------------------------------------------------------------------------
# Opción 6: búsqueda por legajo
# ---------------------------------------------------------------------------

def buscar_por_legajo(estudiantes: list, legajo_buscado: int) -> int:
    """
    Busca un estudiante por legajo recorriendo la lista (búsqueda secuencial).

    Args:
        estudiantes (list): Lista de diccionarios de estudiantes.
        legajo_buscado (int): Legajo que se quiere encontrar.

    Returns:
        int: Posición del estudiante en la lista si se encuentra; -1 si no existe.
    """
    for i in range(len(estudiantes)):
        if estudiantes[i]["legajo"] == legajo_buscado:
            return i
    return -1


def opcion_buscar_estudiante(estudiantes: list) -> None:
    """
    Opción 6 del menú: pide un legajo, lo busca y muestra todos los datos
    del estudiante, incluido el promedio calculado en la opción 3.

    Args:
        estudiantes (list): Lista de diccionarios de estudiantes.

    Returns:
        None
    """
    legajo = pedir_entero("\nIngrese el legajo a buscar: ", 10000, 99999)
    posicion = buscar_por_legajo(estudiantes, legajo)
    if posicion == -1:
        print(f"No se encontró ningún estudiante con legajo {legajo}.")
    else:
        print()
        mostrar_encabezado()
        mostrar_estudiante(estudiantes[posicion])


# ---------------------------------------------------------------------------
# Opción 7: repeticiones de cada nota en una materia
# ---------------------------------------------------------------------------

def contar_calificaciones(estudiantes: list, numero_materia: int) -> list:
    """
    Cuenta cuántas veces se repite cada calificación (1 a 10) en una materia.

    Args:
        estudiantes (list): Lista de diccionarios de estudiantes.
        numero_materia (int): Número de materia (índice + 1), entre 1 y 5.

    Returns:
        list: Lista de 10 elementos. En el índice 0 está la cantidad de
        veces que aparece la nota 1, en el índice 1 la nota 2, y así hasta
        el índice 9, que corresponde a la nota 10.
    """
    contadores = [0] * 10
    indice_materia = numero_materia - 1
    for estudiante in estudiantes:
        nota = estudiante["notas"][indice_materia]
        contadores[nota - 1] += 1
    return contadores


def mostrar_repeticion(nota: int, cantidad: int) -> None:
    """
    Muestra cuántas veces aparece UNA nota (mostrar uno).

    Args:
        nota (int): Calificación (1 a 10).
        cantidad (int): Cantidad de veces que aparece.

    Returns:
        None
    """
    print(f"Nota {nota:>2}: {cantidad:>4} vez/veces")


def mostrar_repeticiones(contadores: list) -> None:
    """
    Recorre los 10 contadores (mostrar todos) y llama a mostrar_repeticion()
    para cada nota.

    Args:
        contadores (list): Lista de 10 contadores devuelta por
            contar_calificaciones().

    Returns:
        None
    """
    for i in range(len(contadores)):
        mostrar_repeticion(i + 1, contadores[i])


def opcion_contar_calificaciones(estudiantes: list) -> None:
    """
    Opción 7 del menú: pide un número de materia y muestra cuántas veces se
    repite cada calificación en esa materia.

    Args:
        estudiantes (list): Lista de diccionarios de estudiantes.

    Returns:
        None
    """
    numero_materia = pedir_entero(f"\nIngrese el número de materia (1 a {CANTIDAD_MATERIAS}): ",
                                  1, CANTIDAD_MATERIAS)
    contadores = contar_calificaciones(estudiantes, numero_materia)
    print(f"\n--- REPETICIONES DE NOTAS EN MAT_{numero_materia} ---\n")
    mostrar_repeticiones(contadores)


def validar_fila_csv(fila):
    """Convierte y valida los nueve campos de un registro CSV."""
    from validaciones import validar_legajo, validar_nombre, validar_genero, validar_calificacion
    if len(fila) != 9:
        return None
    try:
        legajo = int(fila[0])
        nombre = fila[1].strip()
        genero = fila[2].strip().upper()
        notas = [int(fila[i]) for i in range(3, 8)]
        promedio = float(fila[8])
    except ValueError:
        return None
    if not validar_legajo(legajo, [], 0) or not validar_nombre(nombre) or not validar_genero(genero):
        return None
    for nota in notas:
        if not validar_calificacion(nota):
            return None
    if not (0 <= promedio <= 10):
        return None
    return {"legajo":legajo,"nombre":nombre,"genero":genero,"notas":notas,"promedio":promedio}


def cargar_desde_csv(nombre_archivo):
    """Lee estudiantes válidos desde CSV, sin legajos duplicados."""
    estudiantes = []
    legajos = set()
    archivo_valido = True
    try:
        with open(nombre_archivo, 'r', encoding='utf-8-sig', newline='') as archivo:
            lector = csv.reader(archivo)
            for numero, fila in enumerate(lector, 1):
                estudiante = validar_fila_csv(fila)
                if estudiante is None:
                    print('Fila', numero, 'inválida.')
                    archivo_valido = False
                elif estudiante['legajo'] in legajos:
                    print('Fila', numero, 'con legajo repetido.')
                    archivo_valido = False
                elif len(estudiantes) < MAXIMO_ESTUDIANTES:
                    estudiantes.append(estudiante)
                    legajos.add(estudiante['legajo'])
                else:
                    print('El CSV supera el máximo de estudiantes.')
                    archivo_valido = False
                    break
    except (OSError, UnicodeError) as error:
        print('No se pudo leer el CSV:', error)
        return []
    if not archivo_valido:
        print('No se cargó el CSV porque contiene datos inválidos.')
        return []
    return estudiantes


def opcion_cargar_csv():
    """Solicita la ruta del CSV y devuelve los estudiantes válidos cargados."""
    nombre = input('Nombre del archivo CSV: ').strip()
    estudiantes = cargar_desde_csv(nombre)
    print('Estudiantes cargados:', len(estudiantes))
    return estudiantes


def opcion_guardar_json(estudiantes):
    """Guarda la lista de estudiantes en un archivo JSON solicitado por consola."""
    nombre = input('Nombre del archivo JSON de salida: ').strip()
    if not nombre:
        print('Nombre de archivo inválido.')
        return
    try:
        with open(nombre, 'w', encoding='utf-8') as archivo:
            json.dump(estudiantes, archivo, ensure_ascii=False, indent=4)
        print('Datos guardados en', nombre)
    except OSError as error:
        print('No se pudo guardar el archivo:', error)


def mostrar_menu():
    """Muestra las opciones disponibles."""
    print("\n=== SISTEMA DE ESTUDIANTES ===")
    print(1, "- Cargar desde archivo CSV")
    print(2, "- Cargar datos manualmente o de prueba")
    print(3, "- Mostrar todos los datos")
    print(4, "- Calcular promedios")
    print(5, "- Ordenar por promedio")
    print(6, "- Mostrar materias con mayor promedio")
    print(7, "- Buscar estudiante por legajo")
    print(8, "- Contar calificaciones por materia")
    print(9, "- Guardar datos en JSON")
    print(10, "- Salir")


def opcion_salir() -> None:
    """Muestra el mensaje de salida del sistema."""
    print("\nSaliendo del programa.")
