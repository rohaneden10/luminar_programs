#dict={}
#print(type(dict))
#values stored in dictinat as key value pairs
#eg:rollno:10
#name:rohan
#key=rollnoand name
#value=10 and rohan
#student={"roll":1001,"name":"rohan","age":23}
#print(student)
#supports heterogeneosu data
#
#
#
#student={"roll":1001,"name":"rohan","age":23,"age":30}
#print(student)
#implies dictionary doesnt support duplicate key
student={"roll":1001,"name":"rohan","age":23,"cpp":23}
#print(student)
#implies it support duplicate value
#insertion order also preserved
#print(student["age"])
#if we want to fetch values we use corresponding keys
#print(student["name"])
for i in student:
    print(i,":",student[i])
#updationie is it mutable or not
student["name"]="myren"
print(student)
#it is mutable
student["cpp"]+=10
print(student)
#key can be integer too
#del keyword used to delete keywords
del student["cpp"]
print(student)
print("total" in student)#if the key total avaliable in student nd if op is fale its not availiable
student["total"]=120
print(student)
