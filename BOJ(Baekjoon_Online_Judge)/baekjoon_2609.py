from sys import getallocatedblocks, stdin

A, B = map(int, stdin.readline().split())

def GCD(a, b):
    if a > b:
        result = b
    else:
        result = a
    for i in range(result, 0, -1):
        if a%result==0 and b%result==0:
            return result
        else:
            result -= 1

def LCM(a, b):
    return int((a*b)/GCD(a, b))


print(GCD(A, B))
print(LCM(A, B))