import pymysql

conn = pymysql.connect(host="20.73.187.218", user="prius", password="P@ssw0rd", db="proyecto")
cur = conn.cursor()

def formatText(texto,longitud):
    y = ""
    z = ""
    for i in texto:
        y += i
        if len(y) >= longitud and i.isspace():
            z += y + "\n".ljust(6)
            y = ""
    z += y
    return z

aventura = input("Dime que aventura queires jugar: ")
num_paso = 1
while True:
    query = f"select * from pasos where num_paso = '{num_paso}'"
    cur.execute(query)
    pasos = cur.fetchone()
    print(pasos[0],"-",formatText(pasos[1],100))
    if pasos[4] == 0:
        print(" #######    ###    #     #\n",
              "#           #     ##    #\n",
              "#           #     # #   #\n",
              "#####       #     #  #  #\n",
              "#           #     #   # #\n",
              "#           #     #    ##\n",
              "#          ###    #     #")
        break
    input()
    query = f"select * from respuesta where id_paso = '{pasos[0]}'"
    cur.execute(query)
    respuesta = cur.fetchall()
    lista = []
    for i in respuesta:
        print(i[0],"-",i[1])
        lista.append(i[0])

    while True:
        corrector = 0
        opc = input("Elije un camino: ")
        for i in lista:
            if opc.isalnum() == False or opc.isalpha() or int(opc) != i :
                corrector = 0
            else:
                corrector = 1
                break
        if corrector == 1:
            break
        else:
            print("Introduce un valor valido")
    num_paso = f"select num_respuesta from respuesta where id_respuesta = '{opc}'"
    cur.execute(num_paso)
    num_paso = cur.fetchall()
    for i in num_paso:
        num_paso = i[0]
    if opc == "+":
        break
