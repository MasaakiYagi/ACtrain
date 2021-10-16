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

n, q = list(map(int, input().split()))
a = list(map(int, input().split()))
t = [0]*q
x = [0]*q
y = [0]*q
for i in range(q):
    t[i], x[i], y[i] = list(map(int, input().split()))

shift = 0
for i in range(q):
    if t[i] == 1:
        xn = (x[i]-1-shift)%n
        yn = (y[i]-1-shift)%n
        temp = a[xn]
        a[xn] = a[yn]
        a[yn] = temp
    elif t[i] == 2:
        shift += 1
    elif t[i] == 3:
        xn = (x[i]-1-shift)%n
        print(a[xn])