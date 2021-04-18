class Parent:
    parent_name='babu'
    def m1(self,age):
        self.age=age
        print("my name is ",Parent.parent_name)
        print(self.age)
class Child(Parent):
    def m2(self,cage):
        self.cage=cage
        print("parent name is ", Parent.parent_name)
        print(self.age)
        print(self.cage)
c=Child()
c.m1(23)
c.m2(12)
#single inheritance
