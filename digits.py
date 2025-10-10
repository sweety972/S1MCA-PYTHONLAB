a=int(input("enter the number"))
count=0
while a!= 0 :
    a//=10
    count+=1
print("number of digits",count)