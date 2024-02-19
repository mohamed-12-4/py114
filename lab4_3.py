def rewrite(number):
    odd = 0
    even = 0
    while number != 0:
        digit = number % 10
        if digit %2 != 0:
            odd += digit
            odd *= 10
        elif digit %2 == 0:
            even += digit
            even *= 10
        number //= 10
    return odd, even

number = int(input("Enter a number:"))
odd, even = rewrite(number)
print("Even digits as a new number: ", int(str(even)[::-1]))
print("Odd digits as a new number: ", int(str(odd)[::-1]))


