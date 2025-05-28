edad  = int(input("dime tu edad"))

if edad < 12:
    print("eres un niño")
elif edad >12 and edad <17:
    print("eres un adolecente")

elif edad >= 18 and edad <60:
    print("eres un adulto")

else:
    print("eres un viejo")
    