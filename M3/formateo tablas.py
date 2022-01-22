import pymysql

conn = pymysql.connect(host="20.73.187.218", user="pmaestre", password="P@ssw0rd", db="proyecto")
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

def formatText2(text,lenLine,split):
    result = ""

    while len(text) > lenLine:
        inicio = lenLine - 1
        while text.find(" ", inicio, lenLine) == -1:
            inicio = inicio - 1
        result = result + text[0:inicio] + split
        text = text[inicio:].lstrip()
    result = result + text
    return result

def getFormatedBodyColumns(tupla_texts,tupla_sizes,margin=0):
    resultado = ""
    listaTextos = []
    for i in range(len(tupla_texts)):
        listaTextos.append(formatText2(tupla_texts[i],tupla_sizes[i]-margin,"XXXX"))
    totalSize = 0
    for i in range(len(listaTextos)):
        totalSize +=len(listaTextos[i])
    while totalSize > 0:
        for i in range(len(listaTextos)):
            final = listaTextos[i].find("XXXX")
            if final != -1:
                resultado += (listaTextos[i][0:final]+" "*margin).ljust(tupla_sizes[i])
                listaTextos[i] = listaTextos[i][listaTextos[i].find("XXXX")+4:]
            else:
                resultado += (listaTextos[i] + " "*margin).ljust(tupla_sizes[i])
                listaTextos[i] = ""
        resultado += "\n"
        totalSize = 0
        for i in range(len(listaTextos)):
            totalSize += len(listaTextos[i])
    return resultado


def getFormatedTable():
    query = f"select a.id_aventura, a.nombre_aventura, p.id_paso, p.paso, r.id_respuesta, r.respuesta from aventura a inner join pasos p on p.id_aventura=a.id_aventura inner join respuesta r on r.id_paso=p.id_paso;"
    cur.execute(query)
    x = cur.fetchall()
    print(getHeadeForTableFromTuples(("ID AVENTURA - NOMBRE","ID PASO - DESCRIPCION","ID RESPUESTA - DESCRIPCION","NUMERO DE VECES SELECCIONADA"),(0,25,43,31),"Respuestas más usadas"))

query = f"select concat(a.id_aventura,' - ', a.nombre_aventura), concat(p.id_paso,' - ', p.paso),concat( r.id_respuesta,' - ', r.respuesta), count(re.id_respuesta) from aventura a inner join pasos p on p.id_aventura=a.id_aventura inner join respuesta r on r.id_paso=p.id_paso inner join repeticiones re on re.id_respuesta=r.id_respuesta group by re.id_respuesta;"

# query = f"select concat(a.id_aventura,' - ', a.nombre_aventura), concat(p.id_paso,' - ', p.paso),concat( r.id_respuesta,' - ', r.respuesta) from aventura a inner join pasos p on p.id_aventura=a.id_aventura inner join respuesta r on r.id_paso=p.id_paso ;"
cur.execute(query)
x = cur.fetchall()

getFormatedTable()

for i in x:
    texto1 = i[0]
    texto2 = i[1]
    texto3= i[2]
    texto4 = str(i[3])
    tupla = (texto1,texto2,texto3,texto4)
    size = (25, 38, 29, 20)
    print(getFormatedBodyColumns(tupla, size, margin=2))


