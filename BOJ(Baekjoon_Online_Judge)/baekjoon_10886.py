from sys import stdin

T = int(stdin.readline())
a = {'Junhee is not cute!': 0,
     'Junhee is cute!': 0}
for i in range(T):
    val = int(stdin.readline())
    if val == 1:
        a['Junhee is cute!'] += 1
    else:
        a['Junhee is not cute!'] += 1

print(list(a.keys())[list(a.values()).index(max(list(a.values())))])