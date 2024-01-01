import sys

while(True):
    n = int(sys.stdin.readline())
    if n != 0:
        answer = 0
        for i in range(n+1, 2*n+1):
            counts = 0
            for j in range(1, i+1):
                if i%j == 0:
                    counts += 1
            if counts == 2:
                answer += 1
        print(answer)
    else:
        break

# def count_sosu(n):



# while(True):
#     n = int(sys.stdin.readline())
#     if n == 0:
#         break

#     elif n < 7:
#         result = []
#     else:
#         result = []