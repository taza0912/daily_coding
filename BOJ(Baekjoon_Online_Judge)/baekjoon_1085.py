import sys

x, y, w, h = map(int, sys.stdin.readline().split())

s_list = [x, w-x, h-y, y]

print(min(s_list))