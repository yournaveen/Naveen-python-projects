#set is one of the data type which is immutable(cannot modify elements)
a={1,2,3,4,5}
print(a)
#set accepts different data types
a1={90,5.8,'code'}
print(a1)
#set does not accepts duplication
b={1,2,3,4,1,2,5,6}#here 1 and 2 are duplicates(repeating values)
print(b)
#set does not support indexing
#b[2] if you run this it came to an erorr ''set' object is not subscriptable'
#sets accepts sequence if you run sequence of number may change
c={10,20,30,40,50,60,70,80}
print(c)
#if no elements are assigned to a set it will come under 'dict' data type
c1={}#this is a dictionary data type
print(type(c1))
#to define a set in empty we can use a set function
c2=set()#it uses to define a empty set
print(type(c2))
#normally we can add elements in set using some func
d={11,22,33,44,55,66}
d.add(77)#add elemnts
print(d)
#normally we can remove elements in set using some func
d.remove(77)#remove deletes the values in the set
print(d)
#pop func uses normally index values to delete the elements
d.pop()#here we cannot pass index values as set does not support but we can use pop to delete 1st number in the set
print(d)
#clearing the whole element in a set
e={1,2,3,4,5,6,7,8,9}
e.discard(4)#discard also uses the same func like remove func
#but there is main difference between remove and discard if the value is not present in set
#take value 3 it is not present in the set we use discard to delete the value 3 no error will occur come to remove it will fall upon a error
e.update([10,11,12,13])#update is used to add multiple elements in the set but it need to be listed
print(e)

e.clear()#clear is used to remove all elements in a set


