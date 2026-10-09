"""
Módulo datos_prueba.
Datos hardcodeados de 30 estudiantes para probar el programa sin tener
que cargar todo a mano (lo permite la Nota 0 de la consigna).
"""


def obtener_datos_prueba():
    """
    Devuelve las cinco listas paralelas con datos de prueba ya válidos.

    Retorna:
        tuple: (legajos, nombres, generos, notas1, notas2)
    """
    legajos = [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010,
               1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019, 1020,
               1021, 1022, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030]

    nombres = ["Gomez Ana", "Perez Juan", "Lopez Sofia", "Martinez Lucas",
               "Garcia Camila", "Rodriguez Mateo", "Fernandez Alex",
               "Sanchez Valentina", "Romero Tomas", "Diaz Martina",
               "Alvarez Bruno", "Torres Julieta", "Ruiz Sam",
               "Benitez Lautaro", "Acosta Mia", "Medina Franco",
               "Herrera Lucia", "Suarez Nicolas", "Aguirre Emma",
               "Gimenez Joaquin", "Molina Noa", "Silva Agustina",
               "Castro Thiago", "Rios Paula", "Ortiz Ramiro", "Morales Abril",
               "Ramos Facundo", "Vega Renata", "Flores Kim", "Cabrera Santino"]

    generos = ["F", "M", "F", "M", "F", "M", "X", "F", "M", "F",
               "M", "F", "X", "M", "F", "M", "F", "M", "F", "M",
               "X", "F", "M", "F", "M", "F", "M", "F", "X", "M"]

    notas1 = [7, 6, 9, 4, 8, 5, 10, 7, 3, 8,
              6, 9, 2, 7, 5, 8, 6, 4, 7, 9,
              5, 8, 6, 7, 9, 4, 8, 6, 7, 5]

    notas2 = [8, 5, 10, 6, 7, 4, 9, 7, 5, 9,
              7, 8, 4, 6, 6, 8, 9, 3, 9, 7,
              5, 6, 6, 5, 9, 7, 5, 8, 4, 9]

    return legajos, nombres, generos, notas1, notas2
