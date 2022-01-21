import pymysql

conn = pymysql.connect(host="20.73.187.218", user="prius", password="P@ssw0rd", db="proyecto")
cur = conn.cursor()
sel = input("Dime que aventura queires jugar: ")

query = f"select * from pasos where id_aventura = '{sel}'"
cur.execute(query)
pasos = cur.fetchall()

while True:
    x = 1
    for i in pasos:
        if str(i[3])[:-1] == str(x):
            print(i)
    break