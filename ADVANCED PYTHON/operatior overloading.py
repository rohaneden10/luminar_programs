
class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self,other):
        return Book(self.pages + other.pages)
        #return self.pages+other.pages

    def __str__(self):
        return str(self.pages)
num=int("10")
b1=Book(100)
b2=Book(200)
b3=Book(400)
print(b1)
print(b2)
print(b3)
print(b1+b2+b3)
#b1 `and` b2 are book type