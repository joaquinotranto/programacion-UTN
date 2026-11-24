"""
Módulo funciones.

Biblioteca propia con las funciones del TPI 4: listas de diccionarios y archivos.

Los estudiantes se guardan en una lista donde cada elemento es un
diccionario con estas claves:
    "legajo"   -> int de 5 cifras
    "nombre"   -> str
    "genero"   -> 'F', 'M' o 'X'
    "notas"    -> lista de 5 calificaciones enteras entre 1 y 10
    "promedio" -> float (se calcula mediante la opción de promedios)

Como no hay una lista de materias, la nota de la posición j de la lista
"notas" corresponde a la materia MAT_(j + 1).

Funciones del módulo:
    crear_estudiante()
    cargar_estudiante_manual()
    cargar_datos_manual()
    cargar_datos_prueba()
    opcion_cargar_datos()
    mostrar_encabezado()
    mostrar_estudiante()
    mostrar_estudiantes()
    opcion_mostrar_datos()
    calcular_promedio()
    opcion_calcular_promedios()
    ordenar_por_promedio()
    opcion_ordenar_y_mostrar()
    calcular_promedio_materia()
    calcular_promedios_materias()
    buscar_maximo()
    mostrar_materia()
    mostrar_materias_mayor_promedio()
    opcion_materias_mayor_promedio()
    buscar_por_legajo()
    opcion_buscar_estudiante()
    contar_calificaciones()
    mostrar_repeticion()
    mostrar_repeticiones()
    opcion_contar_calificaciones()
    validar_fila_csv()
    cargar_desde_csv()
    opcion_cargar_csv()
    opcion_guardar_json()
    normalizar_estudiantes()
    opcion_normalizar()
    opcion_promedios_funcional()
    opcion_filtrar_desaprobados()
    mostrar_menu()
    opcion_salir()
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

    Lógica:
        Construye un diccionario con claves fijas para identificar cada dato. Guarda la
        lista de notas recibida y asigna None al promedio porque todavía no fue calculado.
        Devuelve el diccionario.

    Parámetros:
        legajo (int): Legajo de 5 cifras.
        nombre (str): Nombre del estudiante.
        genero (str): 'F', 'M' o 'X'.
        notas (list): Lista de 5 calificaciones entre 1 y 10.

    Retorna:
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

    Lógica:
        Pide legajo, nombre y género mediante las funciones de validación. El índice indica
        cuántos registros anteriores deben revisarse para evitar duplicados. Recorre las
        cinco materias con range; j + 1 sirve para mostrar números desde 1 aunque los
        índices comienzan en 0.
        Crea y devuelve el diccionario con crear_estudiante.

    Parámetros:
        estudiantes (list): Lista de estudiantes (se usa para verificar que
            el legajo no esté repetido entre los ya cargados).
        indice (int): Posición del estudiante que se está cargando
            (también es la cantidad de estudiantes ya cargados).

    Retorna:
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

    Lógica:
        Pide una cantidad válida entre 1 y el máximo. Reserva una lista con None y recorre
        sus posiciones. En cada vuelta guarda el diccionario devuelto por
        cargar_estudiante_manual. Devuelve la lista completa.

    Parámetros:
        No recibe parámetros.

    Retorna:
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

    Lógica:
        Recorre los datos de prueba por índice y copia las cinco notas mediante otro for. Se
        copian los datos para que las modificaciones posteriores no alteren las notas
        originales.

    Parámetros:
        No recibe parámetros.

    Retorna:
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
    Opción 2 del menú: carga los datos en la lista de diccionarios.

    Permite elegir entre la carga manual (validando cada dato) o la carga
    de los 1000 estudiantes de prueba hardcodeados.

    Lógica:
        Muestra dos alternativas y pide un entero válido entre 1 y 2. Si se elige 1 realiza
        la carga manual; si no, utiliza los datos de prueba (Nota 0). Informa que terminó la
        carga.

    Parámetros:
        No recibe parámetros.

    Retorna:
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

    Lógica:
        Arma una cadena con los títulos y agrega una columna por materia. Los formatos < y >
        alinean a izquierda y derecha dentro del ancho indicado. Imprime una línea de
        guiones del mismo largo para separar el encabezado.

    Parámetros:
        No recibe parámetros.

    Retorna:
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

    Lógica:
        Construye una fila con los datos del estudiante y recorre sus cinco notas. Comprueba
        si corresponde mostrar el promedio mediante None. El formato .2f muestra dos
        decimales sin modificar el valor almacenado. Finalmente imprime la fila.

    Parámetros:
        estudiante (dict): Diccionario del estudiante.

    Retorna:
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

    Lógica:
        Primero llama a mostrar_encabezado. Luego recorre todos los estudiantes y llama a
        mostrar_estudiante en cada iteración. Se separa mostrar uno de mostrar todos para
        reutilizar la función (Nota 6).

    Parámetros:
        estudiantes (list): Lista de diccionarios de estudiantes.

    Retorna:
        None
    """
    mostrar_encabezado()
    for estudiante in estudiantes:
        mostrar_estudiante(estudiante)


def opcion_mostrar_datos(estudiantes: list) -> None:
    """
    Opción 4 del menú: muestra la lista de diccionarios completa.

    Lógica:
        Imprime el título del informe y llama a mostrar_estudiantes para reutilizar la
        lógica de presentación.

    Parámetros:
        estudiantes (list): Lista de diccionarios de estudiantes.

    Retorna:
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

    Lógica:
        1. Si len(notas) es 0, devuelve 0 para evitar dividir por cero.
        2. Inicializa suma en 0 y recorre cada nota con for.
        3. Acumula con += y divide por len(notas). La división / produce un float; aquí no
        se redondea.

    Parámetros:
        notas (list): Lista de calificaciones del estudiante.

    Retorna:
        float: Promedio de las notas. Si la lista está vacía devuelve 0 (int).

    Ejemplo:
        calcular_promedio([10, 10, 7, 1, 4]) -> 6.4
    """
    if len(notas) == 0:
        return 0
    suma = 0
    for nota in notas:
        suma += nota
    return suma / len(notas)


def opcion_calcular_promedios(estudiantes: list) -> bool:
    """
    Función auxiliar de cálculo iterativo (no se llama desde el menú del TPI 4).

    calcula el promedio de cada estudiante y lo guarda
    en la clave "promedio" de su diccionario.

    Lógica:
        Recorre los estudiantes y llama a calcular_promedio con las notas de cada uno.
        Guarda el resultado en la estructura correspondiente. Imprime una confirmación y
        devuelve True para indicar que se calcularon.

    Parámetros:
        estudiantes (list): Lista de diccionarios (se modifica).

    Retorna:
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

    Lógica:
        1. Obtiene la cantidad n.
        2. El for externo realiza n - 1 pasadas; el interno compara vecinos j y j + 1 hasta
        n - 1 - i, porque al final ya hay elementos ordenados.
        3. En ASC intercambia si el primero es mayor; en DESC si es menor.
        4. Intercambia los datos asociados completos para conservar la identidad de cada
        estudiante. El ordenamiento modifica las estructuras originales, no crea copias.
        En la lista de diccionarios intercambia los diccionarios completos con auxiliar.

    Parámetros:
        estudiantes (list): Lista de diccionarios (se modifica).
        criterio (str): "ASC" para ordenar de menor a mayor,
            "DESC" para ordenar de mayor a menor.

    Retorna:
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
    Opción 6 del menú: pregunta si se ordena de forma ascendente o
    descendente, ordena a los estudiantes por promedio y los muestra.

    Lógica:
        Llama a ordenar_por_promedio con el criterio correspondiente y después a
        mostrar_estudiantes. Reutiliza las funciones de ordenamiento y presentación.
        Pide 1 para ASC o 2 para DESC y traduce esa elección al criterio.

    Parámetros:
        estudiantes (list): Lista de diccionarios (se modifica).

    Retorna:
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

    Lógica:
        Inicializa un acumulador en cero. Recorre los estudiantes sumando únicamente la nota
        del índice de materia indicado. Divide por la cantidad de estudiantes; requiere que
        haya al menos uno.

    Parámetros:
        estudiantes (list): Lista de diccionarios de estudiantes.
        indice_materia (int): Posición de la materia en la lista "notas" (0 a 4).

    Retorna:
        float: Promedio general de la materia.
    """
    suma = 0
    for estudiante in estudiantes:
        suma += estudiante["notas"][indice_materia]
    return suma / len(estudiantes)


def calcular_promedios_materias(estudiantes: list) -> list:
    """
    Calcula el promedio general de cada una de las 5 materias.

    Lógica:
        Crea una lista de cinco ceros. Recorre los índices de materias y guarda en cada
        posición el resultado de calcular_promedio_materia. Devuelve la lista de promedios
        generales.

    Parámetros:
        estudiantes (list): Lista de diccionarios de estudiantes.

    Retorna:
        list: Lista de 5 elementos; en la posición j está el promedio de MAT_(j + 1).
    """
    promedios_materias = [0] * CANTIDAD_MATERIAS
    for j in range(CANTIDAD_MATERIAS):
        promedios_materias[j] = calcular_promedio_materia(estudiantes, j)
    return promedios_materias


def buscar_maximo(lista: list) -> float:
    """
    Busca el valor más grande de una lista (sin usar max()).

    Lógica:
        Toma el primer elemento como máximo inicial (requiere una lista no vacía). Recorre
        los valores y reemplaza el máximo solo si encuentra uno mayor. Devuelve el mayor
        valor, no su índice.

    Parámetros:
        lista (list): Lista de números (no vacía).

    Retorna:
        float: El mayor valor de la lista.

    Ejemplo:
        buscar_maximo([4, 8, 6]) -> 8
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

    Lógica:
        Imprime el número de materia sumando 1 al índice y muestra su promedio con dos
        decimales mediante .2f.

    Parámetros:
        indice_materia (int): Posición de la materia (0 a 4).
        promedio (float): Promedio general de la materia.

    Retorna:
        None
    """
    print(f"MAT_{indice_materia + 1}  -  Promedio: {promedio:.2f}")


def mostrar_materias_mayor_promedio(promedios_materias: list) -> None:
    """
    Recorre TODAS las materias (mostrar todos) y llama a mostrar_materia()
    para cada una que tenga el mayor promedio general. Si hay empate, se
    muestran todas las empatadas.

    Lógica:
        Obtiene el máximo con buscar_maximo. Recorre todos los índices y llama a
        mostrar_materia cuando el promedio coincide con el máximo. Así también muestra todos
        los empates.

    Parámetros:
        promedios_materias (list): Promedio general de cada materia.

    Retorna:
        None
    """
    maximo = buscar_maximo(promedios_materias)
    for j in range(len(promedios_materias)):
        if promedios_materias[j] == maximo:
            mostrar_materia(j, promedios_materias[j])


def opcion_materias_mayor_promedio(estudiantes: list) -> None:
    """
    Opción 8 del menú: muestra la/s materia/s con mayor promedio general.

    Lógica:
        Calcula los promedios generales de las cinco materias, imprime el título y llama a
        mostrar_materias_mayor_promedio para informar las que tienen el máximo.

    Parámetros:
        estudiantes (list): Lista de diccionarios de estudiantes.

    Retorna:
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

    Lógica:
        Realiza una búsqueda secuencial: recorre los índices y compara el legajo de cada
        estudiante con el buscado. Si coincide devuelve el índice y termina. Si no encuentra
        coincidencias devuelve -1 como señal de ausencia.

    Parámetros:
        estudiantes (list): Lista de diccionarios de estudiantes.
        legajo_buscado (int): Legajo que se quiere encontrar.

    Retorna:
        int: Posición del estudiante en la lista si se encuentra; -1 si no existe.

    Ejemplo:
        Si el legajo está en la primera posición, devuelve 0; si no existe, -1.
    """
    for i in range(len(estudiantes)):
        if estudiantes[i]["legajo"] == legajo_buscado:
            return i
    return -1


def opcion_buscar_estudiante(estudiantes: list) -> None:
    """
    Opción 9 del menú: pide un legajo, lo busca y muestra todos los datos
    del estudiante, incluido el promedio calculado en la opción 3.

    Lógica:
        Pide un legajo entre 10000 y 99999 y llama a buscar_por_legajo. Si recibe -1 informa
        que no existe; si no, muestra el encabezado y los datos del estudiante encontrado.

    Parámetros:
        estudiantes (list): Lista de diccionarios de estudiantes.

    Retorna:
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

    Lógica:
        1. Crea diez contadores inicializados en cero.
        2. Resta 1 al número de materia para obtener el índice.
        3. Recorre los estudiantes y obtiene su nota en esa materia.
        4. Incrementa contadores[nota - 1], porque la nota 1 corresponde al índice 0 y la
        nota 10 al índice 9. Devuelve los diez contadores.

    Parámetros:
        estudiantes (list): Lista de diccionarios de estudiantes.
        numero_materia (int): Número de materia (índice + 1), entre 1 y 5.

    Retorna:
        list: Lista de 10 elementos. En el índice 0 está la cantidad de
        veces que aparece la nota 1, en el índice 1 la nota 2, y así hasta
        el índice 9, que corresponde a la nota 10.

    Ejemplo:
        Si las notas de la materia son 1, 1 y 10, devuelve [2, 0, 0, 0, 0, 0, 0, 0, 0, 1].
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

    Lógica:
        Imprime la nota y la cantidad de apariciones, usando anchos de campo para alinear
        los números.

    Parámetros:
        nota (int): Calificación (1 a 10).
        cantidad (int): Cantidad de veces que aparece.

    Retorna:
        None
    """
    print(f"Nota {nota:>2}: {cantidad:>4} vez/veces")


def mostrar_repeticiones(contadores: list) -> None:
    """
    Recorre los 10 contadores (mostrar todos) y llama a mostrar_repeticion()
    para cada nota.

    Lógica:
        Recorre los índices de los contadores y llama a mostrar_repeticion con i + 1 como
        nota y contadores[i] como frecuencia.

    Parámetros:
        contadores (list): Lista de 10 contadores devuelta por
            contar_calificaciones().

    Retorna:
        None
    """
    for i in range(len(contadores)):
        mostrar_repeticion(i + 1, contadores[i])


def opcion_contar_calificaciones(estudiantes: list) -> None:
    """
    Opción 10 del menú: pide un número de materia y muestra cuántas veces se
    repite cada calificación en esa materia.

    Lógica:
        Pide una materia válida entre 1 y 5. Llama a contar_calificaciones, imprime el
        título y pasa la lista resultante a mostrar_repeticiones.

    Parámetros:
        estudiantes (list): Lista de diccionarios de estudiantes.

    Retorna:
        None
    """
    numero_materia = pedir_entero(f"\nIngrese el número de materia (1 a {CANTIDAD_MATERIAS}): ",
                                  1, CANTIDAD_MATERIAS)
    contadores = contar_calificaciones(estudiantes, numero_materia)
    print(f"\n--- REPETICIONES DE NOTAS EN MAT_{numero_materia} ---\n")
    mostrar_repeticiones(contadores)


def validar_fila_csv(fila):
    """
    Convierte y valida los nueve campos de un registro CSV.

    Lógica:
        Comprueba que haya nueve campos. Convierte legajo y notas con int y promedio con
        float; strip elimina espacios externos y upper convierte el género a mayúsculas. Si
        una conversión falla, except ValueError devuelve None. Valida los campos y el rango
        del promedio (0 a 10); devuelve un diccionario si son válidos. No comprueba que el
        promedio coincida con las notas.

    Parámetros:
        No recibe parámetros.

    Retorna:
        None.
    """
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
    """
    Lee estudiantes válidos desde CSV, sin legajos duplicados.

    Lógica:
        Abre el archivo en lectura con with, que lo cierra automáticamente. csv.reader
        separa los campos y enumerate numera las filas desde 1. Valida cada fila y usa un
        set de legajos para detectar duplicados. append agrega registros válidos y add
        registra legajos. Si hay errores, duplicados, exceso de registros o problemas de
        lectura, devuelve una lista vacía; de lo contrario devuelve los estudiantes.

    Parámetros:
        No recibe parámetros.

    Retorna:
        None.
    """
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
    """
    Opción 1 del menú: solicita la ruta del CSV y devuelve los estudiantes válidos cargados.

    Lógica:
        Pide el nombre del archivo, elimina espacios externos con strip, llama a
        cargar_desde_csv e informa la cantidad de registros devueltos.

    Parámetros:
        No recibe parámetros.

    Retorna:
        None.
    """
    nombre = input('Nombre del archivo CSV: ').strip()
    estudiantes = cargar_desde_csv(nombre)
    print('Estudiantes cargados:', len(estudiantes))
    return estudiantes


def opcion_guardar_json(estudiantes):
    """
    Opción 11 del menú: guarda la lista de estudiantes en un archivo JSON solicitado por
    consola.

    Lógica:
        Pide el nombre de salida y rechaza una cadena vacía. Abre el archivo en modo w (crea
        o sobrescribe). json.dump escribe la lista de diccionarios; ensure_ascii=False
        conserva caracteres como ñ e indent=4 aplica sangría. Captura OSError si falla la
        escritura.

    Parámetros:
        No recibe parámetros.

    Retorna:
        None.
    """
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


def normalizar_estudiantes(estudiantes):
    """
    Normaliza los campos de texto con map.

    Lógica:
        map aplica una lambda a cada diccionario. {**e} copia sus claves y valores; nombre y
        genero se reemplazan por versiones en mayúsculas, y strip elimina espacios externos
        del nombre. list materializa el resultado. No modifica directamente la lista
        original.

    Parámetros:
        No recibe parámetros.

    Retorna:
        None.
    """
    return list(map(lambda e: {**e, 'nombre': e['nombre'].strip().upper(), 'genero': e['genero'].upper()}, estudiantes))


def opcion_normalizar(estudiantes):
    """
    Opción 3 del menú: normaliza los textos de todos los estudiantes mediante map.

    Lógica:
        Llama a normalizar_estudiantes y asigna el resultado a estudiantes[:]. La asignación
        por corte reemplaza el contenido de la misma lista, por lo que el cambio se conserva
        en main. Imprime una confirmación.

    Parámetros:
        No recibe parámetros.

    Retorna:
        None.
    """
    estudiantes[:] = normalizar_estudiantes(estudiantes)
    print('Nombres y géneros normalizados.')


def opcion_promedios_funcional(estudiantes):
    """
    Opción 5 del menú: calcula promedios mediante lambda y map.

    Lógica:
        Define una lambda que divide sum(notas) por len(notas). Otra lambda copia cada
        diccionario con **e y reemplaza su promedio. map aplica esa transformación a todos;
        list materializa el resultado y estudiantes[:] actualiza la lista original. Devuelve
        True para indicar que se calcularon los promedios.

    Parámetros:
        No recibe parámetros.

    Retorna:
        None.
    """
    promedio = lambda notas: sum(notas) / len(notas)
    estudiantes[:] = list(map(lambda e: {**e, 'promedio': promedio(e['notas'])}, estudiantes))
    print('Promedios calculados.')
    return True


def opcion_filtrar_desaprobados(estudiantes):
    """
    Opción 7 del menú: muestra los estudiantes cuyo promedio es menor que cuatro.

    Lógica:
        filter aplica la condición lambda e: e["promedio"] < 4 a cada estudiante. Conserva
        solo aquellos para los que es True. list convierte el iterador en lista. Si hay
        resultados los muestra; si no, informa que no hay desaprobados. Requiere promedios
        calculados.

    Parámetros:
        No recibe parámetros.

    Retorna:
        None.

    Ejemplo:
        Un promedio de 3.8 se incluye; uno de 4.0 no.
    """
    encontrados = list(filter(lambda e: e['promedio'] < 4, estudiantes))
    if encontrados:
        mostrar_estudiantes(encontrados)
    else:
        print('No hay estudiantes con promedio menor a 4.')


def mostrar_menu():
    """
    Muestra las opciones disponibles.

    Lógica:
        Imprime el título y las opciones numeradas con print. No lee la opción: esa tarea
        corresponde al programa principal.

    Parámetros:
        No recibe parámetros.

    Retorna:
        None.
    """
    print("\n=== SISTEMA DE ESTUDIANTES ===")
    print(1, "- Cargar desde archivo CSV")
    print(2, "- Cargar datos manualmente o de prueba")
    print(3, "- Normalizar textos en mayúsculas")
    print(4, "- Mostrar todos los datos")
    print(5, "- Calcular promedios (lambda y map)")
    print(6, "- Ordenar por promedio")
    print(7, "- Filtrar promedios menores a 4")
    print(8, "- Mostrar materias con mayor promedio")
    print(9, "- Buscar estudiante por legajo")
    print(10, "- Contar calificaciones por materia")
    print(11, "- Guardar datos en JSON")
    print(12, "- Salir")


def opcion_salir() -> None:
    """
    Opción 12 del menú: muestra el mensaje de salida del sistema.

    Lógica:
        Imprime el mensaje de despedida. El ciclo while del programa principal termina
        porque la opción elegida es la de salida.

    Parámetros:
        No recibe parámetros.

    Retorna:
        None.
    """
    print("\nSaliendo del programa.")
