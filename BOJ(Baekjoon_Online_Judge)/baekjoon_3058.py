from sys import stdin

t = int(stdin.readline())
for i in range(t):
    nlist = sorted(list(map(int, stdin.readline().split())))
    result = []
    for j in nlist:
        if j%2 == 0:
            result.append(j)
    print(sum(result), result[0])