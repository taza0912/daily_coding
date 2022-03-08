import sys

N = int(sys.stdin.readline())

dot_list = []
for i in range(N):
    dot = list(map(int, sys.stdin.readline().split()))
    dot_list.append(dot)

dot_list = sorted(dot_list)
for j in range(N):
    for x in dot_list[j]:
        print(x, end=" ")
    print()

# import sys

# N = int(sys.stdin.readline())

# dot_list = []
# for i in range(N):
#     dot = list(map(int, sys.stdin.readline().split()))
#     dot_list.append(dot[::-1])

# dot_list = sorted(dot_list)
# for j in range(N):
#     dot_list[j] = dot_list[j][::-1]
#     for y in dot_list[j]:
#         print(y, end=" ")
#     print()