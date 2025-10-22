def smaller(a, b):
    if a < b:
        return a
    else:
        return b

x = int(input("Enter first number : "))
y = int(input("Enter second number : "))

if x == y:
    print("gcd = ", x)

else:
    less = smaller(x, y)
    gcd=1
    for i in range(1, less + 1):
        if x % i == 0 and y % i == 0:
            gcd = i
        i=i+1
    print("gcd = ", gcd)
