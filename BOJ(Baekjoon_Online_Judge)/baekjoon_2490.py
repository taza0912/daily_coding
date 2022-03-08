from sys import stdin

for i in range(3):
    val = list(map(int, stdin.readline().split())).count(0)
    if val == 1:
        print("A")
    elif val == 2:
        print("B")
    elif val == 3:
        print("C")
    elif val == 4:
        print("D")
    else:
        print("E")
    