number = int(input("Enter an integer: "))
def sum_of_digits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

def avg_of_digits(n):
    sum = 0
    count = 0
    while n > 0:
        sum += n % 10
        n //= 10
        count += 1
    return sum / count

if number % 2 != 0:
    print(f"{number} is odd and the sum of it digit is: {sum_of_digits(number)}")

if number % 2 == 0:
    print(f"{number} is even and the average of it digit is: {avg_of_digits(number)}")
    