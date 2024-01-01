def how_y(x: list):
    result = 0
    for i in x:
        result += ((i//30)+1)*10
    return result
def how_m(x: list):
    result = 0
    for i in x:
        result += ((i//60)+1)*15
    return result

from sys import stdin

n = int(stdin.readline())
nlist = list(map(int, stdin.readline().split()))
y = how_y(nlist)
m = how_m(nlist)
if y <= m:
    print("Y", end=" ")
if y >= m:
    print("M", end=" ")
print(min(y, m))