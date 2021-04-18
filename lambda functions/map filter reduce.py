#map()
#filter()
#reduce()
lst=[12,32,32,2,2,3,32,2,332]
#we need to find squares of these nos
#map is used when we want to apply some operation to every element in list
#op of map is list
def squ(n1):
    return n1**2
squares=list(map(lambda n1:n1**2,lst))

#squares=list(map(squ,lst))
print(squares)
#if we use lambda functions we replace squ argument by(squares=list(map(lambda n1:n1**2,lst))
#map take two arguments
#1 function to be applied
#2 iterables
