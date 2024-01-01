from sys import stdin

# def f_count(x):
#     result = 0
#     if x == 1:
#         result += 1 + (x+1)*3 - 2
#     else:
#         result += f_count(x-1) + (x+1)*3 -2
#     return result

# print(f_count(int(stdin.readline()))%45678)

n = int(stdin.readline())
a = 1
for i in range(n):
    a += (3*i) + 4
print(a%45678)