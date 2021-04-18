class Student:
    def m1(self,age):
        self.age=age
        print("my age is ",age)
class Babu:
    def m(self):
        print("babu is a bitch")

class Child(Student,Babu):
    def m2(self):
        print(self.age)
obj=Child()
obj.m1(23)
obj.m2()
obj.m()