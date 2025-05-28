lista = []

for i in range(5):
    num = int(input(f"ingrese un numero {i+1} : "))
    if num % 2 ==0:
        lista.append(num)
print(f"numeros pares{lista}: ")