from sys import stdin
import math

r, c, n = map(int, stdin.readline().split())
print(math.ceil(r/n)*math.ceil(c/n))