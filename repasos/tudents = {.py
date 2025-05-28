tudents = {
    "100": {"Name": "Juan", "Age": 17, "Note": 3.0},
    "200": {"Name": "Esteban", "Age": 19, "Note": 5.0},
    "300": {"Name": "Johan", "Age": 22, "Note": 4.0},
    "400": {"Name": "Daniel", "Age": 18, "Note": 2.0},
    "500": {"Name": "Cristian", "Age": 24, "Note": 2.8}
}

def AddSt():
    print("     AÑADIR ESTUDIANTE     ")
    while True:
        ID = input("Ingrese el ID del estudiante: ")
        if ID in Students:
            print(f"Estudiante con ID {ID} ya está en la lista.")
        else:
            Name = input("Ingrese el nombre completo del estudiante: ")
            Age = int(input("Ingrese la edad del estudiante: "))
            Note = float(input("Ingrese la nota del estudiante: "))
            Students[ID] = {'Name': Name, 'Age': Age, 'Note': Note}
            print(f"Estudiante con ID '{ID}' llamado {Name} añadido correctamente.")
        print("\nLista actualizada de estudiantes:")
        PrintL()
        conti = input("¿Desea ingresar otro estudiante? (si/no): ").lower()
        if conti == "no":
            break

def PrintL():
    print("\n     LISTA DE ESTUDIANTES       ")
    for ID, data in Students.items():
        print(f"ID: {ID}, Nombre: {data['Name']}, Edad: {data['Age']}, Nota: {data['Note']}")

# Función para buscar estudiantes
def SearchSt():
    print("\n     BUSCAR ESTUDIANTE      ")
    while True:
        select = input("Buscar por (ID/Nombre): ").lower()
        if select == 'id':
            id_st = input("Ingrese el ID del estudiante: ")
            if id_st in Students:
                stu = Students[id_st]
                print("\nEstudiante encontrado:")
                print(f"ID: {id_st}, Nombre: {stu['Name']}, Edad: {stu['Age']}, Nota: {stu['Note']}")
            else:
                print("No se encontró un estudiante con ese ID.")
        elif select == 'nombre':
            name_search = input("Ingrese el nombre completo o parcial del estudiante: ").lower()
            found = False
            for id_st, stu in Students.items():
                if name_search in stu['Name'].lower():
                    print(f"\nEstudiante encontrado:")
                    print(f"ID: {id_st}, Nombre: {stu['Name']}, Edad: {stu['Age']}, Nota: {stu['Note']}")
                    found = True
            if not found:
                print("No se encontró un estudiante con ese nombre.")
        conti = input("¿Desea buscar otro estudiante? (si/no): ").lower()
        if conti == "no":
            break

# Función para modificar nota
def ModSt():
    print("\n     MODIFICAR NOTA DE ESTUDIANTE     ")
    while True:
        ID = input("Ingrese el ID del estudiante: ")
        if ID in Students:
            note_mod = Students[ID]
            print("\nInformación actual:")
            print(f"ID: {ID}, Nombre: {note_mod['Name']}, Edad: {note_mod['Age']}, Nota: {note_mod['Note']}")
            new_value = float(input("Ingrese la nueva nota: "))
            note_mod["Note"] = new_value
            print("Nota actualizada con éxito.")
        else:
            print("ID no encontrado.")
        conti = input("¿Desea modificar otra nota? (si/no): ").lower()
        if conti == "no":
            break

# Función para eliminar estudiante
def DelStudent():
    print("\n     ELIMINAR ESTUDIANTE      ")
    while True:
        id_st = input("Ingrese el ID del estudiante que desea eliminar: ")
        if id_st in Students:
            stu = Students[id_st]
            print(f"Estudiante encontrado: {stu['Name']}, Nota: {stu['Note']}")
            confirm = input(f"¿Desea eliminar al estudiante con ID {id_st}? (si/no): ").lower()
            if confirm == "si":
                del Students[id_st]
                print("Estudiante eliminado con éxito.")
        else:
            print("ID no encontrado.")
        conti = input("¿Desea eliminar otro estudiante? (si/no): ").lower()
        if conti == "no":
            break

# Función para calcular promedio de notas
def PromNotes():
    print("\n     PROMEDIO DE NOTAS     ")
    if not Students:
        print("No hay estudiantes registrados.")
        return
    total = sum(stu['Note'] for stu in Students.values())
    promedio = total / len(Students)
    print(f"El promedio de las notas es: {promedio:.2f}")
