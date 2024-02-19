N = int(input("Enter the value of N: "))

for i in range(N, 0, -1):
    if i == N or i < 3:
        print(" ".join("$"*i))
    else:
        print(" ".join("$" + "*"*(i-2) + "$"))
    
