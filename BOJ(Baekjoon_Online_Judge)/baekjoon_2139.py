def CY(n):
    result = 0
    if n%400 == 0:
        result = 1
    elif n%100 == 0:
        result = 0
    elif n%4 == 0:
        result = 1
    else:
        result = 0
    return result

from sys import stdin

m_30 = [4, 6, 9, 11]
while True:
    val = list(map(int, stdin.readline().split()))
    result = 0
    if val[0] == 0:
        break
    else:
        if val[1] > 1:
            for i in range(1, val[1]):
                if i == 2:
                    if CY(val[2]) == 0:
                        result += 28
                    else:
                        result += 29
                elif i in m_30:
                    result += 30
                else:
                    result += 31
        result += val[0]
        print(result)