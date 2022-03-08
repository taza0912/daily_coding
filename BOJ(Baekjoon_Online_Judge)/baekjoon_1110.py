import sys

# 0 <= N <= 99
N = int(sys.stdin.readline())

def change(n):
    new_n = str(n)
    if len(new_n) < 2:
        new_n = "0" + new_n
    
    return int(new_n[-1] + str(int(new_n[0]) + int(new_n[1]))[-1])

counts = 0
N_2 = change(N)
while True:
    counts += 1
    if N != N_2:
        N_2 = change(N_2)
        continue
    else:
        print(counts)
        break


# def change(n):
#     new_n = str(n)
#     counts = 0
#     if len(new_n) < 2:
#         new_n = "0" + new_n
    
#     new_n = new_n[-1] + str(int(new_n[0]) + int(new_n[1]))[-1]
#     counts += 1

#     while new_n != str(n):
#         counts += change(int(new_n))
    
#     return counts

# print(change(N))