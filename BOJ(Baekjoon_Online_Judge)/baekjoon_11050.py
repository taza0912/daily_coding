from sys import stdin

def binomial_coefficient(n, k):
    result = 1
    if k != 0:
        c, p = 1, 1
        for i in range(k):
            c *= (n-i)
            p *= (i+1)
        result *= int(c/p)
    return result

N, K = map(int, stdin.readline().split())
print(binomial_coefficient(N, K))