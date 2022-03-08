from sys import stdin

N, K = map(int, stdin.readline().split())
for i in range(N):
    A, B = map(int, stdin.readline().split())
    K += A-B

pritn("비와이")