# ABC220-C
# https://atcoder.jp/contests/abc220/tasks/abc220_c

import bisect

n = int(input())
a = list(map(int, input().split()))
x = int(input())

# Aの塊が何回必要か
b = [0]*n
b[0] = a[0]
for i in range(1,n):
    b[i] = b[i-1]+a[i]
sa = b[-1]
na = x//sa
shift = len(a)*na
x = x-sa*na
# Aの中身で2分探索

ret = bisect.bisect_right(b, x)
ans = shift+ret+1

# 前後+-1を確かめる
if b[ret]-x<=0:
    ans += 1

print(ans)