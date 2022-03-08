from sys import stdin

T = int(stdin.readline())

button_counts = {'A': 0,
                 'B': 0,
                 'C': 0}

while T > 0:
    if T%10 != 0:
        break
    elif T >= 300:
        button_counts['A'] += 1
        T -= 300
    elif T >= 60:
        button_counts['B'] += 1
        T -= 60
    else:
        button_counts['C'] += 1
        T -= 10

result = list(button_counts.values())
if result.count(0) == 3:
    print(-1)
else:
    for i in result:
        print(i, end=" ")