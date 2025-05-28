lista = [1, 4, 3, 10, 6]
busca = int(input("ingresa el numero que buscas: "))

if busca in lista:
    pocision = lista.index(busca)
    print(f"el numero{busca} esta en la pocision: {pocision}.")
else:
    print(f"numero {busca} no esta en la lista")