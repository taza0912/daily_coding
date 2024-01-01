import sys

#  M ≤ N
M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

nums = list(range(M, N+1))
print(nums)

for i in nums:
    counts = 0
    for j in range(1, i+1):
        if i%j == 0:
            counts += 1
    # if counts == 2:


# 2nd
# answer_list = []

# for i in range(M, N+1):
#     counts = 0
#     for j in range(1, i+1):
#         if i%j == 0:
#             counts += 1
#             if counts > 2:
#                 continue
#     if counts == 2:
#         answer_list.append(i)

# if len(answer_list) > 0:
#     answer_sum = 0
#     for k in answer_list:
#         answer_sum += k
#     print(answer_sum)
#     print(answer_list[0])
# else:
#     print(-1)


# 1st
# answer_sum = 0
# answer_min = []
# for i in range(M, N+1):
#     counts = 0
#     for j in range(1, i+1):
#         if i%j == 0:
#             counts += 1
#         if counts > 2:
#             continue
#     if counts == 2:
#         answer_sum += i
#         answer_min.append(i)

# if answer_sum == 0:
#     print(-1)
# else:
#     print(answer_sum)
#     print(min(answer_min))