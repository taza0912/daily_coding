from sys import stdin

L, P = map(int, stdin.readline().split())
article_list = list(map(int, stdin.readline().split()))

for i in article_list:
    print("{} " .format(i - L*P), end="")