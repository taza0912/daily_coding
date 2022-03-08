from sys import stdin

K, D, A = map(int, stdin.readline().split('/'))
if K+A >= D and D!=0:
    print('gosu')
else:
    print('hasu')