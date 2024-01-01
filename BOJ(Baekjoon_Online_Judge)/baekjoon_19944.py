from sys import stdin

N, M = map(int, stdin.readline().split())
if M < 3:
    print("NEWBIE!")
elif M <= N:
    print("OLDBIE!")
else:
    print("TLE!")