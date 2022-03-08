from sys import stdin

N = int(stdin.readline())

array = []
for i in range(N):
    n = int(stdin.readline())
    array.append(n)

for i in sorted(array):
    print(i)

# 1st)
# from sys import stdin

# N = int(stdin.readline())

# array = []
# for i in range(N):
#     n = int(stdin.readline())
#     if len(array) == 0:
#         array.append(n)
#     else:
#         k = -1
#         for j in range(-1, len(array)*(-1) -1, -1):
#             if array[j] >= n:
#                 k = j
#         array.insert(k, n)

# for i in array:
#     print(i)