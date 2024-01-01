# 1 ≤ H, W ≤ 99
# 방 번호는 YXX 나 YYXX 형태인데
# 여기서 Y 나 YY 는 층 수를 나타내고
#  XX 는 엘리베이터에서부터 세었을 때의 번호

import sys

T = int(sys.stdin.readline())

for i in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    # 층
    X = 1
    while N-H > 0:
        X += 1
        N -= H
    Y = N
    print("{0}{1:02}" .format(Y, X))