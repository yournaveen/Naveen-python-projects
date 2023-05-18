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



