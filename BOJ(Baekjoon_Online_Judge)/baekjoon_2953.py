from sys import stdin

s_doc = {}
for i in range(1, 6):
    s_doc[i] = sum(list(map(int, stdin.readline().split())))

t = max(list(s_doc.values()))
for i, (key, value) in enumerate(s_doc.items()):
    if value == t:
        print(key, value)