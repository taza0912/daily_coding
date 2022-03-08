import sys

def triangle(n, tlist):
    result = 0
    if n == 1:
        result += tlist[0]
    


N = int(sys.stdin.readline())

T_List = []
answer = 0
for i in range(N):
    T_List.append(list(map(int, sys.stdin.readline().split())))
