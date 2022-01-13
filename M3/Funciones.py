import pymysql

conn = pymysql.connect(host="20.73.187.218", user="prius", password="P@ssw0rd", db="prueba")
cur = conn.cursor()

def getUsers():
    query = f"select * from usuarios"
    cur.execute(query)
    x = cur.fetchall()
    diccionario = {}
    for i in x:
        diccionario[i[1]] = {"contraseña":i[2],"id":i[0]}
    return  diccionario
#print(getUsers())

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

def userExists(user):
    for i in getUsers():
        if user == i:
            return True
        else:
            return False
#user = input("Dime el usuario: ")
#print(userExists(user))

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

def checkUserbdd(user,password):
    for i in getUsers():
        if user == i:
            if password == getUsers()[i]["contraseña"]:
                return 1
            else:
                return -1
        else:
            return 0

# user = input("Dime tu usuario: ")
# password = input("Dime tu constraseña: ")
# print(checkUserbdd(user,password))

def getHeader(text):
    x = (100-len(text))/2
    y = 100
    if len(text)%2!=0:
        y -= 1
    cadena = "*"*y +"\n" + "="*int(x) + text + "="*int(x) + "\n" + "*"*y
    return cadena
#print(getHeader("ESTO ACEPTA HASTA 100 CARACTERES"))