from sys import stdin

while True:
    result = sum(list(map(int, stdin.readline().split())))
    if result == 0:
        break
    else:
        print(result)