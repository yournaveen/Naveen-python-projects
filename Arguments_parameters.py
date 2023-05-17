#Position argument is nothing but placing the argument in a position
def adding_num(a,b):#Here a,b are Parameters
    c=a+b
    print(c)
adding_num(10,19)#Here 10,19 are arguments
# the above scenario shows positioning the parameter a in 10 and b in 19

#Next is Keyword arguments
#simple 
def biodata(name,age):
    print(name)
    print(age)
biodata("Naveen",21)

#Code using Keyword arguments or default arguments
def biodata(name="Naveen",age=21):#Assining like keyword where parameter value arguments are assign 
    print(name)
    print(age)
biodata()

#code with Arbitrary arguments
def people(*name):
    print(name)
people("Naveen","praveen","Gokul")#Here *name is packed for whole value in call function




