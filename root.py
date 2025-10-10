import math

print("\nGeneral form is Ax^2 + Bx + C = 0, A != 0\n")
a=int(input("Enter A :"))
b=int(input("Enter B :"))
c=int(input("Enter C :"))

if a != 0:
    determinant = ((b*b) - (4*a*c))

    if determinant > 0:
        root1 = (-b + math.sqrt(determinant)) / 2*a
        root2 = (-b - math.sqrt(determinant)) / 2*a
        print("The equation has 2 distinct roots...\nRoot 1 = ", root1, "\nRoot 2 = ", root2)

    if determinant == 0:
        root = -b / (2*a)
        print("The equation has only one root...\nRoot = ", root)

    if determinant < 0:
        print("The equation has no real roots...")
else:
    print("A cannot be zero...")
