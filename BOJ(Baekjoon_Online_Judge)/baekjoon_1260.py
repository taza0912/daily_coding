from sys import stdin

N, M, V = map(int, stdin.readline().split())

b_list = []
for  i in range(M):
    b_list.append(list(map(int, stdin.readline().split())))

n_list = [i for i in range(1, N+1)]


def DFS()