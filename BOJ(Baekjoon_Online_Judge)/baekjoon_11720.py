import sys

N = int(sys.stdin.readline())

answer = 0
N_str = input()
for i in range(N):
    answer += int(N_str[i])

print(answer)