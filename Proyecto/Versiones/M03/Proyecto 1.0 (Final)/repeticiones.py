import pymysql
import Def
conn = pymysql.connect(host="20.73.187.218", user="prius", password="P@ssw0rd", db="proyecto")
cur = conn.cursor()

def repeticiones():
    while True:
        rep = Def.getFormatedReAdventures()
        if rep == "0":
            break
        if not rep.isdigit():
            print("Caracter incorecto")
        else:
            query = f"select * from game"
            cur.execute(query)
            all = cur.fetchall()
            query = f"select id_aventura, nombre_aventura from aventura"
            cur.execute(query)
            saurce = cur.fetchall()
            query = f"select * from repeticiones"
            cur.execute(query)
            paso = cur.fetchall()
            query = f"select id_paso, paso from pasos"
            cur.execute(query)
            x = cur.fetchall()
            query = f"select id_respuesta, respuesta from respuesta"
            cur.execute(query)
            resp = cur.fetchall()
            for n in saurce:
                for i in all:
                    if i[1] == n[0]:
                        a = Def.getHeader(str(n[1]))
            print(a)
            for i in all:
                if i[0] == int(rep):
                    for k in paso:
                        for j in x:
                            for q in resp:
                                if k[3] == int(rep):
                                    if k[1] == j[0] and k[2] is None:
                                        print(j[0], "-", Def.formatText(str(j[1]), 100))
                                        input()
                                        print(" #######    ###    #     #\n",
                                              "#           #     ##    #\n",
                                              "#           #     # #   #\n",
                                              "#####       #     #  #  #\n",
                                              "#           #     #   # #\n",
                                              "#           #     #    ##\n",
                                              "#          ###    #     #")
                                        input()
                                        break
                                    if k[1] == j[0]:
                                        if k[2] == q[0]:
                                            print(j[0], "-", Def.formatText(str(j[1]), 100), Def.get_characters()[i[3]],
                                                  ":")
                                            input()
                                            query = f"select * from respuesta where id_paso = '{k[1]}'"
                                            cur.execute(query)
                                            A = cur.fetchall()
                                            for z in A:
                                                print(z[0], "-", z[1])
                                            input()
                                            print(q[0], "-", q[1])
                                            input()

        break