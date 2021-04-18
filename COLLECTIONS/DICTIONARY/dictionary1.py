employee={"empid":101,"empname":"rohan","desig":"supervisor","salary":10000}
print(employee)
print(employee["empname"])
print("company" in employee)
employee["company"]="luminar"
print(employee)
employee["salary"]+=15000
print(employee)
for i in employee:
    print(i,":",employee[i])