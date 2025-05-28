def mayoria ():
    Edad=int(input("Ingrese su edad: "))
    if Edad>=18:
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad")
    

def Tempe():
    Temp=int(input("Ingrese la temperatura en celcius: "))
    GF=(Temp*(9/5))+32
    print(f"La temperatura en Fahrenheit es: {GF}")    



def area():
    Altura=int(input("Ingrese la altura del triangulo: "))
    Base=int(input("Ingrese la base del triangulo: "))

    AreaT=(Base*Altura)/2
    print(f"El area del cuadrado es: {AreaT} ")


Lista=[1,2,3,4,5,6,7]
def Mayor():
    
    while True:
        Numero=int(input("Ingrese un número a la lista: "))
        Lista.append(Numero)
        Continuar=int(input("Desea agregar otro número a la lista 1 (si) o 2 (no) "))
        if Continuar!=1:
            break
        
    print(Lista)    