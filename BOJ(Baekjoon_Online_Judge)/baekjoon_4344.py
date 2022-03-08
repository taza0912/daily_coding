import sys

C = int(sys.stdin.readline())

for i in range(C):
    S = list(map(int, sys.stdin.readline().split()))
    score_sum = 0
    for j in S[1:]:
        score_sum += j
    score_mean = score_sum/S[0]
    counts = 0
    for k in S[1:]:
        if k > score_mean:
            counts += 1

    print("{:.3f}%" .format((counts/S[0])*100))