# 割り算の整数部分ほしいなら//
# bit_shiftなら
    # <<左シフト
    # >>右シフト
# list(map(int, input().split()))
# int(input())

# 再帰の回数上限撤廃（再帰使うならPythonで通そう）
# import sys
# sys.setrecursionlimit(10**8)
# import itertools

import bisect

n = int(input())
a = list(map(int, input().split()))

s = sum(a)

b = [0]*(2*n)
for i in range(2*n):
    if i == 0:
        b[i] = a[i]
    else:
        b[i] = b[i-1]+a[i%n]

# bの配列にてb[j]-b[i]=s/10となるi,jの組みを見つける
# b[j]=b[i]+s/10となるiに対するjを見つける
flag = True
for i in range(n):
    ind = bisect.bisect_left(b, b[i]+s/10)
    if b[ind]==b[i]+s/10:
        print("Yes")
        flag = False
        break

if flag:
    print("No")