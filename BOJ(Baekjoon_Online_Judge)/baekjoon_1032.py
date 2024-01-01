# N = int(input())
# s_list = []
# for i in range(N):
#     val = list(input()[::-1])
#     s_list.append(val)
#     temp = len(val)

# for j in range(temp):
#     t_list = sorted([s_list[k].pop() for k in range(N)])
#     if t_list[0] != t_list[-1]:
#         print("?", end="")
#     else:
#         print(t_list[0], end="")

N = int(input())
S = list(input())
temp = len(S)
for i in range(N-1):
    x = list(input())
    for j in range(temp):
        if S[j] != x[j]:
            S[j] = "?"

print("".join(S))