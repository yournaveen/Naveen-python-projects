#Handling the Exceptions instead of getting error
#Errors are of three 1.syntax or compile 2.Logical 3.runtime
#1.syntax Error
for i in range(10):
   print(i)# Here a syntax error will occur need indentation
#these error are shwon by python itself to correct
#2.logical error
a=5
b=6
print("Added value is:",a-b)#here we need only added value instead we are getting a subtracted value
#we have made mistake in logical
#3.Run time error
a1=int(input("Enter value 1: "))
a2=int(input("Enter value 2: "))
try:
    c=a1/a2
except:
    print("Sorry !!!! Exception error: no number can be divisible by zero")
else:
    print("Division value is:",c)

#File handling using an Exception
try:
    fp=open('rr.txt','r')
except:
    print("No File for this name found")
else:
    r=fp.read()
    print(r)
   # fp.write("Hi da venna")
    fp.close()
    
