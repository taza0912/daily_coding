from sys import stdin

str_list = []
while(True):
    val = str(stdin.readline())[:-1]
    if val != "":
        str_list.append(val)
    else:
        for i in str_list:
            print(i)
        break