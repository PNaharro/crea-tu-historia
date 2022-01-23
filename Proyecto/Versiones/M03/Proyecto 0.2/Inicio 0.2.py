#####IMPORT######
import Def
import pymysql
conn=pymysql.connect(host="20.73.187.218",user="prius",password="P@ssw0rd",db="proyecto")
####Menus########
menu_principal = ("Iniciar Sesion", "Crear Usuario", "Repetir Aventura", "Reportes", "Salir")
#####CODIGO######
def cabecera():
    print("*" * 126)
    banner = print(
        "    ####   ######   #######    ##              ######   ##   ##           ######   ######    #####   ######    ####      ##",
        "\n",
        "  ##  ##   ##  ##   ##   #   ####             # ## #   ##   ##            ##  ##   ##  ##  ##   ##   ##  ##    ##      ####",
        "\n",
        " ##        ##  ##   ## #    ##  ##              ##     ##   ##            ##  ##   ##  ##  ##   ##   ##  ##    ##     ##  ##",
        "\n",
        " ##        #####    ####    ##  ##              ##     ##   ##            #####    #####   ##   ##   #####     ##     ##  ##",
        "\n",
        " ##        ## ##    ## #    ######              ##     ##   ##            ##       ## ##   ##   ##   ##        ##     ######",
        "\n",
        "  ##  ##   ##  ##   ##   #  ##  ##              ##     ##   ##            ##       ##  ##  ##   ##   ##        ##     ##  ##",
        "\n",
        "   ####   #### ##  #######  ##  ##             ####     #####            ####     #### ##   #####   ####      ####    ##  ##")
    print("")
    print("                         ##   ##   ####     #####   ######    #####   ######    ####      ##")
    print("                         ##   ##    ##     ##   ##  # ## #   ##   ##   ##  ##    ##      ####")
    print("                         ##   ##    ##     #          ##     ##   ##   ##  ##    ##     ##  ##")
    print("                         #######    ##      #####     ##     ##   ##   #####     ##     ##  ##")
    print("                         ##   ##    ##          ##    ##     ##   ##   ## ##     ##     ######")
    print("                         ##   ##    ##     ##   ##    ##     ##   ##   ##  ##    ##     ##  ##")
    print("                         ##   ##   ####     #####    ####     #####   #### ##   ####    ##  ##")
    print("*" * 126)
while True:
    cabecera()
    opc = Def.menu(menu_principal)
    if opc == 1:
        while True:
            user = input("Dime tu usuario: ")
            password = input("Dime tu constraseña: ")
            if Def.checkUserbdd(user, password) == 1:
                print("Usuario identificado")
                break
            elif Def.checkUserbdd(user, password) == 0:
                print("Usuario o contraseña incorrecto/s")
            elif Def.checkUserbdd(user, password) == -1:
                print("Usuario o contraseña incorrecto/s")

    elif opc == 2:
        print(Def.insertUser())
    elif opc == 3:
        print(3)
    elif opc == 4:
        print(4)
    if opc == 5:
        print("Saliendo...")
        break