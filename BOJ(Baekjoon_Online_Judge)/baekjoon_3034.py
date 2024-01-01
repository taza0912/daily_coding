from sys import stdin

n, w, h = map(float, stdin.readline().split())
for i in range(int(n)):
    val = int(stdin.readline())
    if val**2 <= w**2 + h**2:
        print('DA')
    else:
        print('NE')