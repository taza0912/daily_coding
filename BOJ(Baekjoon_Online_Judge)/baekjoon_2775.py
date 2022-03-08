import sys

# def counts(k, n):
#     result = 0
#     if k == 1:
#         result = int((n*n + n)/2)
#     else:
#         for i in range(1, n+1):
#             result += counts(k-1, i)
#     return result

T = int(sys.stdin.readline())

for i in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    # print(counts(k, n))

    counts = [i for i in range(1, n+1)]
    for y in range(k):
        for x in range(1, n):
            counts[x] += counts[x-1]
    print(counts[-1])