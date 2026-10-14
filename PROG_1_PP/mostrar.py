"""
Módulo: mostrar.py

Descripción:
    Se encarga de mostrar los datos de los estudiantes por consola
    en forma de tabla.

Nota 6 de la consigna:
    - mostrar_estudiante muestra UN solo estudiante (una fila).
    - mostrar_estudiantes recorre TODOS los estudiantes y, por cada uno,
      llama a mostrar_estudiante. O sea, la segunda función se llama
      dentro de la primera.

Funciones:
    mostrar_estudiante(legajo, nombre, genero, nota1, nota2, promedio)
    mostrar_estudiantes(titulo, legajos, nombres, generos, notas1, notas2, promedios)
"""


def mostrar_estudiante(legajo, nombre, genero, nota1, nota2, promedio=None):
    """
    Muestra una fila de la tabla con los datos de un estudiante.

    Lógica:
        - Si no se recibe promedio (vale None), imprime la fila sin
          la columna de promedio.
        - Si se recibe promedio, lo imprime al final con 2 decimales.
        En el f-string, :<8, :<22 y :<10 indican el ancho de cada
        columna alineada a la izquierda, para que la tabla quede
        derecha. :.2f muestra el número con 2 decimales.

    Parámetros:
        legajo (int): legajo del estudiante.
        nombre (str): apellido y nombre.
        genero (str): F, M o X.
        nota1 (int): nota del parcial 1.
        nota2 (int): nota del parcial 2.
        promedio (float, opcional): promedio del estudiante. Por
            defecto vale None (no se muestra).

    Retorna:
        No retorna nada (solo imprime).
    """
    if promedio is None:
        print(f"{legajo:<8}{nombre:<22}{genero:<8}{nota1:<10}{nota2:<10}")
    else:
        print(f"{legajo:<8}{nombre:<22}{genero:<8}{nota1:<10}{nota2:<10}{promedio:.2f}")


def mostrar_estudiantes(titulo, legajos, nombres, generos, notas1, notas2, promedios=None):
    """
    Muestra un informe completo: título, encabezado y una fila por
    cada estudiante.

    Lógica:
        1. Imprime una línea de "=", el título y otra línea de "=".
           ("=" * 66 repite el signo 66 veces.)
        2. Imprime el encabezado de las columnas. Si hay promedios,
           agrega la columna "Promedio".
        3. Con un for recorre las posiciones de 0 hasta len(legajos)-1.
        4. Por cada posición i llama a mostrar_estudiante con los datos
           de esa posición en cada lista paralela.
        5. Imprime una línea final de cierre.
        Recibe el título como parámetro para poder reutilizarla en
        todos los informes (opciones 2, 4, 5 y 6).

    Parámetros:
        titulo (str): título del informe.
        legajos, nombres, generos, notas1, notas2 (list): listas paralelas.
        promedios (list, opcional): lista de promedios. Por defecto None.

    Retorna:
        No retorna nada (solo imprime).
    """
    print("\n" + "=" * 66)
    print(titulo)
    print("=" * 66)

    if promedios is None:
        print(f"{'Legajo':<8}{'Apellido y nombre':<22}{'Género':<8}{'Parcial 1':<10}{'Parcial 2':<10}")
    else:
        print(f"{'Legajo':<8}{'Apellido y nombre':<22}{'Género':<8}{'Parcial 1':<10}{'Parcial 2':<10}Promedio")
    print("-" * 66)

    for i in range(len(legajos)):
        if promedios is None:
            mostrar_estudiante(legajos[i], nombres[i], generos[i], notas1[i], notas2[i])
        else:
            mostrar_estudiante(legajos[i], nombres[i], generos[i], notas1[i], notas2[i], promedios[i])

    print("=" * 66)
