from sys import stdin

for i in range(3):
    temp = int(stdin.readline())
    result = 0
    for j in range(temp):
        result += int(stdin.readline())
    if result == 0:
        print("0")
    elif result > 0:
        print("+")
    else:
        print("-")