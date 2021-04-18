#c0nstructor is used to provid instanc evariabkes
#instacne variables cane be defined inside constructor
#used to initialize instance variables
#automatically invoked when object is created
class Addition:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        self.c=self.a+self.b
        print(self.c)
obj=Addition(2,3)
#instance variables are initialised when object is created
