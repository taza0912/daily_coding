N = int(input())

for i in range(1, N+1):
    print(" "*(N-i), end="")
    print("*"*i)
for j in range(1, N):
    print(" "*j, end="")
    print("*"*(N-j))