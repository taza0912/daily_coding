from sys import stdin

B1 = int(stdin.readline(), 2)
B2 = int(stdin.readline(), 2)

print(bin(B1*B2)[2:])