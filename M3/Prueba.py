import pymysql

conn = pymysql.connect(host="20.73.187.218", user="prius", password="P@ssw0rd", db="proyecto")
cur = conn.cursor()

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
    return tuplafink


print(get_table("respuesta")[1][0])
print(get_table("pasos")[1][int(get_table("respuesta")[1][0][2])-1])
print(get_table("aventura")[1][int(get_table("pasos")[1][int(get_table("respuesta")[1][0][2])-1][2])-1])

for i in get_table("respuesta")[1]:
    print("Respuestas=",i[2])
    for j in get_table("pasos")[1]:
        if j[0] == i[2]:
            print(j[0]," - ",j[2])
        for n in get_table("aventura")[1]:
            if n[0] == j[2]:
                print(n[0],n[1])
