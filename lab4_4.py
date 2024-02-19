N = int(input("Enter the even value of N: "))
while N % 2 != 0:
    print(f"{N} is odd", end=", ")
    N = int(input("please enter an even integer: "))

for i in range(N):
    mid = N // 2
    if i >= mid:
        print(" ".join("O"*mid), end=" ")
        print(" ".join("H"*mid))
    else:
        print(" ".join("H"*N))

