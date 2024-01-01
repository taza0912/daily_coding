from sys import stdin

c_list = [1, 1, 2, 2, 2, 8]
t = list(map(int, stdin.readline().split()))

for i in range(6):
    print(c_list[i] - t[i], end=" ")

# k, q, l, b, n, p = map(int, stdin.readline().split())

# print("{} {} {} {} {} {}" .format(1-k, 1-q, 2-l, 2-b, 2-n, 8-p))