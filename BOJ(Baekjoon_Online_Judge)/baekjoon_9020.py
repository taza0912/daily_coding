from sys import stdin

def sosu(num):
    result = []
    for i in range(2, num+1):
        counts = 0
        for j in range(1, i+1):
            if i%j == 0:
                counts += 1
        if counts == 2:
            result.append(i)
    return result

T = int(stdin.readline())

for i in range(T):
    n = int(stdin.readline())
    result1 = 0
    result2 = 0
    nlist = sosu(n)
    for j in range(int(len(nlist)/2)+1):
        for k in range(j, len(nlist)):
            if nlist[j] + nlist[k] == n:
                result1 = nlist[j]
                result2 = nlist[k]
    print("{0} {1}" .format(result1, result2))




# 1st)
# from sys import stdin

# def sosu(num):
#     counts = 0
#     for i in range(1, int(num/2)+1):
#         if num%i == 0:
#             counts += 1
#     if counts == 1:
#         return True
#     else:
#         return False

# def sosu_list(tn):
#     result = []
#     for i in range(2, int(tn/2)):
#         if sosu(i) == True:
#             result.append(i)
#     return result

# T = int(stdin.readline())

# for i in range(T):
#     n = int(stdin.readline())
#     slist = sosu_list(n)
#     result1 = 0
#     result2 = 0
#     for j in range(len(slist)):
#         for k in range(j, len(slist)):
#             if slist[j] + slist[k] == n:
#                 result1 = slist[j]
#                 result2 = slist[k]
#     print("{0} {1}" .format(result1, result2))