from sys import stdin

result = list(map(int, stdin.readline().split()))[1]
result_list = [result]
for i in range(3):
    val = list(map(int, stdin.readline().split()))
    result += val[1]-val[0]
    result_list.append(result)
print(max(result_list))