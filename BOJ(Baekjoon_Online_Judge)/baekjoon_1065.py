import sys

N = int(sys.stdin.readline())

counts = 0

# 1부터 N까지의 정수 중에서,,,
for i in range(1, N+1):
    # 각 자릿수의 차이가 일정한가요?
    if i < 100:
        counts += 1
    else:
        if 2*int(str(i)[1]) == int(str(i)[0]) + int(str(i)[2]):
            counts += 1

print(counts)