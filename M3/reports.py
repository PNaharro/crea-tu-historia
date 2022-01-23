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
#####CODIGO######
while True:
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
            adv = Def.getFormatedAdventures()
            print(adv)
            aventura = Def.get_table("aventura")
            if adv == "0":
                break
            else:
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

            break


    elif opc == 2:
        print(Def.insertUser())
    elif opc == 3:
        print(3)
    elif opc == 4:
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
                print(Def.getHeaderForTableFromTuples2(("ID AVENTURA - NOMBRE", "ID PASO - DESCRIPCION", "ID RESPUESTA - DESCRIPCION", "NUMERO DE VECES SELECCIONADA"), (0, 25, 43, 31), "Respuestas más usadas"))
                query = f"select concat(a.id_aventura,' - ', a.nombre_aventura), concat(p.id_paso,' - ', p.paso),concat( r.id_respuesta,' - ', r.respuesta), count(re.id_respuesta) from aventura a inner join pasos p on p.id_aventura=a.id_aventura inner join respuesta r on r.id_paso=p.id_paso inner join repeticiones re on re.id_respuesta=r.id_respuesta group by re.id_respuesta;"

                cur.execute(query)
                x = cur.fetchall()

                for i in x:
                    texto1 = i[0]
                    texto2 = i[1]
                    texto3 = i[2]
                    texto4 = str(i[3])
                    tupla = (texto1, texto2, texto3, texto4)
                    size = (25, 38, 29, 20)
                    print(Def.getFormatedBodyColumns(tupla, size, margin=2))
                input()

            if opc == 2:
                print(Def.getHeadeForTableFromTuples(("Nombre de usuario", "Partidas Jugadas"), (0, 50, 50),
                                                     ("Player With more games played")))
                conn = pymysql.connect(host="20.73.187.218", user="prius", password="P@ssw0rd", db="proyecto")
                cur = conn.cursor()
                sus = conn.cursor()
                query = f"select * from usuarios"
                cur.execute(query)
                usu = cur.fetchall()
                usuario = {}
                for i in usu:
                    a = i[1]
                    query = f"select id_usu from usuarios where nombre = '{a}'"
                    cur.execute(query)
                    x = cur.fetchall()
                    x = x[0][0]
                    query2 = f"select count(idgame) from game where id_usuario = '{x}'"
                    sus.execute(query2)
                    y = sus.fetchall()
                    y = y[0][0]
                    print(str(a).ljust(50), str(y).rjust(0))
            if opc == 3:
                while True:
                    User = input("Que usuario quieres ver: ")
                    if Def.userExists(User) == True:
                        print(Def.getHeadeForTableFromTuples(("Id aventura", "Name", "Date"), (0, 30, 30),
                                                             ("Games played by")))
                    cur = conn.cursor()
                    query2 = f"select * from game"
                    cur.execute(query2)
                    g = cur.fetchall()
                    if Def.userExists(User) == False:
                        print("este usuario no exisite")
                        print("Prueba con otro usuario")
                    elif Def.userExists(User) == True:
                        query = f"select id_usu from usuarios where nombre = '{User}'"
                        cur.execute(query)
                        x = cur.fetchall()
                        x = x[0][0]
                        for i in g:
                            if x == i[2]:
                                query = f"select id_aventura,nombre_aventura from aventura"
                                cur.execute(query)
                                aventura = cur.fetchall()
                                for j in aventura:
                                    if j[0] == i[1]:
                                        print(str(i[1]).ljust(36), str(j[1]).ljust(29), str(i[4]).ljust(30))
                                    break
                        input()
                        break
            if opc == 4:
                break
    if opc == 5:
        print("Saliendo...")
        break