#####IMPORT######
import Def
import pymysql
conn=pymysql.connect(host="20.73.187.218",user="pnaharro",password="P@ssw0rd",db="proyecto")
####cursor#######
cur=conn.cursor()
sus = conn.cursor()
cur2 = conn.cursor()
sus2 = conn.cursor()
cur3 = conn.cursor()
sus3 = conn.cursor()
#####querys######
query1 = f"select id_aventura from aventura"
query2 = f"select nombre_aventura from aventura"
query3 = f"select id_paso from pasos"
query4 = f"select paso from pasos"
query5 = f"select id_respuesta from respuesta"
query6 = f"select respuesta from respuesta"
####ejecute######
cur.execute(query1)
sus.execute(query2)
cur2.execute(query3)
sus2.execute(query4)
cur3.execute(query5)
sus3.execute(query6)

quety_1 = cur.fetchall()
quety_2 = sus.fetchall()
query_3 = cur2.fetchall()
query_4 = sus2.fetchall()
query_5 = cur3.fetchall()
query_6 = sus3.fetchall()
####Menus########
menu_principal = ("Iniciar Sesion", "Crear Usuario", "Repetir Aventura", "Reportes", "Salir")
menu_report = ("Most used answer", "Play with more games played", "Games played by user", "Back")
#####FLAG######
Flag_Login = True
Flag_Logout = True
#####CODIGO######
while Flag_Login:
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
    opc = Def.menu(menu_principal)
    if opc == 1:
        while True:
            user = input("Dime tu usuario: ")
            password = input("Dime tu constraseña: ")
            if Def.checkUserbdd(user, password) == 1:
                print("Usuario identificado")
                break
            elif Def.checkUserbdd(user, password) == 0:
                print("Constraseña incorrecta")
            elif Def.checkUserbdd(user, password) == -1:
                print("Usuario inexistente")

        while True:
            print("Selecciona historia")
            Def.getFormatedAdventures()
            adv = input("Opcion:")
            aventura = Def.get_table("aventura")

            for i in range(len(aventura)):
                if int(adv) == int(aventura[1][i][0]):
                    print(Def.getHeader(aventura[1][i][1]))
                    cadena = "Aventura:".ljust(20) + str(aventura[1][i][1]).rjust(20) + "\n" + "Descripcion:".ljust(
                        26) + str(aventura[1][i][9]).rjust(30)
                    print(cadena)
                    input("Pulsa para continuar ")
                    while True:
                        print("=" * 20 + "Personajes" + "=" * 20)
                        print("Elije tu personaje")
                        for i in Def.get_characters():
                            cadena = str(i).rjust(2) + ")".ljust(5) + str(Def.get_characters()[i])
                            print(cadena)
                        select_char = input("Opcion: ")
                        if not select_char.isdigit():
                            print("Opcion incorrecta")
                        elif select_char == "0":
                            print("Opcionn incorrecta")
                        elif not int(select_char) >= 1 or int(select_char) <=  len(Def.get_characters()):
                            print("Has seleccionado a {}".format(Def.get_characters()[int(select_char)]))
                            input()
                            break
                        else:
                            print("Opcion incorrecta")
                elif adv == "0":
                    break
            break

    if opc == 2:
        print(2)
    if opc == 3:
        print(3)
    if opc == 4:
        while True:
            print("*" * 126)
            print("                         ######")
            print("                         #     # ###### #####   ####  #####  #####")
            print("                         #     # #      #    # #    # #    #   #   ")
            print("                         ######  #####  #    # #    # #    #   #   ")
            print("                         #   #   #      #####  #    # #####    #   ")
            print("                         #    #  #      #      #    # #   #    #   ")
            print("                         #     # ###### #       ####  #    #   # ")
            print("*" * 126)
            opc = Def.menu(menu_report)
            if opc == 1:
                print(1)
                cadena = "*"*55+"Most used answer"+"*"*55+"\n"+"Id Aventura - Nombre".ljust(31)+\
                         "ID paso - Descricion".rjust(20)+"ID respuesta - Descripcion".rjust(44)+\
                         "Numero veces seleccionado".rjust(31)+"\n"+"*"*126
                print(cadena)
                for i in range(len(quety_1)):
                    for j in range(len(query_3)):
                        for h in range(len(query_5)):
                            cadena1 = str(quety_1[i]).strip("('',)"), "-", str(quety_2[i]).strip("('',)") + "".ljust(31)
                            cadena2 = str(query_3[i]).strip("('',)"), "-", str(query_4[i]).strip("('',)") + "".rjust(20)
                            cadena3 = str(query_5[i]).strip("('',)"), "-", str(query_6[i]).strip("('',)")+"".rjust(44)
                            print(cadena1 + cadena2 + cadena3)

            if opc == 2:
                print(Def.getHeadeForTableFromTuples(("Nombre de usuario","Partidas Jugadas"),(0,50,50),("Player With more games played")))
                query = f""
            if opc == 3:
                while True:
                    User = input("Que usuario quieres ver: ")
                    if Def.userExists(User) == True:
                        print(Def.getHeadeForTableFromTuples(("Id aventura", "Name","Date"), (0, 30, 30),("Games played by")))
                        break
                    if Def.userExists(User) == False:
                        print("este usuario no exisite")
                        print("Prueba con otro usuario")
            if opc == 4:
                print(4)
                Menu_reports = False
    if opc == 5:
        print(5)
        Menu_Inicio = False




while Flag_Logout:
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
    opc = Def.menu(menu_principal)
    if opc == 1:
        while True:
            user = input("Dime tu usuario: ")
            password = input("Dime tu constraseña: ")
            if Def.checkUserbdd(user, password) == 1:
                print("Usuario identificado")
                break
            elif Def.checkUserbdd(user, password) == 0:
                print("Constraseña incorrecta")
            elif Def.checkUserbdd(user, password) == -1:
                print("Usuario inexistente")

        Flag_Login = False
        Flag_Logout = True

        while True:
            print("Selecciona historia")
            Def.getFormatedAdventures()
            adv = input("Opcion:")
            aventura = Def.get_table("aventura")

            for i in range(len(aventura)):
                if int(adv) == int(aventura[1][i][0]):
                    print(Def.getHeader(aventura[1][i][1]))
                    cadena = "Aventura:".ljust(20) + str(aventura[1][i][1]).rjust(20) + "\n" + "Descripcion:".ljust(
                        26) + str(aventura[1][i][9]).rjust(30)
                    print(cadena)
                    input("Pulsa para continuar ")
                    while True:
                        print("=" * 20 + "Personajes" + "=" * 20)
                        print("Elije tu personaje")
                        for i in Def.get_characters():
                            cadena = str(i).rjust(2) + ")".ljust(5) + str(Def.get_characters()[i])
                            print(cadena)
                        select_char = input("Opcion: ")
                        if not select_char.isdigit():
                            print("Opcion incorrecta")
                        elif select_char == "0":
                            print("Opcionn incorrecta")
                        elif not int(select_char) >= 1 or int(select_char) <=  len(Def.get_characters()):
                            print("Has seleccionado a {}".format(Def.get_characters()[int(select_char)]))
                            input()
                            break
                        else:
                            print("Opcion incorrecta")
                elif adv == "0":
                    break
            break

    if opc == 2:
        print(2)
    if opc == 3:
        print(3)
    if opc == 4:
        while True:
            print("*" * 126)
            print("                         ######")
            print("                         #     # ###### #####   ####  #####  #####")
            print("                         #     # #      #    # #    # #    #   #   ")
            print("                         ######  #####  #    # #    # #    #   #   ")
            print("                         #   #   #      #####  #    # #####    #   ")
            print("                         #    #  #      #      #    # #   #    #   ")
            print("                         #     # ###### #       ####  #    #   # ")
            print("*" * 126)
            opc = Def.menu(menu_report)
            if opc == 1:
                print(1)
                cadena = "*"*55+"Most used answer"+"*"*55+"\n"+"Id Aventura - Nombre".ljust(31)+\
                         "ID paso - Descricion".rjust(20)+"ID respuesta - Descripcion".rjust(44)+\
                         "Numero veces seleccionado".rjust(31)+"\n"+"*"*126
                print(cadena)
                for i in range(len(quety_1)):
                    for j in range(len(query_3)):
                        for h in range(len(query_5)):
                            cadena1 = str(quety_1[i]).strip("('',)"), "-", str(quety_2[i]).strip("('',)") + "".ljust(31)
                            cadena2 = str(query_3[i]).strip("('',)"), "-", str(query_4[i]).strip("('',)") + "".rjust(20)
                            cadena3 = str(query_5[i]).strip("('',)"), "-", str(query_6[i]).strip("('',)")+"".rjust(44)
                            print(cadena1 + cadena2 + cadena3)

            if opc == 2:
                print(Def.getHeadeForTableFromTuples(("Nombre de usuario","Partidas Jugadas"),(0,50,50),("Player With more games played")))
                query = f""
            if opc == 3:
                while True:
                    User = input("Que usuario quieres ver: ")
                    if Def.userExists(User) == True:
                        print(Def.getHeadeForTableFromTuples(("Id aventura", "Name","Date"), (0, 30, 30),("Games played by")))
                        break
                    if Def.userExists(User) == False:
                        print("este usuario no exisite")
                        print("Prueba con otro usuario")
            if opc == 4:
                print(4)
                Menu_reports = False
    if opc == 5:
        print(5)
        Menu_Inicio = False