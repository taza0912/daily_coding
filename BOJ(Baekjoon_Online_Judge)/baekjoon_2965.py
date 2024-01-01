from sys import stdin

a, b, c = map(int, stdin.readline().split())
print(max(len([i for i in range(a+1, b)]), len([j for j in range(b+1, c)])))