# ABC224-D
# https://atcoder.jp/contests/abc224/tasks/abc224_d

from collections import deque

m = int(input())
e = [[] for _ in range(9)]
for i in range(m):
    u, v = list(map(int, input().split()))
    e[u-1].append(v-1)
    e[v-1].append(u-1)

p = list(map(int, input().split()))
p = [i-1 for i in p]
now = [-1]*9  # 頂点0~8にあるコマ番号を保管（空きは-1）
for i in range(8):
    now[p[i]] = i

g = deque()
g.append((now,0))
goal = [0,1,2,3,4,5,6,7,-1]
done = set()
flag = True
while(g):
    cand = g.popleft()
    cand_now = cand[0]
    cand_nam = cand[1]
    if cand_now==goal:
        print(cand_nam)
        flag = False
        break
    else:
        emp = cand_now.index(-1)  # 空きの頂点
        next_change = e[emp]
        for i in next_change:
            # 交換
            cand_next = cand_now.copy()
            cand_next[emp] = cand_next[i]
            cand_next[i] = -1
            s = list(map(str,cand_next))
            s = "".join(s)
            if not(s in done):
                done.add(s)
                g.append((cand_next,cand_nam+1))
if flag:
    print(-1)