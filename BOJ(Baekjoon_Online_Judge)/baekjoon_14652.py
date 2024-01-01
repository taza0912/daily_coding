from sys import stdin

N, M, K = map(int, stdin.readline().split())

print(K//M, K%M)