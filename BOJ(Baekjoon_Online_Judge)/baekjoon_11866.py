from sys import stdin

# a = lambda x: x+2
# print(a(3))

def josephus(n_list: list, k: int):
    result = []
    if len(n_list) < k:
        tmp = len(n_list)
        for i in range(tmp):
            val = tmp
            result.append(n_list.pop((k//val)-1))
    else:
        result.append(n_list.pop(k-1))
        n_list_2 = n_list[k-1:] + n_list[:k-1]
        result += josephus(n_list_2, k)
    return result

N, K = map(int, stdin.readline().split())
N_LIST = [i for i in range(1, N+1)]

a = josephus(N_LIST, K)
answer = list(map(str, a))
answer = ", ".join(answer)
print("<{}>" .format(answer))

# print("<", end="")
# for i in range(len(answer)-1):
#     print(answer[i], end=", ")
# print("{}>" .format(answer[-1]))



# def ys(n, k):
#     n_list = [i for i in range(1, N+1)]
#     temp = len(n_list)
#     result_list = []
#     while temp > 0:
#         result_list.append(n_list.pop(k-1))
#         temp -= 1
#         n_list = n_list[k-1:] + n_list[:k-1]



# N, K = map(int, stdin.readline().split())



# for i in range(N):

