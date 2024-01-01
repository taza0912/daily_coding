from sys import stdin

def search_decomposition(n):
    decomposition_list = []
    for i in range(int(n/2), n):
        decomposition = i
        for j in range(len(str(i))):
            decomposition += int(str(i)[j])
        if decomposition == n:
            decomposition_list.append(i)
    
    if len(decomposition_list) == 0:
        return 0
    else:
        return min(decomposition_list)

N = int(stdin.readline())

print(search_decomposition(N))