#class:design pattern
#object:real wordl entity
#references:name that refers to a memory locations ie to do operations on object
class Person:#first letter is capital useful
    def walk(self):
        print("person is walking")
    #self is a keyword for oop #while in class #if methood outside class no self is needed
    def run(self):
        print("person is running")
    def jump(self):
        print("person is jumping")
#referencename=classname()#here obj is reference
obj=Person()#we are creating object of person class
#we use the reference to call the methods of class
obj.walk()
obj.run()
obj.jump()

