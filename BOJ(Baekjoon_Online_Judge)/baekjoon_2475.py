from sys import stdin

n_list = list(map(int, stdin.readline().split()))

result = 0

for i in n_list:
    result += i**2

print(result%10)