print("*"*126)
banner = print("    ####   ######   #######    ##              ######   ##   ##           ######   ######    #####   ######    ####      ##","\n","  ##  ##   ##  ##   ##   #   ####             # ## #   ##   ##            ##  ##   ##  ##  ##   ##   ##  ##    ##      ####","\n"," ##        ##  ##   ## #    ##  ##              ##     ##   ##            ##  ##   ##  ##  ##   ##   ##  ##    ##     ##  ##","\n"," ##        #####    ####    ##  ##              ##     ##   ##            #####    #####   ##   ##   #####     ##     ##  ##","\n"," ##        ## ##    ## #    ######              ##     ##   ##            ##       ## ##   ##   ##   ##        ##     ######","\n","  ##  ##   ##  ##   ##   #  ##  ##              ##     ##   ##            ##       ##  ##  ##   ##   ##        ##     ##  ##","\n","   ####   #### ##  #######  ##  ##             ####     #####            ####     #### ##   #####   ####      ####    ##  ##")
print("")
print("                         ##   ##   ####     #####   ######    #####   ######    ####      ##")
print("                         ##   ##    ##     ##   ##  # ## #   ##   ##   ##  ##    ##      ####")
print("                         ##   ##    ##     #          ##     ##   ##   ##  ##    ##     ##  ##")
print("                         #######    ##      #####     ##     ##   ##   #####     ##     ##  ##")
print("                         ##   ##    ##          ##    ##     ##   ##   ## ##     ##     ######")
print("                         ##   ##    ##     ##   ##    ##     ##   ##   ##  ##    ##     ##  ##")
print("                         ##   ##   ####     #####    ####     #####   #### ##   ####    ##  ##")
print("*"*126)
menu_principal = "1)Iniciar Sesion\n2)Crear Usuario\n3)Repetir Aventura\n4)Reportes\n5)Salir"

def menu(tupla):
    while True:
        cadena = ""
        for i in range(len(tupla)):
            cadena += str(i+1)+")"+tupla[i]+"\n"
        print(cadena)
    opc = input("Opcion:")
    if not opc.isdigit():
        print("Opcion invalida")
    elif int(opc) < 1 or int(opc) > len(tupla):
        print("Opcion invalida")
    else:
        return int(opc)
    # opcion = menu(tupla)
    # print(f"Has elegido {opcion}")
    # if opcion == 1:     menu(tupla1)
    # elif opcion == 2:     menu(tupla2)
    # elif opcion == 3:     menu(tupla3)