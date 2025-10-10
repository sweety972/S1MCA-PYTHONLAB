startYear = int(input("\nEnter the starting year : "))
endYear = int(input("\nEnter the end year : "))

i = startYear

rem = i % 4
if rem != 0:
    i = i + rem

if i % 100 == 0 and i % 400 != 0:
    i = i + 4

while(i <= endYear):
    if(i % 100 == 0 and i % 400 != 0):
        i += 4
    if i > endYear:
        continue
    print("\n", i)
    i += 4
