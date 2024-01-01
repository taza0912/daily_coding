from sys import stdin

A, B = map(int, stdin.readline().split())
C = int(stdin.readline())

B += C
if B >= 60:
    A += B//60
    B = B%60
    if A >= 24:
        A -= 24

print(A, B)