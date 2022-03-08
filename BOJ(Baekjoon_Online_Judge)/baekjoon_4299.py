from sys import stdin

A, B = map(int, stdin.readline().split())

if ((A-B) < 0) or (((A-B)%2) != 0):
    print(-1)
else:
    print((A+B)//2, A-(A+B)//2)


# from sys import stdin

# A, B = map(int, stdin.readline().split())
# if B == 0:
#     print(-1)
# elif A < B:
#     print(-1)
# elif A == B:
#     print(A, 0)
# elif (A+B)%2 != 0:
#     print(-1)
# elif (A-B)%2 != 0:
#     print(-1)
# else:
#     print(int((A+B)/2), int((A-B)/2))