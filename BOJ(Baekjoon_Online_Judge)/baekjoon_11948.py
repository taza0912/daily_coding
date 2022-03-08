from sys import stdin

sc = []
so = []

for i in range(4):
    sc.append(int(stdin.readline()))
for j in range(2):
    so.append(int(stdin.readline()))

sc.pop(sc.index(min(sc)))
so.pop(so.index(min(so)))

print(sum(sc) + sum(so))