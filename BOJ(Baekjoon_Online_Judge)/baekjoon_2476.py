from sys import stdin

tmp = int(stdin.readline())
result = []
for i in range(tmp):
    nlist = sorted(list(map(int, stdin.readline().split())))
    if nlist.count(nlist[1]) == 1:
        result.append(nlist[2]*100)
    elif nlist.count(nlist[1]) == 2:
        result.append(1000 + nlist[1]*100)
    else:
        result.append(10000 + nlist[1]*1000)

print(max(result))