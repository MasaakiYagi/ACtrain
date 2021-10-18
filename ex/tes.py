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

n = int(input())
a = list(map(int, input().split()))

tot = sum(a)
a.extend(a)
flag = False
c = 0
l = 0
r = 0
c = a[0]
for i in range(1,2*n):
    if c<tot/10:
        r += 1
        c += a[r]
    elif c>tot/10:
        while(c>tot/10 and l<=r):
            l += 1
            c -= a[l]
    elif c==tot/10:
        flag = True

if flag:
    print("Yes")
else:
    print("No")
    