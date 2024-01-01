from sys import stdin

mk_score = list(map(int, stdin.readline().split()))
ms_score = list(map(int, stdin.readline().split()))

def sum(a: list):
    result = 0
    for i in a:
        result += i
    
    return result

S = sum(mk_score)
T = sum(ms_score)
if S >= T:
    print(S)
else:
    print(T)