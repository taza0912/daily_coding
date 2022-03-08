from sys import stdin

A, B, C, D = map(int, stdin.readline().split())
print(abs((A+D)-(B+C)))