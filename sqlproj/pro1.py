import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="magic",
    auth_plugin="mysql_native_password"

)
cursor=db.cursor()
#sql="create table employee(eid int,ename varchar(25),desig varchar(30),salary int)"
#cursor.execute(sql)
#db.close()
sql="insert into employee(eid,ename,desig,salary) values(100,'ajay','developer',23000)"
try:
    cursor.execute(sql)
    db.commit()#for reflecting values in table whileinserting and updating
except Exception as e:
    print(e.args)
    db.rollback()
finally:
    db.close()