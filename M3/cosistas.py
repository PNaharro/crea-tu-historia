import pymysql

#MySQL Local
# conn=pymysql.connect(host='localhost', user='PauRius', password='P@ssw0rd',db='Chinook')
#
# cur=conn.cursor()
# albumid = int(input("Dime la ID del album: "))
# query=f"select * from Album where AlbumId = '{albumid}'"
#
# cur.execute(query)
# #fetchall (toda la tabla)
# # rows=cur.fetchall()
# # print(rows)
#
# #fetchone (primero)
# row1=cur.fetchone()
# print(row1)
#
# #fetchmany (numeros personalizados)
# # row=cur.fetchmany(3)
# # print(row)

#MySQL remoto

conn=pymysql.connect(host="20.73.187.218", user="prius", password="P@ssw0rd",db="prueba")
cur=conn.cursor()

nombre = input("Introduce un nombre de usuario: ")
contra = input("Introduce una contraseña: ")

query = f"insert into usuarios (usuario, contraseña) values ('{nombre}','{contra}')"
cur.execute(query)
conn.commit()






