#Replacing value in an array
import array as nav
from random import random
s=nav.array('i',[10,20,30,40,50])
print(s) 
s[1]=909#replacing an element in the array
#above scenario shows the index value 1 is 20 but it is replaced by another value given 909
print(s)
#replacing another one value in array
s[4]=100
print(s)
#Adding and removing array
e=nav.array('i',[11,22,33,44,55])
#append func is used to add values in array
e.append(66)
e.append(77)
print(e)
#if you want add a large number of values use extend
e.extend([88,99,111])
print(e)
#if you want to remove an element from the list
f=nav.array('u',['n','a','v','e','e','e','n'])
#here we hsve used a 'u' type code which is for unicode characters
f.pop(3)#here index value 3 is e in array which need to be removed
print(f)


