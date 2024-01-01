import sys

xdot_doc = {}
ydot_doc = {}

for i in range(3):
    x, y = map(int, sys.stdin.readline().split())
    if x not in xdot_doc:
        xdot_doc[x] = 1
    else:
        xdot_doc[x] += 1
    if y not in ydot_doc:
        ydot_doc[y] = 1
    else:
        ydot_doc[y] += 1

result_x = 0
result_y = 0

for i in xdot_doc.keys():
    if xdot_doc[i] == 1:
        result_x = i
for j in ydot_doc.keys():
    if ydot_doc[j] == 1:
        result_y = j

print(result_x, result_y)