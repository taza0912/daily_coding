from sys import stdin

T = int(input())
for i in range(T):
    A, B = map(int, stdin.readline().split())
    a = int(str(A)[-1])
    if a in (1, 5, 6, 0):
        if a == 0:
            print(10)
        else:
            print(a)
    elif a in (4, 9):
        b = B%2 + 2
        print(str(a**b)[-1])
    else:
        b = B%4 + 4
        print(str(a**b)[-1])