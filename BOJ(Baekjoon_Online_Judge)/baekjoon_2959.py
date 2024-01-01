from sys import stdin

nlist = sorted(list(map(int, stdin.readline().split())))
print(nlist[0] * nlist[2])