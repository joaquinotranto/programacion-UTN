"""
Módulo funciones.

Biblioteca propia con las funciones del TP Listas y Matrices.

Se trabaja con listas paralelas: la fila i de la matriz de calificaciones,
y la posición i de las listas de nombres, géneros, legajos y promedios
corresponden siempre al mismo estudiante.

La matriz tiene 30 filas (estudiantes) por 5 columnas (materias). Como no
hay una lista de materias, la columna j se llama MATERIA_(j + 1).

"""

from validaciones import pedir_entero, pedir_calificacion, pedir_nombre, pedir_genero, pedir_legajo
from datos_prueba import NOMBRES_PRUEBA, GENEROS_PRUEBA, LEGAJOS_PRUEBA, CALIFICACIONES_PRUEBA

CANTIDAD_ESTUDIANTES = 30
CANTIDAD_MATERIAS = 5


# ---------------------------------------------------------------------------
# Inicialización y menú
# ---------------------------------------------------------------------------

def crear_matriz(filas: int, columnas: int, valor_inicial: int) -> list:
    """
    Crea e inicializa una matriz (lista de listas) con un mismo valor.

    Cada fila se crea por separado para que las filas no compartan la
    misma lista en memoria.

    Args:
        filas (int): Cantidad de filas.
        columnas (int): Cantidad de columnas.
        valor_inicial (int): Valor con el que se llena cada celda.

    Returns:
        list: Matriz de filas x columnas con todas las celdas en valor_inicial.
    """
    matriz = [None] * filas
    for i in range(filas):
        matriz[i] = [valor_inicial] * columnas
    return matriz


def mostrar_menu() -> None:
    """
    Muestra por consola el menú de opciones del programa.

    Returns:
        None
    """
    print()
    print("=" * 50)
    print("        SISTEMA DE CALIFICACIONES")
    print("=" * 50)
    print("1 - Cargar datos")
    print("2 - Mostrar todos los datos")
    print("3 - Calcular promedio de cada estudiante")
    print("4 - Ordenar y mostrar estudiantes por promedio (DESC)")
    print("5 - Mostrar materia/s con mayor promedio general")
    print("6 - Buscar estudiante por legajo")
    print("7 - Contar repeticiones de cada nota en una materia")
    print("8 - Salir")
    print("=" * 50)


# ---------------------------------------------------------------------------
# Opción 1: carga de datos
# ---------------------------------------------------------------------------

def cargar_estudiante_manual(matriz: list, nombres: list, generos: list, legajos: list, indice: int) -> None:
    """
    Pide por consola todos los datos de un estudiante y los guarda en la
    posición indicada de la matriz y de las listas paralelas.

    Cada dato se valida con su función de validación correspondiente
    (módulo validaciones) antes de guardarse.

    Args:
        matriz (list): Matriz de calificaciones (se modifica).
        nombres (list): Lista de nombres (se modifica).
        generos (list): Lista de géneros (se modifica).
        legajos (list): Lista de legajos (se modifica).
        indice (int): Posición (fila) del estudiante a cargar.

    Returns:
        None
    """
    print(f"\n--- Estudiante {indice + 1} de {CANTIDAD_ESTUDIANTES} ---")
    legajos[indice] = pedir_legajo("Legajo (5 cifras): ", legajos, indice)
    nombres[indice] = pedir_nombre("Nombre: ")
    generos[indice] = pedir_genero("Género (F/M/X): ")
    for j in range(CANTIDAD_MATERIAS):
        matriz[indice][j] = pedir_calificacion(f"Nota MATERIA_{j + 1}: ")


def cargar_datos_prueba(matriz: list, nombres: list, generos: list, legajos: list) -> None:
    """
    Copia los datos hardcodeados del módulo datos_prueba a la matriz y a
    las listas del programa, elemento por elemento.

    Args:
        matriz (list): Matriz de calificaciones (se modifica).
        nombres (list): Lista de nombres (se modifica).
        generos (list): Lista de géneros (se modifica).
        legajos (list): Lista de legajos (se modifica).

    Returns:
        None
    """
    for i in range(CANTIDAD_ESTUDIANTES):
        nombres[i] = NOMBRES_PRUEBA[i]
        generos[i] = GENEROS_PRUEBA[i]
        legajos[i] = LEGAJOS_PRUEBA[i]
        for j in range(CANTIDAD_MATERIAS):
            matriz[i][j] = CALIFICACIONES_PRUEBA[i][j]


def opcion_cargar_datos(matriz: list, nombres: list, generos: list, legajos: list) -> bool:
    """
    Opción 1 del menú: carga los datos en la matriz y en las listas.

    Permite elegir entre la carga manual de los 30 estudiantes (con
    validación de cada dato) o la carga de datos de prueba hardcodeados.

    Args:
        matriz (list): Matriz de calificaciones (se modifica).
        nombres (list): Lista de nombres (se modifica).
        generos (list): Lista de géneros (se modifica).
        legajos (list): Lista de legajos (se modifica).

    Returns:
        bool: True cuando la carga terminó (los datos quedan cargados).
    """
    print("\n1 - Carga manual")
    print("2 - Cargar datos de prueba")
    tipo_carga = pedir_entero("Elija el tipo de carga: ", 1, 2)

    if tipo_carga == 1:
        for i in range(CANTIDAD_ESTUDIANTES):
            cargar_estudiante_manual(matriz, nombres, generos, legajos, i)
    else:
        cargar_datos_prueba(matriz, nombres, generos, legajos)

    print("\nDatos cargados correctamente.")
    return True


# ---------------------------------------------------------------------------
# Opción 2: mostrar datos
# ---------------------------------------------------------------------------

def mostrar_encabezado(con_promedio: bool) -> None:
    """
    Muestra la fila de títulos de la tabla de estudiantes.

    Args:
        con_promedio (bool): True para agregar la columna PROMEDIO.

    Returns:
        None
    """
    encabezado = f"{'LEGAJO':<8}{'NOMBRE':<18}{'GÉN.':<6}"
    for j in range(CANTIDAD_MATERIAS):
        encabezado += f"{'MAT_' + str(j + 1):>7}"
    if con_promedio:
        encabezado += f"{'PROMEDIO':>10}"
    print(encabezado)
    print("-" * len(encabezado))


def mostrar_estudiante(matriz: list, nombres: list, generos: list, legajos: list,
                       promedios: list, indice: int) -> None:
    """
    Muestra en una línea todos los datos de UN estudiante (mostrar uno).

    Muestra legajo, nombre, género y las 5 calificaciones. Si se recibe
    la lista de promedios (no es None), también muestra el promedio.

    Args:
        matriz (list): Matriz de calificaciones.
        nombres (list): Lista de nombres.
        generos (list): Lista de géneros.
        legajos (list): Lista de legajos.
        promedios (list): Lista de promedios, o None si no se quiere mostrar.
        indice (int): Posición (fila) del estudiante a mostrar.

    Returns:
        None
    """
    linea = f"{legajos[indice]:<8}{nombres[indice]:<18}{generos[indice]:<6}"
    for j in range(CANTIDAD_MATERIAS):
        linea += f"{matriz[indice][j]:>7}"
    if promedios is not None:
        linea += f"{promedios[indice]:>10.2f}"
    print(linea)


def mostrar_estudiantes(matriz: list, nombres: list, generos: list, legajos: list,
                        promedios: list) -> None:
    """
    Muestra los datos de TODOS los estudiantes (mostrar todos).

    Recorre las filas de la matriz y llama a mostrar_estudiante() para
    cada una (Nota 6 del TP).

    Args:
        matriz (list): Matriz de calificaciones.
        nombres (list): Lista de nombres.
        generos (list): Lista de géneros.
        legajos (list): Lista de legajos.
        promedios (list): Lista de promedios, o None si no se quiere mostrar.

    Returns:
        None
    """
    mostrar_encabezado(promedios is not None)
    for i in range(CANTIDAD_ESTUDIANTES):
        mostrar_estudiante(matriz, nombres, generos, legajos, promedios, i)


def opcion_mostrar_datos(matriz: list, nombres: list, generos: list, legajos: list) -> None:
    """
    Opción 2 del menú: muestra la matriz completa de calificaciones junto
    con las listas de legajo, nombre y género.

    Args:
        matriz (list): Matriz de calificaciones.
        nombres (list): Lista de nombres.
        generos (list): Lista de géneros.
        legajos (list): Lista de legajos.

    Returns:
        None
    """
    print("\n--- DATOS DE LOS ESTUDIANTES ---\n")
    mostrar_estudiantes(matriz, nombres, generos, legajos, None)


# ---------------------------------------------------------------------------
# Opción 3: promedios
# ---------------------------------------------------------------------------

def calcular_promedio(notas: list) -> float:
    """
    Calcula el promedio de una lista de calificaciones.

    Suma todas las notas recorriendo la lista y divide por la cantidad.

    Args:
        notas (list): Lista de calificaciones (una fila de la matriz).

    Returns:
        float: Promedio de las notas. Si la lista está vacía devuelve 0.
    """
    if len(notas) == 0:
        return 0
    suma = 0
    for nota in notas:
        suma += nota
    return suma / len(notas)


def opcion_calcular_promedios(matriz: list, promedios: list) -> bool:
    """
    Opción 3 del menú: calcula el promedio de cada estudiante y lo guarda
    en la lista de promedios (paralela a la matriz).

    Args:
        matriz (list): Matriz de calificaciones.
        promedios (list): Lista donde se guardan los promedios (se modifica).

    Returns:
        bool: True cuando los promedios quedaron calculados.
    """
    for i in range(CANTIDAD_ESTUDIANTES):
        promedios[i] = calcular_promedio(matriz[i])
    print("\nPromedios calculados correctamente.")
    return True


# ---------------------------------------------------------------------------
# Opción 4: ordenamiento
# ---------------------------------------------------------------------------

def intercambiar(lista: list, i: int, j: int) -> None:
    """
    Intercambia los elementos de las posiciones i y j de una lista.

    Si la lista es la matriz, intercambia filas completas.

    Args:
        lista (list): Lista (o matriz) a modificar.
        i (int): Primera posición.
        j (int): Segunda posición.

    Returns:
        None
    """
    auxiliar = lista[i]
    lista[i] = lista[j]
    lista[j] = auxiliar


def ordenar_por_promedio(matriz: list, nombres: list, generos: list, legajos: list,
                         promedios: list, criterio: str) -> None:
    """
    Ordena a los estudiantes por promedio usando el método burbuja.

    Cuando dos estudiantes tienen que cambiar de lugar, se intercambian en
    TODAS las listas paralelas (y la fila completa de la matriz), así los
    datos de cada estudiante quedan siempre juntos.

    Args:
        matriz (list): Matriz de calificaciones (se modifica).
        nombres (list): Lista de nombres (se modifica).
        generos (list): Lista de géneros (se modifica).
        legajos (list): Lista de legajos (se modifica).
        promedios (list): Lista de promedios (se modifica).
        criterio (str): "ASC" para ordenar de menor a mayor,
            "DESC" para ordenar de mayor a menor.

    Returns:
        None
    """
    n = len(promedios)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if criterio == "ASC":
                hay_que_intercambiar = promedios[j] > promedios[j + 1]
            else:
                hay_que_intercambiar = promedios[j] < promedios[j + 1]

            if hay_que_intercambiar:
                intercambiar(promedios, j, j + 1)
                intercambiar(matriz, j, j + 1)
                intercambiar(nombres, j, j + 1)
                intercambiar(generos, j, j + 1)
                intercambiar(legajos, j, j + 1)


def opcion_ordenar_y_mostrar(matriz: list, nombres: list, generos: list, legajos: list,
                             promedios: list) -> None:
    """
    Opción 4 del menú: ordena a los estudiantes por promedio de manera
    descendente (DESC) y los muestra.

    Args:
        matriz (list): Matriz de calificaciones (se modifica).
        nombres (list): Lista de nombres (se modifica).
        generos (list): Lista de géneros (se modifica).
        legajos (list): Lista de legajos (se modifica).
        promedios (list): Lista de promedios (se modifica).

    Returns:
        None
    """
    ordenar_por_promedio(matriz, nombres, generos, legajos, promedios, "DESC")
    print("\n--- ESTUDIANTES ORDENADOS POR PROMEDIO (DESC) ---\n")
    mostrar_estudiantes(matriz, nombres, generos, legajos, promedios)


# ---------------------------------------------------------------------------
# Opción 5: materias con mayor promedio
# ---------------------------------------------------------------------------

def calcular_promedio_materia(matriz: list, columna: int) -> float:
    """
    Calcula el promedio general de una materia (una columna de la matriz).

    Args:
        matriz (list): Matriz de calificaciones.
        columna (int): Índice de la columna (0 a 4).

    Returns:
        float: Promedio de todas las notas de esa columna.
    """
    suma = 0
    for i in range(len(matriz)):
        suma += matriz[i][columna]
    return suma / len(matriz)


def calcular_promedios_materias(matriz: list) -> list:
    """
    Calcula el promedio general de cada materia.

    Args:
        matriz (list): Matriz de calificaciones.

    Returns:
        list: Lista de 5 elementos; en la posición j está el promedio de
        MATERIA_(j + 1).
    """
    promedios_materias = [0] * CANTIDAD_MATERIAS
    for j in range(CANTIDAD_MATERIAS):
        promedios_materias[j] = calcular_promedio_materia(matriz, j)
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


def mostrar_materia(columna: int, promedio: float) -> None:
    """
    Muestra UNA materia con su promedio (mostrar uno).

    El nombre se arma como MATERIA_ más el índice de la columna más uno.

    Args:
        columna (int): Índice de la columna de la materia.
        promedio (float): Promedio general de la materia.

    Returns:
        None
    """
    print(f"MATERIA_{columna + 1}  -  Promedio: {promedio:.2f}")


def mostrar_materias_mayor_promedio(promedios_materias: list) -> None:
    """
    Muestra TODAS las materias que tienen el mayor promedio general
    (mostrar todos). Si hay empate, se muestran todas las empatadas.

    Recorre los promedios y llama a mostrar_materia() para cada materia
    cuyo promedio es igual al máximo (Nota 6 del TP).

    Args:
        promedios_materias (list): Promedio de cada materia.

    Returns:
        None
    """
    maximo = buscar_maximo(promedios_materias)
    for j in range(len(promedios_materias)):
        if promedios_materias[j] == maximo:
            mostrar_materia(j, promedios_materias[j])


def opcion_materias_mayor_promedio(matriz: list) -> None:
    """
    Opción 5 del menú: muestra la/s materia/s con mayor promedio general.

    Args:
        matriz (list): Matriz de calificaciones.

    Returns:
        None
    """
    promedios_materias = calcular_promedios_materias(matriz)
    print("\n--- MATERIA/S CON MAYOR PROMEDIO GENERAL ---\n")
    mostrar_materias_mayor_promedio(promedios_materias)


# ---------------------------------------------------------------------------
# Opción 6: búsqueda por legajo
# ---------------------------------------------------------------------------

def buscar_por_legajo(legajos: list, legajo_buscado: int) -> int:
    """
    Busca un legajo en la lista de legajos (búsqueda secuencial).

    Args:
        legajos (list): Lista de legajos.
        legajo_buscado (int): Legajo que se quiere encontrar.

    Returns:
        int: Índice (fila) del estudiante si se encuentra; -1 si no existe.
    """
    for i in range(len(legajos)):
        if legajos[i] == legajo_buscado:
            return i
    return -1


def opcion_buscar_estudiante(matriz: list, nombres: list, generos: list, legajos: list,
                             promedios: list) -> None:
    """
    Opción 6 del menú: pide un legajo, lo busca y muestra todos los datos
    del estudiante, incluido el promedio calculado en la opción 3.

    Args:
        matriz (list): Matriz de calificaciones.
        nombres (list): Lista de nombres.
        generos (list): Lista de géneros.
        legajos (list): Lista de legajos.
        promedios (list): Lista de promedios.

    Returns:
        None
    """
    legajo = pedir_entero("\nIngrese el legajo a buscar: ", 10000, 99999)
    indice = buscar_por_legajo(legajos, legajo)
    if indice == -1:
        print(f"No se encontró ningún estudiante con legajo {legajo}.")
    else:
        print()
        mostrar_encabezado(True)
        mostrar_estudiante(matriz, nombres, generos, legajos, promedios, indice)


# ---------------------------------------------------------------------------
# Opción 7: repeticiones de cada nota en una materia
# ---------------------------------------------------------------------------

def contar_calificaciones(matriz: list, numero_materia: int) -> list:
    """
    Cuenta cuántas veces se repite cada calificación (1 a 10) en una materia.

    Args:
        matriz (list): Matriz de calificaciones.
        numero_materia (int): Número de materia (índice de columna + 1),
            entre 1 y 5.

    Returns:
        list: Lista de 10 elementos. En el índice 0 está la cantidad de
        veces que aparece la nota 1, en el índice 1 la nota 2, y así hasta
        el índice 9, que corresponde a la nota 10.
    """
    contadores = [0] * 10
    columna = numero_materia - 1
    for i in range(len(matriz)):
        nota = matriz[i][columna]
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
    print(f"Nota {nota:>2}: {cantidad:>2} vez/veces")


def mostrar_repeticiones(contadores: list) -> None:
    """
    Muestra cuántas veces aparece cada nota (mostrar todos), llamando a
    mostrar_repeticion() para cada una.

    Args:
        contadores (list): Lista de 10 contadores devuelta por
            contar_calificaciones().

    Returns:
        None
    """
    for i in range(len(contadores)):
        mostrar_repeticion(i + 1, contadores[i])


def opcion_contar_calificaciones(matriz: list) -> None:
    """
    Opción 7 del menú: pide un número de materia y muestra cuántas veces
    se repite cada calificación en esa materia.

    Args:
        matriz (list): Matriz de calificaciones.

    Returns:
        None
    """
    numero_materia = pedir_entero(f"\nIngrese el número de materia (1 a {CANTIDAD_MATERIAS}): ",
                                  1, CANTIDAD_MATERIAS)
    contadores = contar_calificaciones(matriz, numero_materia)
    print(f"\n--- REPETICIONES DE NOTAS EN MATERIA_{numero_materia} ---\n")
    mostrar_repeticiones(contadores)


def opcion_salir() -> None:
    """Muestra el mensaje de salida del sistema."""
    print("\nSaliendo del programa.")
