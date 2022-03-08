# 첫 번째 숫자가 두 번째 숫자의 약수라면 factor
#                               배수라면 multiple
#                               둘 다 아니라면 neither
from sys import stdin

while True:
    A, B = map(int, stdin.readline().split())
    if A == 0:
        break
    elif B%A == 0:
        print("factor")
    elif A%B == 0:
        print("multiple")
    else:
        print("neither")
