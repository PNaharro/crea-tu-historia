import pymysql

conn=pymysql.connect(host="20.73.187.218", user="prius", password="P@ssw0rd",db="prueba")
cur=conn.cursor()

def get_table():
    tabla = input("Introduce el nombre de la tabla: ")
    query = f"select * from {tabla}"
    cur.execute(query)
    rows = cur.fetchall()
    print(rows)
#get_table()

def insertUser():
    user = input("Introduce un nombre de usuario: ")
    password = input("Introduce una contraseña: ")
    query = f"insert into usuarios (usuario, contraseña) values ('{user}','{password}')"
    cur.execute(query)
    conn.commit()
#insertUser()

def checkUser():
    user = input("Introduce un nombre de usuario: ")
    if len(user) < 6 or len(user) > 10 and user.isalnum() == False:
        return False
    else:
        return True
#print(checkUser())

def checkPassword():
    password = input("Introduce una contraseña: ")
    if len(password) < 8 or len(password) > 12 and password.isalnum() == False:
        return False
    else:
        return True
#print(checkUser())
