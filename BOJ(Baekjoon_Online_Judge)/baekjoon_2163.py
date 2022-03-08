from sys import stdin

def cut(S):
    if S == 1:
        result = 0
    elif S == 2:
        result = 1
    while S > 1:
        result += 1
        result += cut(S/2)*2
    return result

N, M = map(int, stdin.readline().split())
print(cut(N*M))