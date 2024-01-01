from sys import stdin

N, M, K = map(int, stdin.readline().split())
print(min([M, K]) + min([(N-M), (N-K)]))