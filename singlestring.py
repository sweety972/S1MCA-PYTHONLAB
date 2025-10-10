a = input("Enter the first string : ")
b = input("Enter the second string : ")
c = b[0] + a[1:] + a[0] + b[1:]
print("Joint string with first characters swapped :",c)