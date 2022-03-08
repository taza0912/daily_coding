from sys import stdin

for i in range(3):
    val = list(map(int, stdin.readline().split()))
    result = []
    for j in range(-1, -4, -1):
        if val[j] >= val[j-3]:
            result.append(str(val[j]-val[j-3]))
        else:
            val[j-1] -= 1
            result.append(str((val[j]-val[j-3]+60)))
    print(" ".join(result[::-1]))