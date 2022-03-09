t = int(input())
for i in range(t):
    if i == 0:
        print(' '*(t-i-1), end='')
        print('*')
    else:
        print(' '*(t-i-1), end='')
        print('*', end='')
        print(' '*(2*i-1), end='')
        print('*')