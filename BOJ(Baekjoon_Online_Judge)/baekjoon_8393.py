import sys

n = int(sys.stdin.readline())
t = n
for i in range(t-1, 0, -1):
    n += i

print(n)