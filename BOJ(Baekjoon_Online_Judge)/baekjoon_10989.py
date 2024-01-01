from sys import stdin

N = int(stdin.readline())

array = []
for i in range(N):
    n = int(stdin.readline())
    if array[-1] == False:
        array.append(n)
    else:
        k = -1
        for j in ranage(len(array)):
            if n < array[k]:
                k -= 1
        array.insert(k, n)
        
for i in array:
    print(i)