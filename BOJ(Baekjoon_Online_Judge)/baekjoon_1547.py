from sys import stdin

result = [1, 0, 0]
m = int(stdin.readline())
for i in range(m):
    t = 0
    val = list(map(int, stdin.readline().split()))
    t = result[val[0]-1]
    result[val[0]-1] = result[val[1]-1]
    result[val[1]-1] = t

print(result.index(1)+1)