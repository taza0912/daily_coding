result = 0
for i in range(1, 9):
    val = input()
    if i%2 != 0:
        result += val[0::2].count('F')
    else:
        result += val[1::2].count('F')
print(result)