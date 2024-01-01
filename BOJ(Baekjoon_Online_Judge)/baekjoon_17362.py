n = int(input())
t = n%8

if t in [6, 7]:
    print(10-t)
elif t == 0:
    print(2)
else:
    print(t)