python
# Este programa gestiona información básica de una lista de estudiantes

# Creamos una lista vacía para almacenar la información de los estudiantes
lista_estudiantes = []

# Solicitamos al usuario que ingrese los datos de los estudiantes
while True:
    nombre = input("Ingresa el nombre del estudiante (o 'salir' para terminar): ")
    if nombre.lower() == "salir":
        break
    
    edad = int(input("Ingresa la edad del estudiante: "))
    promedio = float(input("Ingresa el promedio del estudiante: "))
    activo = input("¿El estudiante está activo? (si/no): ").lower() == "si"
    
    # Creamos un diccionario con los datos del estudiante
    estudiante = {
        "nombre": nombre,
        "edad": edad,
        "promedio": promedio,
        "activo": activo
    }
    
    # Agregamos el diccionario a la lista de estudiantes
    lista_estudiantes.append(estudiante)

# Mostramos la información de los estudiantes
print("\nInformación de los estudiantes:")
for estudiante in lista_estudiantes:
    print("Nombre:", estudiante["nombre"])
    print("Edad:", estudiante["edad"])
    print("Promedio:", estudiante["promedio"])
    print("Activo:", estudiante["activo"])
    print("-" * 30)

# Datos de ejemplo
estudiante1 = {
    "nombre": "Laura",
    "edad": 21,
    "promedio": 9.8,
    "activo": True
}
estudiante2 = {
    "nombre": "Pedro",
    "edad": 20,
    "promedio": 8.3,
    "activo": True
}
estudiante3 = {
    "nombre": "Ana",
    "edad": 19,
    "promedio": 7.5,
    "activo": False
}

# Agregamos los datos de ejemplo a la lista de estudiantes
lista_estudiantes.append(estudiante1)
lista_estudiantes.append(estudiante2)
lista_estudiantes.append(estudiante3)

# Mostramos la información de los estudiantes nuevamente
print("\nInformación de los estudiantes (con nuevos datos de ejemplo):")
for estudiante in lista_estudiantes:
    print("Nombre:", estudiante["nombre"])
    print("Edad:", estudiante["edad"])
    print("Promedio:", estudiante["promedio"])
    print("Activo:", estudiante["activo"])
    print("-" * 30)


En este nuevo programa, hemos agregado datos de ejemplo para tres estudiantes diferentes: Laura, Pedro y Ana.
