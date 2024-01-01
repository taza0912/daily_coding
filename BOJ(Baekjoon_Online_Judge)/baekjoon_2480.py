from sys import stdin

n_list = sorted(list(map(int, stdin.readline().split())))
min_num = n_list[0]
medium_num = n_list[1]
max_num = n_list[2]

count_num = n_list.count(medium_num)

if max_num == min_num:
    print(10000 + max_num*1000)
elif count_num == 2:
    print(1000 + medium_num*100)
else:
    print(max_num*100)