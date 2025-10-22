str = input("Enter the string : ")
dict = {}

for i in range(len(str)):
    if str[i] in dict:
        dict[str[i]] += 1
    elif str[i] == " ":
        dict['space'] = 1
    else:
        dict[str[i]] = 1

print(dict)
