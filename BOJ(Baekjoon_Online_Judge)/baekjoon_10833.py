from sys import stdin

n = int(stdin.readline())
result = 0
for i in range(n):
    val = list(map(int, stdin.readline().split()))
    result += val[1]%val[0]
print(result)