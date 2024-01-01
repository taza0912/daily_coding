from sys import stdin

N = int(stdin.readline())

dot_list = list(map(int, stdin.readline().split()))
dot_set = sorted(set(dot_list))
dot_doc = {dot_set[i]: i for i in range(len(dot_set))}
for j in range(N):
    print(dot_doc[j], end=" ")