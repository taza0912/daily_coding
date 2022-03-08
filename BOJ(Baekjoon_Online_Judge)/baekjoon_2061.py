from sys import stdin

k, l = map(int, stdin.readline().split())
result = ""
for i in range(l-1, 1, -1):
    if k%i == 0:
        result = "BAD" + " " + str(min(i, k//i))
        break

if len(result) != 0:
    print(result)
else:
    print("GOOD")