'''
data types:
    int
    str
    float
    list
    tuple
    set
    dict
    bool
        

    



en=str(input("Enter your name:"))
edob=int(input("Enter your Age:"))

if edob>=18:
    eg=str(input("Enter your Gender:"))
    eph=int(input("Enter your Phone number:"))
    r=[en,edob,eg,eph]
    print("____:)Registration successfull____")
    print("Your Details:",r)
else:
    print("Sorry .....You are not eligible for this criteria")
    print("!!!Thank you!!!")


#area of triangle a=(b*h)/2
b=int(input('Enter the breath:'))
h=int(input('Enter the height:'))
print('Area to triangle')
a=(b*h)/2
print('Area of the triangle is:',a)


#swapping two numbers
#method1
a=int(input('Enter the value a:'))
b=int(input('Enter the value b:'))
print('swapping two numbers')

temp=a #temp=a
a=b #a=b
b=temp #b=temp

#method2
a=a+b# assume a=5 b=10 5+10=15,a=15
b=a-b# a=15 15-10=5,b=5
a=a-b# a=15 b=5 15-5=10,a=10

#method3
#python method
a,b=b,a

print(a)
print(b)


#1kilmeter=1000 meter
#1/1000 or 0.001 kilometers in 1 meter.
kilometer=int(input('Enter the value to convert kilometer to mile: '))
mile=kilometer*0.60934
print(kilometer,'kilometer in mile is :',mile)



#prime number
#prime number that is divisible by 1 and divisible by itself
#method 1
n=int(input('Enter the number: '))
count=0
for i in range(1,n+1):
    if n%i==0:
        count=count+1
if count==2:
    print('prime number')
else:
    print('not a prime number')

#method 2
n=int(input('Enter the number: '))
for i in range(2,n):
    if n%i==0:
        print('not a prime number')
        break
else:
    print('prime number')



#prime number within range program
s=int(input('Enter the starting number: '))
e=int(input('Enter the ending number: '))
count=0
slag=0
for i in range(s,e+1):
    if s%i==0 and e%1==0:
        count=count+1
            
if count==2:
    print('prime numbers')
else:
    print('not prime numbers')
  
#PRIME NUMBERS with intervals
start=int(input('Enter the starting number'))
end=int(input('Enter the ending number'))
for num in range(start,end+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)

#ARMSTRONG NUMBERS
n=int(input('Enter the number:'))
temp=n
cube_value=0
while temp>0:
    last_digit=temp%10#3 #5 #1
    cube_value=cube_value+last_digit**len(str(n))#0+27 #27+15**3 #152+1**3
    temp=temp//10#153//10_15 #15//10_1 #1//10_0.1
if cube_value==n:
    print('is a armstrong number')
else:
    print('Not a armstrong number')



def armstrongornot(a):
    temp=a
    count_digit=0
    while temp>0:
        last_num=temp%10
        count_digit=count_digit+last_num**len(str(a))
        temp=temp//10
    if count_digit==a:
        print('armstrong num')
    else:
        print('not a armstrong num')


#Fibonacci series
n=int(input('Enter the limit: '))
a=0
if n<=0:
    print('no negative numbers enter valid number')
elif n==1:
    print(a)
else:
    a=0
    b=1
    print(a)
    print(b)
    #0 1 1 2 3 5 8 13 21 34
    #a b c=a+b
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c)

#factorial
def factorial(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    print(f)
'''
#Reverse string
#method 1 (using indexing)
def reversestring(name):
    reverse_string=name[::-1]
    return reverse_string

#method 2 (using for loop)
def reversestring2(name):
    reverse_string=''#empty due to concadenation
    for i in name:#name='vicky'
        reverse_string=i+reverse_string
        #reverse_string=v+''=v now reverse_string=v
        #reverse_string=i+v=iv now reverse_string=iv
        #reverse_string=c+iv=civ now reverse_string=civ
        #reverse_string=k+civ=kciv now reverse_string=kciv
        #reverse_string=y+civ=ykciv now reverse_string=ykciv
        return reverse_string
    











































