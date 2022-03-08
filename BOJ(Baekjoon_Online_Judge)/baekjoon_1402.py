from sys import stdin

def y(n):
    result = []
    for i in range(1, n+1):
        if n%i == 0:
            result.append(i)
    return result

def x(nlist: list, v:int):
    result = ""
    for i in nlist[:-1]:
        for j in nlist[1:]:
            if i+j == v:
                result = "yes"
                return result
    result = "no"
    return result


T = int(input())
for i in range(T):
    A, B = map(int, stdin.readline().split())
    tmp = y(A)
    print(x(tmp, B))
    continue