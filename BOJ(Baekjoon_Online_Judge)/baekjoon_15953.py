from sys import stdin

nlist = list(range(1, 22))
reward_2017 = {}
t = 1
for i in [5000000, 3000000, 2000000, 500000, 300000, 100000]:
    reward_2017[i] = nlist[:t]
    nlist = nlist[t:]
    t += 1

nlist = list(range(1, 32))
reward_2018 = {}
t = 0
for i in [5120000, 2560000, 1280000, 640000, 320000]:
    reward_2018[i] = nlist[:2**t]
    nlist = nlist[2**t:]
    t += 1

t = int(stdin.readline())
for i in range(t):
    a, b = map(int, stdin.readline().split())
    result = 0
    for key, value in reward_2017.items():
        if a in value:
            result += key
    for key, value in reward_2018.items():
        if b in value:
            result += key
    print(result)