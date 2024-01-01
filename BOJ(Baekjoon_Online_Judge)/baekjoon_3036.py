from sys import stdin

N = int(stdin.readline())

c_list = list(map(int, stdin.readline().split()))

for i in range(1, len(c_list)):
    A = c_list[0]
    B = c_list[i]
    x = 2
    while B != 1:
        if A%x==0 and B%x==0:
            A = A//x
            B = B//x
        elif x == B:
            break
        else:
            x += 1
    print("{0}/{1}" .format(A, B))