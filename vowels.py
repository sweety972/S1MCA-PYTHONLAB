vowelAlphabets = "aeiouAEIOU"
word = input("Enter a word : ")
ourVowels = ""
for i in word:
    if i in vowelAlphabets:
        ourVowels += i

for i in ourVowels:
    print(i + "\n")