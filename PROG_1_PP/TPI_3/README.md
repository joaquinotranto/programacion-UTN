# TPI 3 — Documentación técnica y guía de defensa

## 1. Objetivo y alcance
Programa de consola en Python para administrar legajos, nombres, géneros, cinco calificaciones y promedios de estudiantes. Se desarrolló a partir de la consigna correspondiente de Programación I. No se utiliza una base de datos.

## 2. Organización de archivos
- `main.py`: punto de entrada. Mantiene el estado, ejecuta el `while` del menú y distribuye las opciones mediante `match`.
- `funciones.py`: biblioteca propia con carga, cálculos, consultas, visualización y operaciones de cada opción del menú.
- `validaciones.py`: funciones propias que verifican y solicitan datos válidos.
- `datos_prueba.py`: conjunto de datos de ejemplo para ejecutar y verificar el programa.
- `estudiantes.csv`: archivo de texto separado por comas para cargar estudiantes; cada fila contiene legajo, nombre, género, cinco notas y promedio.

## 3. Representación de los datos
Se utiliza una **lista de diccionarios**. Cada diccionario contiene `legajo` (entero de cinco cifras), `nombre` (texto), `genero` (`F`, `M` o `X`), `notas` (lista de cinco enteros entre 1 y 10) y `promedio` (valor calculado). El trabajo contempla hasta 1000 estudiantes.

## 4. Opciones del menú — explicación de la consigna
1. **Cargar estudiantes desde un archivo CSV ingresado por consola.**
2. **Cargar estudiantes manualmente.**
3. **Mostrar estudiantes con encabezado.**
4. **Calcular y guardar promedios.**
5. **Ordenar por promedio ASC o DESC.**
6. **Mostrar materia(s) con mayor promedio general.**
7. **Buscar estudiante por legajo.**
8. **Contar frecuencias de notas de una materia.**
9. **Guardar estudiantes en JSON.**
10. **Salir.**

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

## 6. Archivos CSV y JSON
**CSV:** el programa solicita el nombre del archivo al ejecutar la opción de carga; el archivo debe existir en el entorno de ejecución. El formato de fila es `legajo,nombre,genero,nota1,nota2,nota3,nota4,nota5,promedio`.
**JSON:** la opción de guardado serializa los registros de la lista de diccionarios en un archivo `.json`. Para verificarlo, hay que ejecutar la opción y comprobar el archivo generado.

## 8. Biblioteca de funciones: documentación del código
Las descripciones siguientes proceden de los docstrings incluidos en los archivos Python de esta entrega. Se mantienen sus nombres reales para que puedas encontrarlas en OnlineGDB.

### `funciones.py`

#### `crear_estudiante(legajo, nombre, genero, notas)`

Crea el diccionario de un estudiante con todas sus claves.

El promedio arranca en None porque todavía no fue calculado.

Args:
    legajo (int): Legajo de 5 cifras.
    nombre (str): Nombre del estudiante.
    genero (str): 'F', 'M' o 'X'.
    notas (list): Lista de 5 calificaciones entre 1 y 10.

Returns:
    dict: Diccionario con las claves legajo, nombre, genero, notas y promedio.

#### `cargar_estudiante_manual(estudiantes, indice)`

Pide por consola todos los datos de un estudiante, validando cada uno,
y devuelve el diccionario armado.

Args:
    estudiantes (list): Lista de estudiantes (se usa para verificar que
        el legajo no esté repetido entre los ya cargados).
    indice (int): Posición del estudiante que se está cargando
        (también es la cantidad de estudiantes ya cargados).

Returns:
    dict: Diccionario del estudiante cargado.

#### `cargar_datos_manual()`

Carga manual: pide la cantidad de estudiantes (1 a 1000) y después los
datos de cada uno.

La lista se crea con el tamaño elegido y se completa por posición, sin
usar append.

Returns:
    list: Lista de diccionarios con los estudiantes cargados.

#### `cargar_datos_prueba()`

Carga los 1000 estudiantes hardcodeados del módulo datos_prueba.

Arma un diccionario nuevo para cada estudiante (con la clave promedio
en None) y copia también la lista de notas, para no modificar los datos
originales del módulo.

Returns:
    list: Lista de diccionarios con los estudiantes de prueba.

#### `opcion_cargar_datos()`

Opción 1 del menú: carga los datos en la lista de diccionarios.

Permite elegir entre la carga manual (validando cada dato) o la carga
de los 1000 estudiantes de prueba hardcodeados.

Returns:
    list: Lista de diccionarios con los estudiantes cargados.

#### `mostrar_encabezado()`

Muestra el encabezado de la tabla, con cada clave al lado de la otra:
LEGAJO | NOMBRE | GENERO | N1 | N2 | N3 | N4 | N5 | PROM

Returns:
    None

#### `mostrar_estudiante(estudiante)`

Muestra en una línea todos los datos de UN estudiante (mostrar uno):
legajo, nombre, género, las 5 notas y el promedio.

Si el promedio todavía no se calculó (vale None), muestra un guion.

Args:
    estudiante (dict): Diccionario del estudiante.

Returns:
    None

#### `mostrar_estudiantes(estudiantes)`

Muestra TODOS los estudiantes (mostrar todos): imprime el encabezado y
recorre la lista con un for, llamando a mostrar_estudiante() para cada
diccionario (Nota 6 del TP).

Args:
    estudiantes (list): Lista de diccionarios de estudiantes.

Returns:
    None

#### `opcion_mostrar_datos(estudiantes)`

Opción 2 del menú: muestra la lista de diccionarios completa.

Args:
    estudiantes (list): Lista de diccionarios de estudiantes.

Returns:
    None

#### `calcular_promedio(notas)`

Calcula el promedio de una lista de calificaciones.

Suma todas las notas recorriendo la lista y divide por la cantidad.

Args:
    notas (list): Lista de calificaciones del estudiante.

Returns:
    float: Promedio de las notas. Si la lista está vacía devuelve 0.

#### `opcion_calcular_promedios(estudiantes)`

Opción 3 del menú: calcula el promedio de cada estudiante y lo guarda
en la clave "promedio" de su diccionario.

Args:
    estudiantes (list): Lista de diccionarios (se modifica).

Returns:
    bool: True cuando los promedios quedaron calculados.

#### `ordenar_por_promedio(estudiantes, criterio)`

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

#### `opcion_ordenar_y_mostrar(estudiantes)`

Opción 4 del menú: pregunta si se ordena de forma ascendente o
descendente, ordena a los estudiantes por promedio y los muestra.

Args:
    estudiantes (list): Lista de diccionarios (se modifica).

Returns:
    None

#### `calcular_promedio_materia(estudiantes, indice_materia)`

Calcula el promedio general de una materia: suma la nota de esa
materia de todos los estudiantes y la divide por la cantidad.

Args:
    estudiantes (list): Lista de diccionarios de estudiantes.
    indice_materia (int): Posición de la materia en la lista "notas" (0 a 4).

Returns:
    float: Promedio general de la materia.

#### `calcular_promedios_materias(estudiantes)`

Calcula el promedio general de cada una de las 5 materias.

Args:
    estudiantes (list): Lista de diccionarios de estudiantes.

Returns:
    list: Lista de 5 elementos; en la posición j está el promedio de MAT_(j + 1).

#### `buscar_maximo(lista)`

Busca el valor más grande de una lista (sin usar max()).

Args:
    lista (list): Lista de números (no vacía).

Returns:
    float: El mayor valor de la lista.

#### `mostrar_materia(indice_materia, promedio)`

Muestra UNA materia con su promedio (mostrar uno).

El nombre se arma como MAT_ más el índice de la materia más uno.

Args:
    indice_materia (int): Posición de la materia (0 a 4).
    promedio (float): Promedio general de la materia.

Returns:
    None

#### `mostrar_materias_mayor_promedio(promedios_materias)`

Recorre TODAS las materias (mostrar todos) y llama a mostrar_materia()
para cada una que tenga el mayor promedio general. Si hay empate, se
muestran todas las empatadas.

Args:
    promedios_materias (list): Promedio general de cada materia.

Returns:
    None

#### `opcion_materias_mayor_promedio(estudiantes)`

Opción 5 del menú: muestra la/s materia/s con mayor promedio general.

Args:
    estudiantes (list): Lista de diccionarios de estudiantes.

Returns:
    None

#### `buscar_por_legajo(estudiantes, legajo_buscado)`

Busca un estudiante por legajo recorriendo la lista (búsqueda secuencial).

Args:
    estudiantes (list): Lista de diccionarios de estudiantes.
    legajo_buscado (int): Legajo que se quiere encontrar.

Returns:
    int: Posición del estudiante en la lista si se encuentra; -1 si no existe.

#### `opcion_buscar_estudiante(estudiantes)`

Opción 6 del menú: pide un legajo, lo busca y muestra todos los datos
del estudiante, incluido el promedio calculado en la opción 3.

Args:
    estudiantes (list): Lista de diccionarios de estudiantes.

Returns:
    None

#### `contar_calificaciones(estudiantes, numero_materia)`

Cuenta cuántas veces se repite cada calificación (1 a 10) en una materia.

Args:
    estudiantes (list): Lista de diccionarios de estudiantes.
    numero_materia (int): Número de materia (índice + 1), entre 1 y 5.

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

Recorre los 10 contadores (mostrar todos) y llama a mostrar_repeticion()
para cada nota.

Args:
    contadores (list): Lista de 10 contadores devuelta por
        contar_calificaciones().

Returns:
    None

#### `opcion_contar_calificaciones(estudiantes)`

Opción 7 del menú: pide un número de materia y muestra cuántas veces se
repite cada calificación en esa materia.

Args:
    estudiantes (list): Lista de diccionarios de estudiantes.

Returns:
    None

#### `validar_fila_csv(fila)`

Convierte y valida los nueve campos de un registro CSV.

#### `cargar_desde_csv(nombre_archivo)`

Lee estudiantes válidos desde CSV, sin legajos duplicados.

#### `opcion_cargar_csv()`

Solicita la ruta del CSV y devuelve los estudiantes válidos cargados.

#### `opcion_guardar_json(estudiantes)`

Guarda la lista de estudiantes en un archivo JSON solicitado por consola.

#### `mostrar_menu()`

Muestra las opciones disponibles.

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

#### `validar_notas(notas)`

Verifica que las notas de un estudiante sean una lista de cinco (5)
calificaciones enteras entre 1 y 10.

Args:
    notas (list): Lista de calificaciones del estudiante.

Returns:
    bool: True si la lista tiene 5 elementos y todos son notas válidas;
    False en caso contrario.

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

#### `validar_legajo(legajo, estudiantes, cantidad_cargados)`

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

#### `pedir_legajo(mensaje, estudiantes, cantidad_cargados)`

Pide un legajo hasta que sea un entero de cinco cifras no repetido.

Args:
    mensaje (str): Texto que se muestra al pedir el legajo.
    estudiantes (list): Lista de diccionarios de estudiantes.
    cantidad_cargados (int): Cuántos estudiantes ya están cargados.

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
9. Probar carga de `estudiantes.csv`, y también un nombre de archivo inexistente.
10. Guardar JSON y abrirlo para confirmar su contenido.

## 10. Preguntas típicas de defensa
**¿Por qué separamos los archivos?** Para mantener la ejecución principal, las reglas de validación y la lógica del negocio organizadas en módulos.
**¿Qué es un docstring?** Es una cadena de documentación escrita inmediatamente debajo de la definición de una función (o al inicio de un módulo) que explica su propósito, parámetros y resultado.
**¿Qué hace `match`?** Selecciona qué función ejecutar según la opción elegida en el menú.
**¿Qué hace `while`?** Repite el menú hasta que el usuario selecciona salir.
**¿Cómo se obtiene el promedio?** Se suman las cinco notas y se divide por cinco.
**¿Por qué validar?** Para impedir registros incompatibles con los requisitos del problema.
**¿Qué es un diccionario?** Una estructura que guarda pares clave-valor, por ejemplo `legajo` y su número.
**¿Cuál es la diferencia entre CSV y JSON?** CSV representa registros en filas de campos separados por comas; JSON representa estructuras de datos con listas y objetos/diccionarios.

## 11. Alcance de esta documentación
La existencia de funciones y docstrings se comprobó mediante inspección de los archivos. Esta guía no equivale a certificar que todas las rutas interactivas hayan sido probadas exhaustivamente. Antes de la defensa se recomienda realizar las pruebas del apartado 9 en OnlineGDB.
