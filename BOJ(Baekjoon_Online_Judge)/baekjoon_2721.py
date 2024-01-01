from sys import stdin

T = int(stdin.readline())
for i in range(T):
    n = int(stdin.readline())
    print(int((((n*(n+1)/2)**2)/2) + (n*(n+1)*(2*n+1)/4) + (n*(n+1)/2)))