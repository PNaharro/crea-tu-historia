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
# print(get_table(aventura))
# print(get_table(pasos))
# print(get_table(respuesta))

for i in range(len(get_table("aventura")[1])):
    for j in range(len(get_table("aventura")[1])):
        print(get_table("aventura")[1][i][j],"\n",get_table("pasos")[1][i][j],"\n",get_table("respuesta")[1][i][j])



def getFormatedTable():
    print(getHeadeForTableFromTuples(("ID AVENTURA - NOMBRE","ID PASO - DESCRIPCION","ID RESPUESTA - DESCRIPCION","NUMERO DE VECES SELECCIONADA"),(0,30,30,39),"Respuestas más usadas"))

getFormatedTable()