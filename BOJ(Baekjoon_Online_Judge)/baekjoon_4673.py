# # def check_selfNumber(n):
# #     check = True
# #     for i in range(1, n+1):
# #         m = i
# #         x = str(i)
# #         for j in range(len(x)):
# #             m += int(x[j])
# #         if m == n:
# #             check = False
# #     if check == True:
# #         return n

# def d(n):
#     if len(str(n)) == 1:
#         for y in range(10):
#             if 2*y == n:
#                 return False
#     elif len(str(n)) == 2:
#         for x in range(10):
#             for y in range(10):
#                 if 11*x + 2*y == n:
#                     return False
#     elif len(str(n)) == 3:
#         for j in range(10):
#             for x in range(10):
#                 for y in range(10):
#                     if 101*j + 11*x + 2*y == n:    
#                         return False
#     else:
#         for i in range(10):
#             for j in range(10):
#                 for x in range(10):
#                     for y in range(10):
#                         if 1001*i + 101*j + 11*x + 2*y == n:
#                             return False
#     return n

# for i in range(1, 9999):
#     if d(i) != False:
#         print(d(i))

numSet = set(range(1, 10001))
checkNums = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    checkNums.add(i)

self_nums = sorted(numSet - checkNums)

for i in self_nums:
    print(i)