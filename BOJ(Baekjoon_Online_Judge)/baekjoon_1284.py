from sys import stdin

while True:
    val = int(stdin.readline())
    if val == 0:
        break
    else:
        result = 1
        for i in str(val):
            if i == "0":
                result += 4
            elif i == "1":
                result += 2
            else:
                result += 3
            result += 1
        print(result)
        continue
            