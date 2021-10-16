# 典型90問032
# https://atcoder.jp/contests/typical90/tasks/typical90_af

import itertools as it

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
xy = {}
for i in range(n+1):
    xy[i] = []
for i in range(m):
    x, y = list(map(int, input().split()))
    xy[x].append(y)
    xy[y].append(x)

# 探索組み合わせの列挙
cand = list(it.permutations(range(1,n+1)))

ans = 10**10
for i in cand:
    # 噂クリア確認
    ngflag = False
    for j in range(n-1):  # 一人ずつ噂に引っかかるかをチェック
        f = i[j]  # 渡す人
        t = i[j+1]  # 受け取る人
        if t in xy[f]:
            ngflag = True
        if f in xy[t]:
            ngflag = True
    if ngflag:
        pass
    else:
        time = 0
        for j in range(n):
            time += a[i[j]-1][j]
        ans = min(ans, time)

if ans == 10**10:
    ans = -1

print(ans)
