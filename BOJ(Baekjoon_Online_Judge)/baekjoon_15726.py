from sys import stdin

nlist = list(map(int, stdin.readline().split()))
print(max(int(nlist[0]*nlist[1]/nlist[2]), int(nlist[0]/nlist[1]*nlist[2])))