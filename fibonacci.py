n = int(input("Enter the number of terms  : "))
a = 0
b = 1
count = 0

while count < n:
    print(a, " ")
    temp = a
    a = b
    b = temp + b
    count += 1
