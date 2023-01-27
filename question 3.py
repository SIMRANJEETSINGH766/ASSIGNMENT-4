import random as ran
a=int(input("enter a number from where you want numbers to start (eg-11)"))
b=int(input("enter a number from where you want numbers to end (eg-115)"))
lis1=lis2=[]
for i in range (0,10):
    n=ran.randint(a,b)
    lis1.append(n)
for j in range (0,10):
    n=ran.randint(a,b)
    lis2.append(n)
for k in range (0,10):
    r=ran.choice(lis1)
    s=ran.choice(lis2)
    d=r*s
    print(r,"*",s,"=")
    num=int(input("enter the answer"))
    if d==num:
        print("your ans is right")
    else:
        print("your ans is wrong")
        print("the right ans is "d)
