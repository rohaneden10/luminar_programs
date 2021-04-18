#def add(num1,num2):
   # return num1+num2
#we need to call using several arguments
#def add(*args):
   # sum=0
  #  for num in args:
  #      sum=sum+num
  #  return sum
#res=add(10,20,30)
#print(res)
      #*args means accpts in tuple format)
#**kwargs in dictionary format
#def print_person(**kwargs):
  #  print(kwargs)
#print_person(name="ajay",bpalce="angamalt",wplace="bombay")

















employees={
           1000:{"name":"sajay","desig":"python trainer","exp":3},
           1001:{"name":"babu","desig":"java trainer","exp":3},
           1002:{"name":"syay","desig":"java script trainer","exp":2}
}
#eid=int(input("enter employee id"))
#if(eid in employees):
#    print(employees[eid]["name"])
#else:
  #  print("eid not exist")

def emp_details(**kwargs):$kwargs(eid:1000,prop:"desig")
    id=kwargs["eid"]
    prop=kwargs["prop"]
    if(id in employees):
        print(employees[id]["name"])
        print(employees[id][prop])
    else:
        print("eid no exist")

emp_details(eid=1000,prop="desig")