# 典型90問076
# https://atcoder.jp/contests/typical90/tasks/typical90_bx

import bisect

n = int(input())
a = list(map(int, input().split()))

s = sum(a)

# 長さ2倍の累積配列を考える
b = [a[0]]
for i in range(1,n):
    b.append(b[-1]+a[i])
for i in range(n):
    b.append(b[-1]+a[i])
    
# b[j]-b[i]=s/10となるi,jの組があるかを探索する
# b[j]=b[i]+s/10を探す
find = False
for i in range(n):
    val = bisect.bisect(b, b[i]+s/10)
    if b[val-1] == b[i]+s/10:
        print("Yes")
        find = True
        break

if not(find):
    print("No")