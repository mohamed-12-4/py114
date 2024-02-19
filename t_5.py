"""
##########################################################################################################
Task 5: Write a program that reads n integers and finds their sum. Note: The first line of the input holds
the number of integers n. Each of the following n holds an integer. Sum up the numbers and print the
result.
#########################################################################################################
"""

sum = 0

n = int(input("Enter the number of integers: "))

for i in range(n):
    number = int(input(f"Enter integer {i+1}: "))
    sum += number

print(f"the sum of the {n} integers is: {sum}")