def menu(tupla):
    while True:
        cadena = ""
        for i in range(len(tupla)):
            cadena += "".ljust(50)+(str(i+1)+")"+tupla[i]+"\n")
        print(cadena)
        return
def revision(tupla):
        opc = input("Opcion:")
        if not opc.isdigit():
            print("Opcion invalida")
        elif int(opc) < 1 or int(opc) > len(tupla):
            print("Opcion invalida")
        else:
            return int(opc)
