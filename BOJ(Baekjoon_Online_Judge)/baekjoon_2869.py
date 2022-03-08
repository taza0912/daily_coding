import sys

A, B, V = map(int, sys.stdin.readline().split())

days = (V-B)/(A-B)
print(int(days) if days == int(days) else int(days) + 1)



# 이와같은 코드는 부등식의 계산이 이루어지기 때문에
# 시간초과가 생긴다.
# 따라서 A,B,V가 입력되면
# 바로 답이 나오는 구조여야 한다.
# 위와 같은 코드는 K의 값을 점차 늘리기 때문에
# 결과적으로 K의 값만큼 while문을 반복한다.
# 하지만 if구문의 조건식,
# a*k-b*(k-1) => v 를 이항시켜 정리하면
# k>=(v-b)/(a-b)로 바꿀 수 있다.
# 이를 통해 k의 값을 바로 도출 할 수 있다.
# k,즉 일수를 최소화시켜야 한다.
# 따라서 k는 (v-b)/(a-b) 혹은 (v-b)//(a-b)+1이다.

# 1번째 시도
# def snail_move(a, b, c):
#     result = 0
#     while c > 0:
#         result += 1
#         c -= a
#         if c == 0:
#             break
#         else:
#             c += b
#     return result

# 2번째 시도
# def snail_move(a, b, c):
#     result = 0
#     if c == a:
#         result += 1
#     else:
#         c -= a - b
#         result += 1
#         result += snail_move(a, b, c)
#     return result

# 3번째 시도
# if A == V:
#     print(1)
# else:
#     counts = 1
#     days = 2
#     while True:
#         if V <= A + counts*(-B + A):
#             print(days)
#             break
#         else:
#             counts += 1
#             days += 1