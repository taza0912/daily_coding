from sys import stdin

s_list = list(input().split("-"))

result = 0
for i in range(len(s_list)):
    num = 0
    if "+" not in s_list[i]:
        num += int(s_list[i])
    else:
        ilist = list(s_list[i].split("+"))
        for j in ilist:
            num += int(j)
    if i == 0:
        result += num
    else:
        result -= num

print(result)



# s_list = str(stdin.readline())
# result = []
# # 55-50+40 (8)(1, len(s)-1)
# idx_start = 0
# for i in range(1, len(s_list)-1):
#     if idx_start < len(s_list)-2




# idx_start = 0
# idx_end = -1
# for i in range(1, len(s_list)-1):
#     if idx_start < len(s_list)-2:
#         if s_list[i] == "-" or s_list[i] == "+":
#             idx_end = i-1
#     else:
#         idx_end = -1
        
#     result.append(int(s_list[idx_start:idx_end]))
#     idx_start = i+1

# print(result)




#