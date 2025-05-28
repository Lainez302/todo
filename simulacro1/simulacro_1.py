students = {
    "1": {" Name": "Alexander", "Age": 18, "Note": 5.0},
    "2": {" Name": "Jhonatan", "Age": 24, "Note": 4.2},
    "3": {" Name": "Tomas", "Age": 19, "Note": 3.7},
    "4": {" Name": "Cristian", "Age": 21, "Note": 2.9},
    "5": {" Name": "Antonio", "Age": 23, "Note": 1.5}
}

def AddSt():
    print("\n     AÑADIR ESTUDIANTE     ")
    while True:
        ID = input("Ingrese el ID del estudiante: ")
        if ID in students:
            print(f"Estudiante con ID {ID} ya está en la lista.")
        else:

            Name = input("Ingrese el nombre completo del estudiante: ")
            Age = int(input("Ingrese la edad del estudiante: "))
            Note = float(input("Ingrese la nota del estudiante: "))
            students[ID] = {'Name': Name, 'Age': Age, 'Note': Note}
            print(f"\nEstudiante con ID '{ID}' llamado {Name}")
            print(students)
            print("agrego correctamente el usuario")
            break
        
    
while True:
    print("\n 1) agregar \n 2) buscar: \n número de identificación: \n nota: ")
    opcion= input("ingrese una opcion")

    if opcion == "1":
        AddSt()


        
     
