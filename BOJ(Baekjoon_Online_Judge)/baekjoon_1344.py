a = int(input())
b = int(input())
c = {i for i in range(0, 19)}
d = {2, 3, 5, 7, 11, 13, 17}
temp = list(c-d)

result = 0
for i in temp:
    for j in temp:
        val = ((a/100)**i)*(((1-(a/100))**(18-i)))*((b/100)**j)*(((1-(b/100))**(18-j)))
        result += val
print("{:.16}" .format(1-result))