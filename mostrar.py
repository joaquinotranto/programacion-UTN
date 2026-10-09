"""
Módulo mostrar.
Tiene una función que muestra UN estudiante y otra que recorre TODOS
y llama a la primera por cada uno (Nota 6 de la consigna).
"""


def mostrar_estudiante(legajo, nombre, genero, nota1, nota2, promedio=None):
    """
    Muestra una fila (un estudiante) del informe.

    Parámetros:
        legajo (int), nombre (str), genero (str), nota1 (int), nota2 (int)
        promedio (float, opcional): si se pasa, se muestra con 2 decimales.
    """
    if promedio is None:
        print(f"{legajo:<8}{nombre:<22}{genero:<8}{nota1:<10}{nota2:<10}")
    else:
        print(f"{legajo:<8}{nombre:<22}{genero:<8}{nota1:<10}{nota2:<10}{promedio:.2f}")


def mostrar_estudiantes(titulo, legajos, nombres, generos, notas1, notas2, promedios=None):
    """
    Muestra un informe con título, encabezado y una fila por estudiante.
    Recorre las listas paralelas y llama a mostrar_estudiante por cada posición.

    Parámetros:
        titulo (str): título del informe.
        legajos, nombres, generos, notas1, notas2 (list): listas paralelas.
        promedios (list, opcional): si se pasa, se agrega la columna Promedio.
    """
    print("\n" + "=" * 66)
    print(titulo.center(66))
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
