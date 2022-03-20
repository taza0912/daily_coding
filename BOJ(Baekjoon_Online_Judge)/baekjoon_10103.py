from sys import stdin

n = int(stdin.readline())
X, Y = 100, 100
for i in range(n):
    x, y = map(int, stdin.readline().split())
    if x == y:
        continue
    elif x > y:
        Y -= x
    else:
        X -= y

print(X)
print(Y)