import sys

T = int(sys.stdin.readline())

for i in range(T):
    RS = list(map(str, sys.stdin.readline().split()))
    answer = ""
    for j in RS[1]:
        answer += j*int(RS[0])
    
    print(answer)