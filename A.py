a = int(input("Number 1: "))
b = int(input("Number 2: "))
c = int(input("Number 3: "))

if a >= c and a >= b:
    print(a)
elif b >= a and b >= c:
    print(b)
elif c >= a and c >= b:
    print(c)