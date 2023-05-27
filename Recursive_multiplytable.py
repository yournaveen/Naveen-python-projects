#Getting multiplication table using recursion
def recmul(n,t):
    if n>0:
     recmul(n-1,t)
     print(n,"*",t,"=",n*t)
    if n==0:
     print("Your table is")
t=int(input("Enter the table number: "))
n=int(input("Enter the table limit: "))#Here n is given input as a value, u can also use funtion call to enter the value
recmul(n,t)


