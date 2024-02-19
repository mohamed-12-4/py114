"""
Write a program that prints the day of the week depending on the given number (1 … 7) or "Error!" if
invalid input is given.
"""
import os
n = int(input("Enter week number:"))

if n < 1 or n > 7:
    print("Error!")
    os._exit(0)

m = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday",
}

print(m[n])


