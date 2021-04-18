#step1 import mysql module
import mysql.connector

#step2 establish a concection

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="magic",
    auth_plugin="mysql_native_password"
)

#step3 create cursor object ie cursor object aid data transport from mysql and vicecersa
cursor=db.cursor()#cursor object is created
sql="select version()"
cursor.execute(sql)
db.close()