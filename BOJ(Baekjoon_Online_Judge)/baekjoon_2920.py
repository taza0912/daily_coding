from sys import stdin

nlist = list(map(int, stdin.readline().split()))
result_list = []
for i in range(len(nlist)-1):
    if nlist[i] > nlist[i+1]:
        result_list.append(0)
    else:
        result_list.append(1)

if result_list.count(1) == 7:
    print('ascending')
elif result_list.count(0) == 7:
    print('descending')
else:
    print('mixed')