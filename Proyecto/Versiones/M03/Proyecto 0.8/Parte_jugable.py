import pymysql
import Def
conn = pymysql.connect(host="20.73.187.218", user="prius", password="P@ssw0rd", db="proyecto")
cur = conn.cursor()

def sel_aventura(user):
    while True:
        while True:
            adv = Def.getFormatedAdventures()
            aventura = Def.get_table("aventura")
            if not adv.isdigit():
                print("Valor incorrecto")
            elif adv == "0":
                break
            elif adv == "2" or adv == "3" or adv == "4" or adv == "5":
                print("EN DESARROLLO")
                input()
            elif adv != "1":
                print("Valor incorrecto")
            else:
                break

        for i in range(len(aventura)):
            if int(adv) == int(aventura[1][i][0]):
                print(Def.getHeader(aventura[1][i][1]))
                cadena = "Aventura:".ljust(20) + str(aventura[1][i][1]).rjust(20) + "\n" + "Descripcion:".ljust(
                    26) + str(aventura[1][i][7]).rjust(30)
                print(cadena)
                input("Pulsa para continuar ")
                while True:
                    print("=" * 20 + "Personajes" + "=" * 20)
                    print("Elije tu personaje")
                    for i in Def.get_characters():
                        cadena = str(i).rjust(2) + ")".ljust(5) + str(Def.get_characters()[i])
                        print(cadena)
                    select_char = input("Opcion (Pulsa 0 para salir):")
                    if not select_char.isdigit():
                        print("Opcion incorrecta")
                    elif select_char == "0":
                        break
                    elif not int(select_char) >= 1 or int(select_char) <= len(Def.get_characters()):
                        print("Has seleccionado a {}".format(Def.get_characters()[int(select_char)]))
                        input()
                        user = f"select id_usu from usuarios where nombre = '{user}'"
                        cur.execute(user)
                        user = cur.fetchall()
                        query = f"insert into game (id_aventura, id_usuario, id_personaje, fechacreacion, usuariocreacion) values ('{adv}','{user[0][0]}','{select_char}',current_timestamp(),user());"
                        cur.execute(query)
                        conn.commit()
                        break
                    else:
                        print("Opcion incorrecta")
            elif adv == "0":
                break
        break


    num_paso = adv
    while True:
        if adv == "0":
            break
        if select_char == "0":
            break
        query = f"select * from pasos where num_paso = '{num_paso}'"
        cur.execute(query)
        pasos = cur.fetchone()
        print(pasos[0],"-",Def.formatText(pasos[1],100),Def.get_characters()[int(select_char)],":")
        if pasos[4] == 0:
            print(" #######    ###    #     #\n",
                  "#           #     ##    #\n",
                  "#           #     # #   #\n",
                  "#####       #     #  #  #\n",
                  "#           #     #   # #\n",
                  "#           #     #    ##\n",
                  "#          ###    #     #")

            query = f"insert into repeticiones (id_paso,id_game,usuariocreacion) values ('{pasos[0]}',(select max(idgame) from game),user());"
            cur.execute(query)
            conn.commit()
            input()
            break
        input()
        query = f"select * from respuesta where id_paso = '{pasos[0]}'"
        cur.execute(query)
        respuesta = cur.fetchall()
        lista = []
        for i in respuesta:
            print(i[0], "-", i[1])
            lista.append(i[0])

        while True:
            corrector = 0
            opc = input("Elije un camino (Pulsa 0 para salir): ")
            print("")
            if opc == "0":
                break
            for i in lista:
                if opc != str(i):
                    corrector = 0
                else:
                    corrector = 1
                    break
            if corrector == 1:
                query = f"insert into repeticiones (id_paso,id_respuesta,id_game,usuariocreacion) values ('{int(pasos[0])}','{int(opc)}',(select max(idgame) from game),user());"
                cur.execute(query)
                conn.commit()
                break
            else:
                print("Introduce un valor valido")
        num_paso = f"select num_respuesta from respuesta where id_respuesta = '{opc}'"
        cur.execute(num_paso)
        num_paso = cur.fetchall()
        for i in num_paso:
            num_paso = i[0]
        if opc == "0":
            break