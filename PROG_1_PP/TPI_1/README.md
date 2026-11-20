# TPI 1 — Documentación técnica y guía de defensa

## 1. Objetivo y alcance
Programa de consola en Python para administrar legajos, nombres, géneros, cinco calificaciones y promedios de estudiantes. Se desarrolló a partir de la consigna correspondiente de Programación I. No se utiliza una base de datos.

## 2. Organización de archivos
- `main.py`: punto de entrada. Mantiene el estado, ejecuta el `while` del menú y distribuye las opciones mediante `match`.
- `funciones.py`: biblioteca propia con carga, cálculos, consultas, visualización y operaciones de cada opción del menú.
- `validaciones.py`: funciones propias que verifican y solicitan datos válidos.
- `datos_prueba.py`: conjunto de datos de ejemplo para ejecutar y verificar el programa.

## 3. Representación de los datos
Se usan **listas paralelas** para legajo, nombre y género; una **matriz de 30 filas por 5 columnas** para las notas; y una lista adicional para promedios. El índice de cada lista identifica al mismo estudiante que la fila correspondiente de la matriz. Al ordenar deben mantenerse alineados todos esos datos.

## 4. Opciones del menú — explicación de la consigna
1. **Cargar 30 estudiantes en listas paralelas y matriz de 30 × 5.**
2. **Mostrar todos los estudiantes.**
3. **Calcular y guardar promedios en una lista.**
4. **Ordenar por promedio DESC y mostrar.**
5. **Mostrar materia(s) con mayor promedio general.**
6. **Buscar estudiante por legajo.**
7. **Contar frecuencias de notas de una materia.**
8. **Salir.**

## 5. Reglas de validación y funcionamiento
- El legajo debe ser un número entero de **cinco cifras**.
- El nombre debe cumplir la validación de texto definida en `validaciones.py`.
- El género se restringe a `F`, `M` o `X`.
- Cada estudiante tiene **cinco notas enteras**, cada una de **1 a 10**.
- Se evita ejecutar consultas y cálculos sin haber cargado previamente datos; cargar y salir son excepciones.
- Las funciones de `validaciones.py` se utilizan para centralizar la verificación de entradas y evitar repetir lógica.
- `mostrar_estudiantes` recorre la colección y llama a `mostrar_estudiante` para imprimir un registro; en el TPI 1 también se conserva la correspondencia entre listas y matriz.
- El promedio individual se calcula sumando las cinco notas y dividiendo por cinco.
- El promedio de una materia se calcula con las notas de esa columna de todos los estudiantes; si varias materias empatan en el máximo, deben mostrarse todas.
- Para contar notas se devuelve una lista de **10 posiciones**: índice 0 = frecuencia de nota 1, ..., índice 9 = frecuencia de nota 10.
- El menú se implementa con `match` dentro de un ciclo `while`.

## 8. Biblioteca de funciones: documentación del código
Las descripciones siguientes proceden de los docstrings incluidos en los archivos Python de esta entrega. Se mantienen sus nombres reales para que puedas encontrarlas en OnlineGDB.

### `funciones.py`

#### `crear_matriz(filas, columnas, valor_inicial)`

Crea e inicializa una matriz (lista de listas) con un mismo valor.

Cada fila se crea por separado para que las filas no compartan la
misma lista en memoria.

Args:
    filas (int): Cantidad de filas.
    columnas (int): Cantidad de columnas.
    valor_inicial (int): Valor con el que se llena cada celda.

Returns:
    list: Matriz de filas x columnas con todas las celdas en valor_inicial.

#### `mostrar_menu()`

Muestra por consola el menú de opciones del programa.

Returns:
    None

#### `cargar_estudiante_manual(matriz, nombres, generos, legajos, indice)`

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

#### `cargar_datos_prueba(matriz, nombres, generos, legajos)`

Copia los datos hardcodeados del módulo datos_prueba a la matriz y a
las listas del programa, elemento por elemento.

Args:
    matriz (list): Matriz de calificaciones (se modifica).
    nombres (list): Lista de nombres (se modifica).
    generos (list): Lista de géneros (se modifica).
    legajos (list): Lista de legajos (se modifica).

Returns:
    None

#### `opcion_cargar_datos(matriz, nombres, generos, legajos)`

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

#### `mostrar_encabezado(con_promedio)`

Muestra la fila de títulos de la tabla de estudiantes.

Args:
    con_promedio (bool): True para agregar la columna PROMEDIO.

Returns:
    None

#### `mostrar_estudiante(matriz, nombres, generos, legajos, promedios, indice)`

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

#### `mostrar_estudiantes(matriz, nombres, generos, legajos, promedios)`

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

#### `opcion_mostrar_datos(matriz, nombres, generos, legajos)`

Opción 2 del menú: muestra la matriz completa de calificaciones junto
con las listas de legajo, nombre y género.

Args:
    matriz (list): Matriz de calificaciones.
    nombres (list): Lista de nombres.
    generos (list): Lista de géneros.
    legajos (list): Lista de legajos.

Returns:
    None

#### `calcular_promedio(notas)`

Calcula el promedio de una lista de calificaciones.

Suma todas las notas recorriendo la lista y divide por la cantidad.

Args:
    notas (list): Lista de calificaciones (una fila de la matriz).

Returns:
    float: Promedio de las notas. Si la lista está vacía devuelve 0.

#### `opcion_calcular_promedios(matriz, promedios)`

Opción 3 del menú: calcula el promedio de cada estudiante y lo guarda
en la lista de promedios (paralela a la matriz).

Args:
    matriz (list): Matriz de calificaciones.
    promedios (list): Lista donde se guardan los promedios (se modifica).

Returns:
    bool: True cuando los promedios quedaron calculados.

#### `intercambiar(lista, i, j)`

Intercambia los elementos de las posiciones i y j de una lista.

Si la lista es la matriz, intercambia filas completas.

Args:
    lista (list): Lista (o matriz) a modificar.
    i (int): Primera posición.
    j (int): Segunda posición.

Returns:
    None

#### `ordenar_por_promedio(matriz, nombres, generos, legajos, promedios, criterio)`

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

#### `opcion_ordenar_y_mostrar(matriz, nombres, generos, legajos, promedios)`

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

#### `calcular_promedio_materia(matriz, columna)`

Calcula el promedio general de una materia (una columna de la matriz).

Args:
    matriz (list): Matriz de calificaciones.
    columna (int): Índice de la columna (0 a 4).

Returns:
    float: Promedio de todas las notas de esa columna.

#### `calcular_promedios_materias(matriz)`

Calcula el promedio general de cada materia.

Args:
    matriz (list): Matriz de calificaciones.

Returns:
    list: Lista de 5 elementos; en la posición j está el promedio de
    MATERIA_(j + 1).

#### `buscar_maximo(lista)`

Busca el valor más grande de una lista (sin usar max()).

Args:
    lista (list): Lista de números (no vacía).

Returns:
    float: El mayor valor de la lista.

#### `mostrar_materia(columna, promedio)`

Muestra UNA materia con su promedio (mostrar uno).

El nombre se arma como MATERIA_ más el índice de la columna más uno.

Args:
    columna (int): Índice de la columna de la materia.
    promedio (float): Promedio general de la materia.

Returns:
    None

#### `mostrar_materias_mayor_promedio(promedios_materias)`

Muestra TODAS las materias que tienen el mayor promedio general
(mostrar todos). Si hay empate, se muestran todas las empatadas.

Recorre los promedios y llama a mostrar_materia() para cada materia
cuyo promedio es igual al máximo (Nota 6 del TP).

Args:
    promedios_materias (list): Promedio de cada materia.

Returns:
    None

#### `opcion_materias_mayor_promedio(matriz)`

Opción 5 del menú: muestra la/s materia/s con mayor promedio general.

Args:
    matriz (list): Matriz de calificaciones.

Returns:
    None

#### `buscar_por_legajo(legajos, legajo_buscado)`

Busca un legajo en la lista de legajos (búsqueda secuencial).

Args:
    legajos (list): Lista de legajos.
    legajo_buscado (int): Legajo que se quiere encontrar.

Returns:
    int: Índice (fila) del estudiante si se encuentra; -1 si no existe.

#### `opcion_buscar_estudiante(matriz, nombres, generos, legajos, promedios)`

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

#### `contar_calificaciones(matriz, numero_materia)`

Cuenta cuántas veces se repite cada calificación (1 a 10) en una materia.

Args:
    matriz (list): Matriz de calificaciones.
    numero_materia (int): Número de materia (índice de columna + 1),
        entre 1 y 5.

Returns:
    list: Lista de 10 elementos. En el índice 0 está la cantidad de
    veces que aparece la nota 1, en el índice 1 la nota 2, y así hasta
    el índice 9, que corresponde a la nota 10.

#### `mostrar_repeticion(nota, cantidad)`

Muestra cuántas veces aparece UNA nota (mostrar uno).

Args:
    nota (int): Calificación (1 a 10).
    cantidad (int): Cantidad de veces que aparece.

Returns:
    None

#### `mostrar_repeticiones(contadores)`

Muestra cuántas veces aparece cada nota (mostrar todos), llamando a
mostrar_repeticion() para cada una.

Args:
    contadores (list): Lista de 10 contadores devuelta por
        contar_calificaciones().

Returns:
    None

#### `opcion_contar_calificaciones(matriz)`

Opción 7 del menú: pide un número de materia y muestra cuántas veces
se repite cada calificación en esa materia.

Args:
    matriz (list): Matriz de calificaciones.

Returns:
    None

#### `opcion_salir()`

Muestra el mensaje de salida del sistema.

### `validaciones.py`

#### `es_numero_entero(texto)`

Verifica si un texto está formado solamente por dígitos (0 al 9).

Recorre el texto caracter por caracter y compara cada uno contra el
rango '0'..'9'. Un texto vacío no se considera número.

Args:
    texto (str): Texto ingresado por el usuario.

Returns:
    bool: True si el texto no está vacío y todos sus caracteres son
    dígitos; False en caso contrario.

#### `validar_rango(numero, minimo, maximo)`

Verifica que un número entero esté dentro de un rango (incluye los bordes).

Args:
    numero (int): Número a validar.
    minimo (int): Valor mínimo permitido.
    maximo (int): Valor máximo permitido.

Returns:
    bool: True si minimo <= numero <= maximo; False en caso contrario.

#### `validar_calificacion(calificacion)`

Verifica que una calificación sea un entero entre 1 y 10.

Args:
    calificacion (int): Nota a validar.

Returns:
    bool: True si la nota está entre 1 y 10 inclusive; False si no.

#### `es_letra(caracter)`

Verifica si un caracter es una letra (incluye acentos, ñ y ü).

Args:
    caracter (str): Un único caracter.

Returns:
    bool: True si es una letra mayúscula o minúscula; False si no.

#### `validar_nombre(nombre)`

Verifica que un nombre sea válido.

Un nombre es válido si tiene al menos 2 caracteres, está formado solo
por letras y espacios, y contiene al menos una letra.

Args:
    nombre (str): Nombre del estudiante.

Returns:
    bool: True si el nombre es válido; False en caso contrario.

#### `validar_genero(genero)`

Verifica que el género sea 'F', 'M' o 'X' (en mayúscula).

Args:
    genero (str): Género del estudiante.

Returns:
    bool: True si el género es 'F', 'M' o 'X'; False en caso contrario.

#### `validar_legajo(legajo, legajos, cantidad_cargados)`

Verifica que un legajo sea un entero de cinco cifras y que no esté repetido.

Un número de cinco cifras está entre 10000 y 99999. Además se revisan
los legajos ya cargados (de la posición 0 hasta cantidad_cargados - 1)
para que no haya dos estudiantes con el mismo legajo.

Args:
    legajo (int): Legajo a validar.
    legajos (list): Lista de legajos del programa.
    cantidad_cargados (int): Cuántos legajos de la lista ya están cargados.

Returns:
    bool: True si el legajo tiene cinco cifras y no está repetido;
    False en caso contrario.

#### `pedir_entero(mensaje, minimo, maximo)`

Pide un número entero por consola hasta que sea válido y esté en rango.

Args:
    mensaje (str): Texto que se muestra al pedir el dato.
    minimo (int): Valor mínimo aceptado.
    maximo (int): Valor máximo aceptado.

Returns:
    int: El número ingresado, ya validado.

#### `pedir_calificacion(mensaje)`

Pide una calificación por consola hasta que sea un entero entre 1 y 10.

Args:
    mensaje (str): Texto que se muestra al pedir la nota.

Returns:
    int: La calificación ingresada, ya validada.

#### `pedir_nombre(mensaje)`

Pide el nombre de un estudiante hasta que sea válido.

Args:
    mensaje (str): Texto que se muestra al pedir el nombre.

Returns:
    str: El nombre ingresado, ya validado.

#### `convertir_genero(texto)`

Convierte 'f', 'm' o 'x' en minúscula a su versión en mayúscula.

Se hace con comparaciones para no usar el método upper(). Si el texto
no es una de esas letras, se devuelve igual que vino.

Args:
    texto (str): Género ingresado por el usuario.

Returns:
    str: El género en mayúscula, o el texto original si no corresponde.

#### `pedir_genero(mensaje)`

Pide el género de un estudiante hasta que sea 'F', 'M' o 'X'.

Acepta también las letras en minúscula y las convierte a mayúscula.

Args:
    mensaje (str): Texto que se muestra al pedir el género.

Returns:
    str: 'F', 'M' o 'X'.

#### `pedir_legajo(mensaje, legajos, cantidad_cargados)`

Pide un legajo hasta que sea un entero de cinco cifras no repetido.

Args:
    mensaje (str): Texto que se muestra al pedir el legajo.
    legajos (list): Lista de legajos del programa.
    cantidad_cargados (int): Cuántos legajos ya están cargados.

Returns:
    int: El legajo ingresado, ya validado.

## 9. Pruebas recomendadas antes de entregar
1. Ejecutar `main.py` y elegir una opción de consulta antes de cargar datos: debe bloquearla.
2. Cargar datos de prueba o ingresar registros válidos.
3. Intentar un legajo corto, género distinto de F/M/X, y notas 0 y 11: deben rechazarse.
4. Mostrar registros y comprobar legajos, cinco notas y encabezado.
5. Calcular promedio y verificar un caso a mano, por ejemplo `[8, 7, 9, 6, 10]` produce `8.0`.
6. Ordenar ASC/DESC (según las opciones disponibles) y comprobar los extremos.
7. Buscar un legajo existente y otro inexistente.
8. Elegir una materia y comprobar que la suma de las 10 frecuencias sea igual al número de estudiantes cargados.

## 10. Preguntas típicas de defensa
**¿Por qué separamos los archivos?** Para mantener la ejecución principal, las reglas de validación y la lógica del negocio organizadas en módulos.
**¿Qué es un docstring?** Es una cadena de documentación escrita inmediatamente debajo de la definición de una función (o al inicio de un módulo) que explica su propósito, parámetros y resultado.
**¿Qué hace `match`?** Selecciona qué función ejecutar según la opción elegida en el menú.
**¿Qué hace `while`?** Repite el menú hasta que el usuario selecciona salir.
**¿Cómo se obtiene el promedio?** Se suman las cinco notas y se divide por cinco.
**¿Por qué validar?** Para impedir registros incompatibles con los requisitos del problema.
**¿Qué son listas paralelas?** Listas cuyos elementos del mismo índice pertenecen al mismo estudiante; la matriz usa esa misma posición para sus notas.

## 11. Alcance de esta documentación
La existencia de funciones y docstrings se comprobó mediante inspección de los archivos. Esta guía no equivale a certificar que todas las rutas interactivas hayan sido probadas exhaustivamente. Antes de la defensa se recomienda realizar las pruebas del apartado 9 en OnlineGDB.
