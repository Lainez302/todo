usuario = int(input("Digite un numero:"))
usuario2 = int(input("Digite el segundo numero:"))
usuario3 = int(input("Digite el tercer numero:"))

if usuario < usuario2 and usuario < usuario3:
    print("El primer numero es el menor")
elif usuario2 < usuario and usuario2 < usuario3:
    print("El segundo numero es el menor")
elif usuario3 < usuario and usuario3 < usuario2:
    print("El tercer numero es el menor")
else:
    print("Los numeros son iguales")

  