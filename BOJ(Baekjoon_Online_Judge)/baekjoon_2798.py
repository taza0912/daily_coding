import sys

n, m = map(int, sys.stdin.readline().split())

c = list(map(int,sys.stdin.readline().split()))

answer_list = []
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            black_jack = (c[i] + c[j] + c[k])
            if black_jack > m:
                continue
            else:
                answer_list.append(black_jack)

print(max(answer_list))