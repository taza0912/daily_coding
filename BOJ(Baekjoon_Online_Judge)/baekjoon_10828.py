from sys import stdin

N = int(stdin.readline())

nlist = []
for i in range(N):
    cmd = list(map(str, stdin.readline().split()))
    if cmd[0] == "push":
        nlist.append(cmd[1])
    elif cmd[0] == "pop":
        if len(nlist) == 0:
            print(-1)
        else:
            print(nlist.pop())
    elif cmd[0] == "size":
        print(len(nlist))
    elif cmd[0] == "empty":
        if len(nlist) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == "top":
        if len(nlist) == 0:
            print(-1)
        else:
            print(nlist[-1])