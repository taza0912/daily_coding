# print(ord(" ")-64)
while (True):
    val = input()
    if val == "#":
        break
    else:
        result = 0
        for i in range(len(val)):
            if val[i] != " ":
                result += (i+1)*(ord(val[i])-64)
        print(result)
        continue
