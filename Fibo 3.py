n=int(input("Enter the number :"))
f=0
s=1

for i in range(n):
    print(f)
    print(s)
    t=f+s
    print(f,"+",s,"=",t)
    f=s
    s=t
    
    
