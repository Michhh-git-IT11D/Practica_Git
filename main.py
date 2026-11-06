print("SISTEMA DE REGISTRO DE ESTUDIANTES")
print("1. Registrar estudiante")
print("2. Consultar estudiantes")
print("3. Salir")

estudiantes = []

def registrar_estudiante(nombre):
    estudiantes.append(nombre)
    print("Estudiante registrado:", nombre)
def consultar_estudiantes():
    print("ESTUDIANTES REGISTRADOS")
    for estudiante in estudiantes:
        print(estudiante)


def calcular_promedio(calificaciones):
    """Calcula la media de una lista de calificaciones numericas no vacia."""
    if not calificaciones:
        raise ValueError("Se necesita al menos una calificacion para calcular el promedio.")
    return sum(calificaciones) / len(calificaciones)

registrar_estudiante("Juan Pérez")
registrar_estudiante("María López")

consultar_estudiantes()

calificaciones = [8, 9, 10]
print("Promedio de calificaciones:", calcular_promedio(calificaciones))
