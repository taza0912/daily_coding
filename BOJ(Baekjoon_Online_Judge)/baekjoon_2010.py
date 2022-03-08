from sys import stdin

N = int(stdin.readline())
val = 0
for i in range(N):
    val += int(stdin.readline())
print(val-(N-1))