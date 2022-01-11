import pymysql
def getUsers():
    conn = pymysql.connect(host="20.73.187.218", user="prius", password="P@ssw0rd", db="prueba")
    cur = conn.cursor()
    query = f"select * from usuarios"
    cur.execute(query)
    x = cur.fetchall()
    diccionario = {}
    for i in x:
        diccionario[i[1]] = {"contraseña":i[2],"id":i[0]}
    print(diccionario)

getUsers()