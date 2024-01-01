from sys import stdin

t = int(stdin.readline())
for i in range(t):
    n = bin(int(stdin.readline()))[2:][::-1]
    for j in range(len(n)):
        if n[j] == '1':
            print(j, end=" ")
    print()