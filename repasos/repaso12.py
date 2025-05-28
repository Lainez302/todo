frutas = ["manzana", "pera", "uva", "melon", "arroz"]
print("lista de frutas", frutas)
eliminar = input("ingresa la fruta que quieres eliminar: ")
if eliminar in frutas:
    frutas.remove(eliminar)
    print("fruta eliminada", frutas)

else:
    print("la fruta no se encuentra en la lista")