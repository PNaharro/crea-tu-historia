import pymysql

conn = pymysql.connect(host="20.73.187.218", user="prius", password="P@ssw0rd", db="proyecto")
cur = conn.cursor()

query = f"select * from aventura"
cur.execute(query)
aventura = cur.fetchall()
query = f"select * from personajes"
cur.execute(query)
personajes = cur.fetchall()
adventures = {}
for i in aventura:
    adventures[i[0]] = {"Name": i[1], "Description": i[9], "characters": []}
    for j in personajes:
        adventures[i[0]]["characters"].append(j[0])
#print(adventures)

query = f"select * from personajes"
cur.execute(query)
characters = {}
personajes = cur.fetchall()
for i in personajes:
    characters[i[0]] = i[1]
#print(characters)

query = f"select num_paso from pasos"
cur.execute(query)
num_paso = []
num = cur.fetchall()
for i in num:
    num_paso.append(i)
num = str(num_paso[0]).strip("(,)")
#print(num)

###################################     FUNCIONES     #########################################################
#MUESTRA LOS USUSARIOS EN UN DICCIONARIO CON SUS CONTRASEÑAS E IDS
#######################################################################################################################
def getUsers():
    query = f"select * from usuarios"
    cur.execute(query)
    x = cur.fetchall()
    diccionario = {}
    for i in x:
        diccionario[i[1]] = {"contraseña":i[2],"id":i[0]}
    return  diccionario
#print(getUsers())
#######################################################################################################################
#MUESTRA LOS USUARIOS EN UNA LISTA, USUARIO E ID
#######################################################################################################################
def getUserIds():
    query = f"select * from usuarios"
    cur.execute(query)
    x = cur.fetchall()
    listausr = [[],[]]
    for i in x:
        listausr[0].append(i[1])
        listausr[1].append(i[0])
    return listausr
#print(getUserIds())
#######################################################################################################################
#COMPRUEBA SI EL USUARIO EXISTE EN LA BASE DE DATOS
#######################################################################################################################
def userExists(user):
    for i in getUsers():
        if user == i:
            return True
        else:
            return False
#user = input("Dime el usuario: ")
#print(userExists(user))
#######################################################################################################################
#COMPRUEVA SI LA PASW INSERTADA ES SEGURA
#######################################################################################################################
def checkPassword(password):
    if not len(password) >=8 and len(password) <= 12:
        return False
    may = 0
    min = 0
    num = 0
    c_esp = 0
    esp = 0
    for i in password:
        if i.isupper():
            may += 1
        elif i.islower():
            min += 1
        elif i.isnumeric():
            num += 1
        elif not i.isalnum():
            c_esp += 1
        if i.isspace():
            esp += 1
    if may == 0 or min == 0 or num == 0 or c_esp == 0 or esp >= 1:
        return False
    else:
        return True
#print(checkPassword("P@ssw0rd"))
#######################################################################################################################
#PONES UN USUARIO Y LA CONTRASEÑA RESPECTIVA DEL USUARIO Y LOS COMPRUEVA
#######################################################################################################################
def checkUserbdd(user,password):
    for i in getUsers():
        if user == i:
            if password == getUsers()[i]["contraseña"]:
                return 1
            else:
                return -1
        else:
            return 0
#user = input("Dime tu usuario: ")
#password = input("Dime tu constraseña: ")
#print(checkUserbdd(user,password))
#######################################################################################################################
#PONES EL NOMBRE DE LA TABLA DE LA BDD Y TE MUESTRA EN UNA TUPLA DE TUPLAS SU CONTENIDO
#######################################################################################################################
def get_table(tabla):
    query = f"select * from {tabla}"
    cur.execute(query)
    columnas = cur.description
    tupla = (())
    for i in columnas:
        tupla = tupla + i
        tupla = tupla[:-6]
    x = cur.fetchall()
    tuplafin = ((tupla),(x))
    return tuplafin
#tabla = input("Introduce el nombre de la tabla: ")
#print(get_table(tabla))
#######################################################################################################################
#COMPRUEBA SI EL USR CUMPLE LOS REQUISITOS
#######################################################################################################################
def checkUser(user):
    if len(user) < 6 or len(user) > 10 and user.isalnum() == False:
        return False
    else:
        return True
#user = input("Introduce un nombre de usuario: ")
#print(checkUser(user))
#######################################################################################################################
#CREA UNA CABECERA
#######################################################################################################################
def getHeader(text):
    x = (100-len(text))/2
    y = 100
    if len(text)%2!=0:
        y -= 1
    cadena = "*"*y +"\n" + "="*int(x) + text + "="*int(x) + "\n" + "*"*y
    return cadena
#print(getHeader("ESTO ACEPTA HASTA 100 CARACTERES"))
#######################################################################################################################
#PERMITE CREAR UN USUARIO EN LA BDD
#######################################################################################################################
def checkUserbdd_insertUser(user):
    for i in getUsers():
        if user == i:
            return 1
        else:
            return 0

def insertUser():
    confirmacion = "Usuario creado con exito"
    salir = "Saliendo"
    while True:
        user = input("\nPulsa 1 para salir...\nDime tu usuario: ")
        if user == "1":
            return salir
        elif checkUser(user) == False:
            print("El usuario no cumple con los requisitos")
        else:
            print("Usuario correcto")
            if checkUserbdd_insertUser(user) == 1:
                print("Este nombre de usuario ya existe en la base de datos")
            else:
                print("Este nombre no esta en la base de datos")
                break
    while True:
        password = input("\nPulsa 1 para salir...\nDime tu contraseña: ")
        if password == "1":
            return salir
        elif checkPassword(password) == False:
            print("La contraseña no cumple los requisitos")
        else:
            print("La contraseña cumple los requisitos")
            query = f"insert into usuarios (nombre, password, usuariocreacion) values ('{user}','{password}',user())"
            cur.execute(query)
            conn.commit()
            return confirmacion
#print(insertUser())
#######################################################################################################################
#DEVUELVE UN DICT CON LAS AVENTURAS
#######################################################################################################################
def get_adventures_with_chars():
    return adventures
#print(get_adventures_with_chars())
#######################################################################################################################
#DEVUELVE UN DICT CON LOS PERSONAJES
#######################################################################################################################
def get_characters():
    return characters
#print(get_characters())
#######################################################################################################################
#CUANDO EL TEXTO SUPERA LA LONGITUD, HACE UN ENTER
#######################################################################################################################
def formatText(texto,longitud):
    y = ""
    z = ""
    for i in texto:
        y += i
        if len(y) >= longitud and i.isspace():
            z += y + "\n"
            y = ""
    z += y
    return z
#print(formatText("texto de ejemplo",20))
#######################################################################################################################
#PERMITE CREAR UNA CABECERA COMPLETA
#######################################################################################################################
def getHeader_getHeadeForTableFromTuples(text):
    x = (104-len(text))/2
    y = 104
    if len(text)%2!=0:
        y -= 1
    cadena = "="*int(x) + text + "="*int(x)
    return cadena

def getHeadeForTableFromTuples(t_name_columns,t_size_columns,title):
    cadena = getHeader_getHeadeForTableFromTuples(title) + "\n"
    for i in t_name_columns:
            cadena += i.rjust(t_size_columns[0])
            t_size_columns = t_size_columns[1:]
    cadena += "\n" + "*" * 104
    return cadena
#print(getHeadeForTableFromTuples(("Columna1","Columna2","Columna3","Columna4"),(0,30,50,10),"Texto de ejemplo"))
#######################################################################################################################

#######################################################################################################################
def formatText_getFormatedAdventures(texto,longitud):
    y = ""
    z = ""
    for i in texto:
        y += i
        if len(y) >= longitud and i.isspace():
            z += y + "\n".ljust(58)
            y = ""
    z += y
    return z
#print(formatText_getFormatedAdventures("texto de ejemplo",20))
def getFormatedAdventures():
    cadena = getHeadeForTableFromTuples(("Id Aventura","Aventura","Descripcion"),(0,13,44),"Adventures")
    print(cadena)
    x = 0

    while True:
        try:
            for i in get_adventures_with_chars():
                print(str(i + x).ljust(15), get_adventures_with_chars()[i + x]["Name"].ljust(40),
                      formatText_getFormatedAdventures(get_adventures_with_chars()[i + x]["Description"], 40))
                if i == 3:
                    break
                if x == 3 and i == 2:
                    break
            adv = input("opcion: ")
            if adv == "0":
                break
            elif adv == "+":
                x += 3
            elif adv == "-":
                x -= 3
        except:
          x = 0
    return adv
#######################################################################################################################
#CREA UN MENU AUTOMATICAMENTE
#######################################################################################################################
def menu(tupla):
    while True:
        cadena = ""
        for i in range(len(tupla)):
            cadena += "".ljust(50)+(str(i+1)+")"+tupla[i]+"\n")
        print(cadena)
        opc = input("Opcion:")
        if not opc.isdigit():
            print("Opcion invalida")
        elif int(opc) < 1 or int(opc) > len(tupla):
            print("Opcion invalida")
        else:
            return int(opc)
#print(menu(("Tupla","De","Ejemplo")))
#######################################################################################################################
def get_answers_bystep_adventure(adv):
    query = f"select paso from pasos where id_aventura = {adv}"
    cur.execute(query)
    pasos = {}
    paso = cur.fetchall()
    x = 1
    for i in paso:
        pasos["pasos{}".format(x)] = i[0]
        x += 1
    return pasos

def get_id_bystep_adventure(adv):
    query = f"select respuesta from respuesta where id_aventura = {adv}"
    cur.execute(query)
    respuesta = {}
    resp = cur.fetchall()
    x = 1
    for i in resp:
        respuesta["pasos{}".format(x)] = i[0]
        x += 1
    return respuesta

def get_first_step_adventure(adv):
    num = str(num_paso[0]).strip("(,)")
    query = f"select paso from pasos where num_paso ={num} and id_aventura = {adv}"
    cur.execute(query)
    primera = cur.fetchall()
    return primera
#
# def getIdGames():
#     query = f"select id_game + m1  from repeticiones"
#     cur.execute(query)
#     games = ()
#     game_id = cur.fetchall()


#######    ###    #     #
#           #     ##    #
#           #     # #   #
#####       #     #  #  #
#           #     #   # #
#           #     #    ##
#          ###    #     #