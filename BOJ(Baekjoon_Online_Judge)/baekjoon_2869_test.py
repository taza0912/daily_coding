from sys import stdin

A, B, V = map(int, stdin.readline().split())

N = (V-B)/(A-B)
if N == (V-B)//(A-B):
    print(int(N))
else:
    print(int(N) + 1)