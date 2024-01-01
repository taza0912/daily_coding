from sys import stdin

a_list = []
b_list = []
for i in range(5):
    if i < 3:
        a_list.append(int(stdin.readline()))
    else:
        b_list.append(int(stdin.readline()))

print(min(a_list) + min(b_list) - 50)