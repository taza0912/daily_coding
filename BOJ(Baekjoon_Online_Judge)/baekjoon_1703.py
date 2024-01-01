from sys import stdin

while True:
    val = list(map(int, stdin.readline().split()))
    if len(val) == 1 and val[0] == 0:
        break
    else:
        tmp = len(val)
        result = 1
        x = 0
        for i in val[1:]:
            if x == 0:
                result *= i
                x = 1
            else:
                result -= i
                x = 0
        print(result)