from sys import stdin
import random
import math

n = int(stdin.readline())

if n == 0:
    print("divide by zero")
else:
    nlist = list(map(int, stdin.readline().split()))
    val = 0
    for i in nlist:
        val += i*(1/len(nlist))
    print(f"{(sum(nlist)/len(nlist))/val:.2f}")