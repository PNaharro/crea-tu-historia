inicio = "1)Login\n2)Create User\n3)Replay Adventure\n4)Reports\n5)Exit"
banner = print("    ####   ######   #######    ##              ######   ##   ##           ######   ######    #####   ######    ####      ##","\n","  ##  ##   ##  ##   ##   #   ####             # ## #   ##   ##            ##  ##   ##  ##  ##   ##   ##  ##    ##      ####","\n"," ##        ##  ##   ## #    ##  ##              ##     ##   ##            ##  ##   ##  ##  ##   ##   ##  ##    ##     ##  ##","\n"," ##        #####    ####    ##  ##              ##     ##   ##            #####    #####   ##   ##   #####     ##     ##  ##","\n"," ##        ## ##    ## #    ######              ##     ##   ##            ##       ## ##   ##   ##   ##        ##     ######","\n","  ##  ##   ##  ##   ##   #  ##  ##              ##     ##   ##            ##       ##  ##  ##   ##   ##        ##     ##  ##","\n","   ####   #### ##  #######  ##  ##             ####     #####            ####     #### ##   #####   ####      ####    ##  ##")
print("")
print("                         ##   ##   ####     #####   ######    #####   ######    ####      ##")
print("                         ##   ##    ##     ##   ##  # ## #   ##   ##   ##  ##    ##      ####")
print("                         ##   ##    ##     #          ##     ##   ##   ##  ##    ##     ##  ##")
print("                         #######    ##      #####     ##     ##   ##   #####     ##     ##  ##")
print("                         ##   ##    ##          ##    ##     ##   ##   ## ##     ##     ######")
print("                         ##   ##    ##     ##   ##    ##     ##   ##   ##  ##    ##     ##  ##")
print("                         ##   ##   ####     #####    ####     #####   #### ##   ####    ##  ##")

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
