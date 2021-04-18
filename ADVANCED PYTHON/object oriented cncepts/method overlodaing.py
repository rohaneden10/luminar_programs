class Person:
    def show(self,num1):
        self.num1=num1
        print(self.num1)
class Student(Person):
    def show(self,num2,num3):
        self.num2=num2
        self.num3=num3
        print(self.num2,self.num3)
per=Student()
per.show(3,4)#call depend on no of arguments