# 典型90問032
# https://atcoder.jp/contests/typical90/tasks/typical90_af

import itertools as it

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
xy = [list(map(int, input().split())) for _ in range(m)]
kenaku = [[False]*n for _ in range(n)]
for i in xy:
    kenaku[i[0]-1][i[1]-1] = True
    kenaku[i[1]-1][i[0]-1] = True

ans = 10001

# 順列全探索
cands = list(it.permutations(list(range(n))))
for cand in cands:
    # 噂判定
    flag = True
    for i in range(n-1):
        if kenaku[cand[i]][cand[i+1]]:
            flag = False
    if flag:
        # 時間計測
        time = 0
        k = 0
        for i in cand:
            time += a[i][k]
            k += 1
            
        if time<ans:
            ans = time

if ans == 10001:
    ans = -1

print(ans)
