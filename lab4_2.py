def count(number):
    odd = 0
    while number != 0:
        digit = number % 10
        if digit %2 != 0:
            odd += 1
        number //= 10
    return odd

while 1:
    number = int(input("Enter a number: or -1 to stop "))
    if number == -1:
        break
    odd = count(number)
    print(f"Number of odd digits =: {odd}")

print("End, Thank you")
