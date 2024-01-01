from sys import stdin

# 방학: L d_list[0]
# 국어: A d_list[1]
# 수학: B d_list[2]
# 국어 하루: C d_list[3]
# 수학 하루: D d_list[4]

d_list = []
for i in range(5):
    d_list.append(int(stdin.readline()))

result = []
for i in (1, 2):
    val = d_list[i]//d_list[i+2]
    result.append(val)
    if d_list[i]%d_list[i+2] != 0:
        result[i-1] += 1

print(d_list[0] - max(result))
