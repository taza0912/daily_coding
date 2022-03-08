from sys import stdin

N = list(str(stdin.readline()))

for i in sorted(N)[::-1]:
    print(i, end="")