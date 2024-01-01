from sys import stdin

# 동전종류: 1 ≤ N ≤ 10
# 만들어야 하는 금액: 1 ≤ K ≤ 100,000,000
N, K = map(int, stdin.readline().split())

coin_list = []
for i in range(N):
    coin_list.append(int(stdin.readline()))

coin = 0
idx = -1
while K != 0:
    if K//coin_list[idx] > 0:
        coin += K//coin_list[idx]
        K = K%coin_list[idx]
    else:
        idx -= 1

print(coin)

# coin_doc = {}
# for i in range(N):
#     coin_doc[int(stdin.readline())] = 0

# print(coin_doc)
# coin_doc = reversed(coin_doc)
# print(coin_doc)
# for i in coin_doc[::-1]: