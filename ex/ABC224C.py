# ABC224-C
# https://atcoder.jp/contests/abc224/tasks/abc224_c

import itertools

n = int(input())
p = [list(map(int, input().split())) for _ in range(n)]

# 三角形か判定関数
def judge(cnd):
    p1 = p[cnd[0]]
    p2 = p[cnd[1]]
    p3 = p[cnd[2]]
    
    dx1 = p2[0]-p1[0]
    dx2 = p3[0]-p1[0]
    dy1 = p2[1]-p1[1]
    dy2 = p3[1]-p1[1]
    if dx2*dy1==dx1*dy2:
        return False
    else:
        return True

# 全組み合わせ判定
cands = list(itertools.combinations(range(n), 3))
ans = 0
for cand in cands:
    if judge(cand):
        ans += 1

print(ans)