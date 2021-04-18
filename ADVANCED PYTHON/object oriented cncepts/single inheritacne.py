class Student:
    def m1(self,age):
        self.age=age
        print("my age is ",self.age)

class Child(Student):
    def m2(self):
        print(self.age)
obj=Child()
obj.m1(23)
obj.m2()