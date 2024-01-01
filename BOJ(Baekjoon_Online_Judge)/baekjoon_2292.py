N = int(input())

if N == 1:
    print(1)
else:
    a = 1
    while (3*a*a - 3*a + 2) <= N:
        a += 1
    print(a)