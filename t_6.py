"""
########################################################################################################
Task 6: Write a program that finds the count of all numbers in the range [1 … 1000], that end in 3 or 5.
########################################################################################################
"""

count = 0

for i in range(0, 1001):
    if i % 10 == 3 or i % 10 == 5:
        count += 1
print(f"the count of numbers ending with 3 or 5 is: {count}")