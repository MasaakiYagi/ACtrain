# ABC223-C
# https://atcoder.jp/contests/abc224/tasks/abc223_c

import bisect

n = int(input())
a = [0]*n
b = [0]*n
for i in range(n):
    a[i], b[i] = list(map(int, input().split()))

sa = [0]*n  # 距離の累積配列
st = [0]*n  # 時間の累積配列
for i in range(n):
    if i==0:
        sa[i] = a[i]
        st[i] = a[i]/b[i]
    else:
        sa[i] = sa[i-1]+a[i]
        st[i] = st[i-1]+a[i]/b[i]

sumt = st[-1]  # 全体時間
hsumt = sumt/2  # 半分の時間＝左右の火がぶつかる時間

# にぶたんで何本目の導火線でぶつかるか探索
ind = bisect.bisect_right(st,hsumt)

# ind-1~indの間で，導火線がぶつかる時間割合
if ind==0:
    f = hsumt/st[ind]
else:
    f = (hsumt-st[ind-1])/(st[ind]-st[ind-1])

# 導火線がぶつかる距離
if ind==0:
    ans = sa[ind]*f
else:
    ans = sa[ind-1] + (sa[ind]-sa[ind-1])*f
print(ans)