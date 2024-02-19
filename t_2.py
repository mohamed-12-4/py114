"""
Taks 1
Seema is 21 years old. For each even birthday (2nd, 4th, 6th ….20) she receives money. For her
second birthday, she receives 10 USD, and the sum increases by 10 USD with each following odd birthday
(3rd -> 10, 5th-> 20, 7th-> 30, etc.). Seema has secretly been saving the money for 21 years. On her 21st
birthday, she wants to buy a washing machine for 150 USD. Write a program that calculates how much
money she has saved and whether it is enough to buy a washing machine.

"""

sum = 0
total = 10
for i in range(2, 22):
    if i % 2 == 0:
        total += sum

    if i % 2 != 0:
        sum += 10

print("she can buy washing machine" if total >= 150 else "She have to save more")
