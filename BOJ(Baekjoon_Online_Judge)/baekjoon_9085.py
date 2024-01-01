from sys import stdin

t = int(stdin.readline())
for i in range(t):
    n = int(stdin.readline())
    print(sum(list(map(int, stdin.readline().split()))))