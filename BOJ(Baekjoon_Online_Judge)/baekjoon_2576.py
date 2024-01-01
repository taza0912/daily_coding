from sys import stdin

a = []
b = 0
for i in range(7):
    val = int(stdin.readline())
    if val%2 != 0:
        a.append(val)
        b += val

if b != 0:
    print(b)
    print(min(a))
else:
    print(-1)