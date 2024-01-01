from ntpath import join
from re import T
from sys import stdin

tmp = int(stdin.readline())
nlist = list(map(str, stdin.readline().split()))
nlist = ''.join(nlist).split('0')
result = 0
for i in nlist:
    t = 0
    for j in i:
        t += 1
        result += t

print(result)