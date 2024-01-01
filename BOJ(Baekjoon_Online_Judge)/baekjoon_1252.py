a, b = map(str, input().split())
print(bin(int(a, 2) + int(b, 2)))[2:]

# from sys import stdin

# a, b = map(int, stdin.readline().split())
# s_result = list(str(a + b))[::-1]
# ddd = 0
# for i in range(len(s_result)):
#     if ddd + int(s_result[i]) >= 2:
#         s_result[i] = int(s_result[i]) - 2
#         ddd = 1
# if ddd == 1:
#     s_result.append("1")

# print(int(''.join(s_result[::-1])))


# from sys import stdin

# a, b = map(int, stdin.readline().split())
# s_result = list(str(a + b))
# while "2" in s_result:
#     t = s_result[::-1]
#     bn = list("0"*(len(t)+1))
#     for i in range(len(t)):
#         if t[i] == "2":
#             t[i] = "0"
#             bn[i+1] = "1"
#     s_result = int(''.join(t[::-1])) + int(''.join(bn[::-1]))
# print(int(''.join(s_result)))

# a, b = map(input()[::-1])

# tmp_s = min(len(a), len(b))
# tmp_e = max(len(a), len(b))
# of = 0
# result = ""
# for i in range(tmp_s):
#     val = of + int(a[i]) + int(b[i])
#     if val >= 2:
#         result += str(val-2)
#         of = 1
#     else:
#         result += str(val)
#         of = 0
# if tmp_s == tmp_e:
#     if of == 1:
#         result += "1"
# else:
#     for j in range(tmp_s, tmp_e):
#         nn = of + 