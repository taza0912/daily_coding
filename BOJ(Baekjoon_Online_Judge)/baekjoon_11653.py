import sys

N = int(sys.stdin.readline())

x = 2
n_doc = {}

while True:
    if N == 1:
        break
    elif N%x != 0:
        x += 1
        continue
    else:
        while N%x == 0:
            if x not in n_doc:
                n_doc[x] = 1
            else:
                n_doc[x] += 1
            N /= x
        x += 1
        continue

for i, j in n_doc.items():
    for k in range(j):
        print(i)