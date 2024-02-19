N = int(input("Enter an integer 'N': "))

a = 0
b = 1
c = a + b
sum = 0
print("The Febonacci series up to the value {}".format(N))
print(a, b, end = " ")
while c <= N:
    print(c, end=" ")
    sum += c
    c = a + b
    a = b
    b = c
    
    
print("\nThe sum of this series is:", sum)