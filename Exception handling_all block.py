#Exception are nothing but handling Errors
#there are normally many types of errors which are derived form class Exception
#to handle these types are errors Exceptions are used
#justsee below it has 4 statements,statements has 2 forms 1.normal statment 2. Critical statement
a=int(input("Enter the value 1:"))
b=int(input("Enter the value 2:"))
try:
    c=a/b#i do no whether this statement run or may be get error so i use a try block to avoid getting error
except Exception as e:#Exception takes all types of errors(E is case sensitive) & e can be any character to define Exception
    print(e)
else:
    print("Division value is:",c)
finally:
    print("Thank you")#this finally  block will print even it is error or not a error that code occurs

#another scenario
try:
    n=int(input("Enter you reg no: "))#we have given a string instead of giving integer we have value erro
except Exception as a:
    print(a)
else:
    print(n)


#Using raise Exception
#creating a marks for the people it should be between 0 to 100
m=int(input("Enter you mark:"))
try:
    if m<0 or m>100:
        raise Exception ("Please Enter value between 0 to 100")#raise Exception is also called user defined exception that we can use manually to raise exception
    print("Your mark is: ",m)
except Exception as e:
    print(e)
