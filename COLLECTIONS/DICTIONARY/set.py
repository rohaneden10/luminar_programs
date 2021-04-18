#define
#set={1,2,3}
#print(type(set))
#just {} is dictionary,valuesinside curly braces gives set..to create empty set we use set function
#set=set()
#print(type(set))#op is
#set={1,2,34,4,"sab"}
#print(set)#implies set is heterogeneous
#doesnt support duplication
#true boolean value is 1 and set doesnt suppor ruplication
#insertion order s not reserevd because op data is not in the same order as input data
#set is mutable
# to add an element to list usr set.add()
set={1,2,3}
set.update([10,2,3])#for multipleelements
print(set)
#toczlculate set sum sum functionis there

print(sum(set))
print(min(set))
print(max(set))
print(len(set))
set1={1,2,3,4,5}
set2={6,2,7,8,9}
set3=set1.union(set2)
print(set3)
set4=set1.intersection(set2)
print(set4)
set6=set2.difference(set1)
print(set6)#in set 2 and not in set1