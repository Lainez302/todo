nota = int(input("ingresa lo que sacaste:"))
if nota < 5:
    print("perdiste")
elif nota >= 5 and nota < 7:
    print("pasaste")
elif nota >= 7 and nota <= 10:
    print("sobresaliente")
else:
    print("no valido")
