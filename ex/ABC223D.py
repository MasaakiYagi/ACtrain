# ABC223-D
# https://atcoder.jp/contests/abc223/tasks/abc223_d

import heapq

n, m = list(map(int, input().split()))
e = [[] for _ in range(n)]
jisu = [0]*n
for i in range(m):
    a, b = list(map(int, input().split()))
    e[a-1].append(b-1)
    jisu[b-1] += 1

# 次数0の管理配列
s = []
for i in range(n):
    if jisu[i]==0:
        heapq.heappush(s, i)

ans = []
while(len(s)>0):
    # sの中で最小の数をansに追加
    now = heapq.heappop(s)
    ans.append(now)
    
    # nowがつながっていた頂点の次数を減らす，次数が0になったらsに追加
    for i in e[now]:
        jisu[i] -= 1
        if jisu[i]==0:
            heapq.heappush(s,i)

if len(ans)==n:
    ans = [x+1 for x in ans]
    print(*ans)
else:
    print(-1)