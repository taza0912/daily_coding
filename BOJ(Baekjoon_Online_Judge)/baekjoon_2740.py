from sys import stdin

N, M = map(int, stdin.readline().split())
A = []
for i in range(N):
    A.append(list(map(int, stdin.readline().split())))

M, K = map(int, stdin.readline().split())
B = []
for x in range(M):
    B.append(list(map(int, stdin.readline().split())))

for p in range(N):
    for q in range(K):
        val = 0
        for r in range(M):
            val += A[p][r] * B[r][q]
        print(val, end=" ")
    print()