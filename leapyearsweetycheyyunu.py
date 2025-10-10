start=int(input("enter the starting year"))
end=int(input("enter the end"))
i=start
while(i<=end):
    if i%4==0 and i%100!=0 or i%400==0:
        print("\n",i)
    i+=4

    


