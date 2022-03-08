from sys import stdin

N = int(stdin.readline())
plist = sorted(list(map(int, stdin.readline().split())))

answer = 0
for i in range(N):
    time = 0
    for j in range(i+1):
        time += plist[j]
    answer += time
print(answer)