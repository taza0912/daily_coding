n = int(input())
n_list = [0, 1]
for i in range(2, n+1):
    n_list.append(n_list[-1] + n_list[-2])

print(n_list[n])

# def p(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         result = p(n-1) + p(n-2)
#         return result
    
# n = int(input())
# print(p(n))