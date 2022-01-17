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
    return tuplafin
# print(get_table("aventura"))
# print(get_table("pasos"))
# print(get_table("respuesta"))


# print(get_table("respuesta")[1][0])
# print(get_table("pasos")[1][int(get_table("respuesta")[1][0][2])-1])
# print(get_table("aventura")[1][int(get_table("pasos")[1][int(get_table("respuesta")[1][0][2])-1][2])-1])

for i in get_table("respuesta")[1]:
    print("Respuesta=", i[2])
    for j in get_table("pasos")[1][i[2]]:
        print("Pasos=",j)
        for n in get_table("aventura")[1]:
            print("Aventura=",n)