from sys import stdin

a_x, a_y, a_z = map(int, stdin.readline().split())
b_x, b_y, b_z = map(int, stdin.readline().split())

print(b_x-a_z, b_y//a_y, b_z-a_x)