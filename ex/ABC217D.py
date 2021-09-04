# ABC217-D
# https://atcoder.jp/contests/abc217/tasks/abc217_d

import bisect
import array

l, q = list(map(int, input().split()))
c = [0]*q
x = [0]*q
for i in range(q):
    c[i], x[i] = list(map(int, input().split()))
# 切断長さ配列で管理
w = array.array('i', [0,l])
for i in range(q):
    if c[i] == 1:
        bisect.insort(w,x[i])
    else:
        ind = bisect.bisect(w,x[i])
        print(w[ind]-w[ind-1])