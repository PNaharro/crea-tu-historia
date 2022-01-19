import pymysql

conn = pymysql.connect(host="20.73.187.218", user="prius", password="P@ssw0rd", db="proyecto")
cur = conn.cursor()

def getHeader_getHeadeForTableFromTuples(text):
    x = (120-len(text))/2
    y = 120
    if len(text)%2!=0:
        y -= 1
    cadena = "="*int(x) + text + "="*int(x)
    return cadena
def getHeadeForTableFromTuples(t_name_columns,t_size_columns,title):
    cadena = getHeader_getHeadeForTableFromTuples(title) + "\n"
    for i in t_name_columns:
            cadena += i.rjust(t_size_columns[0])
            t_size_columns = t_size_columns[1:]
    cadena += "\n" + "*" * 119
    return cadena

def formatText(texto,longitud):
    y = ""
    z = ""
    for i in texto:
        y += i
        if len(y) >= longitud and i.isspace():
            z += y + "\n".ljust(30)
            y = ""
    z += y
    return z

def getFormatedTable():
    query = f"select a.id_aventura, a.nombre_aventura, p.id_paso, p.paso, r.id_respuesta, r.respuesta from aventura a inner join pasos p on p.id_aventura=a.id_aventura inner join respuesta r on r.id_paso=p.id_paso;"
    cur.execute(query)
    x = cur.fetchall()
    print(getHeadeForTableFromTuples(("ID AVENTURA - NOMBRE","ID PASO - DESCRIPCION","ID RESPUESTA - DESCRIPCION","NUMERO DE VECES SELECCIONADA"),(0,25,40,34),"Respuestas más usadas"))
    for i in x:
        print(i[0], "-", formatText(i[1], 20),str(i[2]).rjust(7),"-",formatText(i[3],20),str(i[4]).rjust(10),"-",i[5])
getFormatedTable()


