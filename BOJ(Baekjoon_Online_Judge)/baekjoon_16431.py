from sys import stdin

B = list(map(int, stdin.readline().split()))
D = list(map(int, stdin.readline().split()))
J = list(map(int, stdin.readline().split()))

tmp = [max(abs(B[0]-J[0]), abs(B[1]-J[1])), abs(D[0]-J[0])+abs(D[1]-J[1])]
result = ''
if tmp[0] < tmp[1]:
    result = 'bessie'
elif tmp[0] > tmp[1]:
    result = 'daisy'
else:
    result = 'tie'

print(result)