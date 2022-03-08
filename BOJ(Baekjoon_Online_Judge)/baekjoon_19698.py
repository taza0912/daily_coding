from sys import stdin

n, w, h, l = map(int, stdin.readline().split())
val = (w//l)*(h//l)
print(min(val, n))