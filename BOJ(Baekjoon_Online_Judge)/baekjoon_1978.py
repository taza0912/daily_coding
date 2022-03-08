import sys

N = int(sys.stdin.readline())

n_list = list(map(int, sys.stdin.readline().split()))

answer = 0
for i in range(N):
    counts = 0
    for j in range(1, n_list[i]+1):
        if n_list[i]%j == 0:
            counts += 1
    if counts == 2:
        answer += 1

print(answer)