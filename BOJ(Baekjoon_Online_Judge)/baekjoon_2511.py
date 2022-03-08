from sys import stdin

a = list(map(int, stdin.readline().split()))
b = list(map(int, stdin.readline().split()))
result = []
for i in range(10):
    if a[i] == b[i]:
        result.append('D')
    elif a[i] > b[i]:
        result.append('A')
    else:
        result.append('B')

result_score = {'A': result.count('A')*3 + result.count('D'),
                'B': result.count('B')*3 + result.count('D'),
                'D': result.count('D')}

print(list(result_score.values())[0], list(result_score.values())[1])
if result_score['D'] == 10:
    print('D')
elif list(result_score.values())[0] != list(result_score.values())[1]:
    print(list(result_score.keys())[list(result_score.values()).index(max(list(result_score.values())))])
else:
    print(''.join(''.join(result).split('D'))[-1])