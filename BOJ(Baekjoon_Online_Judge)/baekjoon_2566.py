from sys import stdin

nlist = []
for i in range(9):
    nlist.append(list(map(int, stdin.readline().split())))

max_nums = []
max_nums_index = []
for j in nlist:
    max_nums.append(max(j))
    max_nums_index.append(j.index(max(j)))

result = max(max_nums)
print(result)
print(max_nums.index(result)+1, max_nums_index[max_nums.index(result)]+1)