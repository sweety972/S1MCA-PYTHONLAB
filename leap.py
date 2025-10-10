a=int(input("Enter the year : "))
if a % 4 == 0 and a % 100 != 0:
    print("It is a leap year.")
elif a % 4 == 0 and a % 100 == 0 and a % 400 == 0:
    print("It is a leap year.")
else:
    print("It is not a leap year.")
