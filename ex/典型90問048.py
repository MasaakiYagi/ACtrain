# 典型90問048
# https://atcoder.jp/contests/typical90/tasks/typical90_av


import heapq

n, k = list(map(int, input().split()))
c = []
for i in range(n):
    a, b = list(map(int, input().split()))
    a, b = -a, -b
    heapq.heappush(c, b)
    heapq.heappush(c, a-b)

ans = 0
for i in range(k):
    ans += heapq.heappop(c)

ans = -ans
print(ans)