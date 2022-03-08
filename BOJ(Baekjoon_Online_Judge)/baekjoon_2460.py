from sys import stdin

result = []
people = 0
for i in range(10):
    val = list(map(int, stdin.readline().split()))
    people -= val[0]
    people += val[1]
    result.append(people)
print(max(result))