from sys import stdin

A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

result = 0
if A < 0:
    result += abs(A)*C
    A = 0
if A == 0:
    result += D + E*B
else:
    result += E*(B-A)
print(result)