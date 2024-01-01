from sys import stdin

n, m, k = map(int, stdin.readline().split())
result = []
for i in range(k+1):
    a = n-i
    b = m-(k-i)
    if a<0 or b<0:
        continue
    else:
        result.append(min(a//2, b))

print(max(result))