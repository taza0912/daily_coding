from sys import stdin

N, K = map(int, stdin.readline().split())
k = 0
for i in range(1, N+1):
    if N%i != 0:
        continue
    else:
        k += 1
        if k == K:
            print(i)
            break
        else:
            continue
if k < K:
    print(0)