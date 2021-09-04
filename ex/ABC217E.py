# ABC217-E
# https://atcoder.jp/contests/abc217/tasks/abc217_e

import heapq
from collections import deque

q = int(input())
w = deque()
h = []
bf = []
for _ in range(q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        w.append(q[1])
    elif (q[0] == 2):
        if not(h) and len(w)>0:
            # heapソートされたものがないときはwからpop
            print(w.popleft())
        else:
            # heapソートされたものがあるときは，heappop
            print(heapq.heappop(h))
    elif (q[0] == 3) and len(w)>0:
        for i in range(len(w)):
            heapq.heappush(h, w.popleft())