import pymysql

conn = pymysql.connect(host="20.73.187.218", user="prius", password="P@ssw0rd", db="proyecto")
cur = conn.cursor()

cadena = "=" * 58 + "Adventures" + "=" * 58 + "\n" + "Id Aventura".ljust(5) + \
         "Aventura".rjust(20) + "Descripcion".rjust(44) + "\n" + "*" * 126


#print(cadena)

def formatText(text,lenLine,split):
    if len(text) == lenLine:
        print("A")
        if text[lenLine].isspace():
            print("A")
            print(text[lenLine], split)





formatText("UN barco  humilde juas juas juas juas juas juas",10,"\n")

