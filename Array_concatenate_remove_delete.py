#concatenate is nothing but adding two arrays
from array import *
a=array('i',[5,10,15,20,25])
b=array('i',[1,2,3,4,5])
#if you want add two values of array your another result variable should also be defined by int or d or u
c=array('i')
c=a+b
print(c)
#remove method is used to remove the 1st value of same integer
#see below
d=array('i',[10,20,50,30,40,50])
d.remove(50)#here extra value 50 is given which is removed by remove function it always removes the 1st value of same integer
print(d)
e=array('i',[10,20,50,30,40,50])
e.pop(2)#pop function pop ups the index value by removing the value with the index placement
print(e)

