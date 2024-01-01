from sys import stdin

N = int(stdin.readline())
p_doc = {}
for i in range(N):
    p = list(map(str, stdin.readline().split()))
    if p[0] not in p_doc:
        p_doc[p[0]] = [p[1]]
    else:
        p_doc[p[0]].append(p[1])

print(p_doc)