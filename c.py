"""
Task 3: Write a Python program that prompts the user to enter an alphabet. Then determine if it is a
vowel. Letters A,a, E,e, I,i,O, o, and U,u are vowels. If entered alphabet is lower case vowel , convert it
to higher case.
Hint: Use of built-in function upper() or lower() is allowed.
 Consider use of membership operator. 
"""
c = input("Enter an alphabet: ")
assert len(c) == 1 and c.isalpha(), "not a character"
print(f"{c.upper()} is Vowel" if c.upper() in ["O", "A", "E", "I", "U"] else f"{c.upper()} Not a vowel")