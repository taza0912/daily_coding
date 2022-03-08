def split_string(string, idx):
    

def idx_count(string, idx):
    global split_idx
    split_idx = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
    result = 0
    for i in split_idx:
        result += len(string.split(idx)) -1
    return result

S = input()
result = 0
for i in split_idx:


s = 'abcdefg'
print(s.split('a'))





# for i in split_idx:



# W = input()

# check_list = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
# counts = len(W)

# for i in check_list:
#     m = 1
#     if len(i) == 3:
#         m += 1
#     if i in W:
#         counts -= m

# print(counts)

# counts = len(W)
# t = len(W)-1
# for i in range(t):
#     if W[i] == "c":
#         # c=, c-
#         if W[i+1] == "=" or W[i+1] == "-":


#     elif W[i] == "d":
#         # dz=, d-
#         if W[i+1] == ""
#     elif W[i] == "l":
#         # lj
#         if W[i+1] == ""
#     elif W[i] == "n":
#         # nj
#         if W[i+1] == ""
#     elif W[i] == "s":
#         # s=
#         if W[i+1] == ""
#     elif W[i] == "z":
#         # z=
#         if W[i+1] == "=":

#     else:

# print(W)