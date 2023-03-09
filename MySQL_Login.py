import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='latihan'
    )
print("welcome")

kunci=int(input("id mana yang akan diganti nilainya:"))
userbaru=input("nama usernya: ")
passbaru=input("passwordnya: ")
cursor=mydb.cursor()
#teknik1
sql_query="Update user set username='"+userbaru+"',password='"+passbaru+"' where iduser='"+str(kunci)+"'"
#teknik2
cursor.execute("""
        UPDATE USER
        SET username=%s, password=%s
        WHERE iduser=%s
    """,(userbaru,passbaru,kunci))
print(sql_query)
#cursor.execute(sql_query)
print("data berhasil di update")
mydb.commit()
mydb.close()