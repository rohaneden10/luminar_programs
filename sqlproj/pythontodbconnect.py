#connection python and mysql
#mysql-connector for communication between python and mysql
#step1 import mysql module
import mysql.connector

#step2 establish a concection

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    auth_plugin="mysql_native_password"
)

#step3 create cursor object ie cursor object aid data transport from mysql and vicecersa
cursor=db.cursor()#cursor object is created
#execute queries of sqlproj
sql="select version()"
cursor.execute(sql)
data=cursor.fetchone()
print(data)
db.close()
#close db connection
