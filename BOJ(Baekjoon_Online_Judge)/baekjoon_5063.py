from sys import stdin

n = int(stdin.readline())
for i in range(n):
    r, e, c = map(int, stdin.readline().split())
    if r > e-c:
        print('do not advertise')
    elif r < e-c:
        print('advertise')
    else:
        print('does not matter')