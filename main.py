print("SISTEMA DE REGISTRO DE ESTUDIANTES")
print("1. Registrar estudiante")
print("2. Consultar estudiantes")
print("3. Salir")

estudiantes = []

def registrar_estudiante(nombre):
estudiantes.append(nombre)
  print("Estudiante registrado:", nombre)
ndef consultar_estudiantes():
print ("ESTUDIANTES REGISTRADOS")
   for estudiante in estudiantes:
 print(estudiante)

registrar_estudiante("Juan Pérez")
registrar_estudiante("María López")

consultar_estudiantes()
