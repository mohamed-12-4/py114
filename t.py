s = input("Enter a character")

if len(s) == 1 and s.isalpha():
    print("it is a character")
    if s.isupper():
        print("is upper")
    elif s.islower():
        print("is lower")

else:
    print("no a character")