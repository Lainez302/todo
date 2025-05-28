Historial=[]

Usuario={
    "Saldo": 0
    

}
while True:
    print("\n   Menú    ")
    print("1. Ver el saldo de su cuenta")
    print("2. Retirar dinero")
    print("3. Depositar dinero")
    print("4. Ver historial de movimientos")
    print("5. Salir")

    Accion = int(input("Seleccione una opción (1-5): "))
    if  Accion==1:
        print("\n   VER SALDO EN CUENTA   ")
        print(f"\n Saldo disponible: {Usuario["Saldo"]} ")
        movimiento={
            "Tipo": "Consulta de saldo"
        }
        Historial.append(movimiento)
    
    if Accion==2:
        print("\n   RETIRAR DINERO  ")
        Retirar=float(input("Ingrese la cantidad de dinero a retirar: "))
        Nuevo_Saldo=Usuario["Saldo"]-Retirar
        if Usuario["Saldo"]==0:
            print("No hay saldo en la cuenta")
            break

        print(f"Saldo retirado: {Retirar} ")
        print(f"Nuevo saldo: {Nuevo_Saldo}")
        movimiento={
            "Tipo": "Retiro",
            "Retiro": Retirar,
            "Nuevo Saldo": Nuevo_Saldo

        }
        Historial.append(movimiento)

    if Accion==3:
        print("\n   DEPOSITAR DINERO  ")
        Depositar=float(input("Ingrese la cantidad de dinero a depositar:  "))
        Nuevo_Saldo=Usuario["Saldo"]+Depositar
        

        print(f"Saldo depositado: {Depositar} ")
        print(f"Nuevo saldo: {Nuevo_Saldo} ")
        movimiento={
            "Tipo": "Deposito",
            "Deposito": Depositar,
            "Nuevo Saldo": Nuevo_Saldo

        }
        Historial.append(movimiento)

    if Accion==4: 
        print("     HISTORIAL DE MOVIMIENTOS    ")
        print(Historial)




    if Accion==5:
        print("¡Adios!")
        break
