from sys import stdin

N = int(stdin.readline())

pdoc = {}
for i in range(65, N+65):
    pdoc[chr(i)] = list(map(int, stdin.readline().split()))

plist = [0 for i in range(N)]

for i in range(65, N+65):
    k = 0
    for j in range(65, N+65):
        if i == j:
            continue
        elif pdoc[chr(i)][0] < pdoc[chr(j)][0]:
            if pdoc[chr(i)][1] < pdoc[chr(j)][1]:
                k += 1
        plist[i-65] = k+1

for l in plist:
    print(l, end=" ")