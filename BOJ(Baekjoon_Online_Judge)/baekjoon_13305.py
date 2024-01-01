# 제일 왼쪽의 도시에서
# 제일 오른쪽의 도시로 자동차를 이용하여 이동
# 처음 출발할 때 자동차에는 기름이 없어서
# 주유소에서 기름을 넣고 출발
# 도로를 이용하여 이동할 때 1km마다 1리터의 기름을 사용
# 각 도시에는 단 하나의 주유소가 있으며,
# 도시 마다 주유소의 리터당 가격은 다를 수 있음
# 원 안에 있는 숫자는 그 도시에 있는 주유소의 리터당 가격
# 도로 위에 있는 숫자는 도로의 길이

# 첫 번째 줄: 도시의 개수를 나타내는 정수 N
# (2 ≤ N ≤ 100,000)
# 다음 줄에는 인접한 두 도시를 연결하는 도로의 길이
# (제일 왼쪽 도로부터 N-1개의 자연수)
# 다음 줄에는 주유소의 리터당 가격

from sys import stdin

N = int(stdin.readline())
S = list(map(int, stdin.readline().split()))
oil_price = list(map(int, stdin.readline().split()))

# total_price = 0
# for i in range(N-1):
#     l = 0
#     if i == 0:
#         total_price += oil_price[i]*S[i]
#     else:
#         for j in range(i+1, N):
#             if oil_price[i] < oil_price[j]:




# cheapest_idx = oil_price.index(min(oil_price[:-2]))



# idx = 0
# while idx < N-1:
#     idx_b = idx+1
#     if oil_price[idx] < oil_price[idx_b]:
