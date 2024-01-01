from sys import stdin

K, N, M = map(int, stdin.readline().split())
result = K*N-M

if result > 0:
    print(result)
else:
    print(0)