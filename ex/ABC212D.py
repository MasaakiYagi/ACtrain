# ABC212-D
# https://atcoder.jp/contests/abc212/tasks/abc212_d

import heapq

q = int(input())
offset = 0
que = []
for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        heapq.heappush(que, query[1] - offset)
    elif query[0] == 2:
        offset += query[1]
    else:
        print(heapq.heappop(que) + offset)

