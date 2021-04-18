import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="magic",
    auth_plugin="mysql_native_password"

)
files=open("employee","r")
cursor=db.cursor()
#sql="create table employee(eid int,ename varchar(25),desig varchar(30),salary int)"
#cursor.execute(sql)
#db.close()
for lines in files:
    data=lines.rstrip("\n").split(",")
    sql="insert into employee(eid,ename,desig,salary)values(%s,%s,%s,%s)"
#sql="DELETE FROM employee WHERE eid=100;"
#sql="update employee set salary=25000 where eid=100"
    cursor.execute(sql,tuple(data))
    db.commit()#for reflecting values in table whileinserting and updating
db.close()