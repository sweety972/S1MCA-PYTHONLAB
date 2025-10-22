str = input("Enter the string : ")

check = str[-1:-4:-1]
check = check[::-1]

if check == "ing" :
    print(str + "ly")
else:
    print(str + "ing")
