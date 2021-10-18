# 典型90問064
# https://atcoder.jp/contests/typical90/tasks/typical90_bl

n, q = list(map(int, input().split()))
a = list(map(int, input().split()))
t = [list(map(int, input().split())) for _ in range(q)]

# まず差分配列を作る
da = [0]*(n-1)
huben = 0
for i in range(n-1):
    da[i] = a[i+1]-a[i]
    huben += abs(da[i])

# 地殻変動毎に差分を計算
for i in t:
    l, r, v = i
    l, r = l-1, r-1
    temp = 0
    if l>0:
        temp -= abs(da[l-1])
        da[l-1] += v
        temp += abs(da[l-1])
    if r<(n-1):
        temp -= abs(da[r])
        da[r] -= v
        temp += abs(da[r])
    huben += temp
    print(huben)