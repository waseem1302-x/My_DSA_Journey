word = input("Enter Your Word: ")
vowels = "AEIOUaeiou"
count = 0

for letter in word:
    if letter in vowels:
        print(letter, "is vowel")
        count += 1
    else:
        print(letter)

print("Total vowels:", count)
