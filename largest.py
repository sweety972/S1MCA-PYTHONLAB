a=int(input("enter first number :"))
b=int(input("enter second number :"))
c=int(input("enter third number :"))
if a>b and a>c :
    print(a," is the largest")
elif b>a and b>c :
    print (b,"is largest")
else:
    print(c, "is largest")