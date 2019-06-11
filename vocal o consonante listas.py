vocal=["a","A","E","e","i","I","O","o","U","u"]
letra=input("Ingresa una letra y te dire si es vocal o consonate")
for elem in vocal:
    if letra == elem:
        print("Es una vocal")
    else:
        print("Es una consonate")

