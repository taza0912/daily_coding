C = input()

x = {}
start = 65
for i in range(3, 11):
    x[i] = []
    t = 3
    if i == 8 or i == 10:
        t = 4
    for j in range(t):
        x[i].append(chr(start))
        start += 1

answer = 0
for k in C:
    for n in range(3, 11):
        if k in x[n]:
            answer += n

print(answer)