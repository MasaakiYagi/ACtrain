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
b = list(map(int, input().split()))
c = list(map(int, input().split()))

# 全て46で割ったあまりに変換し，その個数を管理する
newa = [0]*46
newb = [0]*46
newc = [0]*46
for i in range(n):
    newa[a[i]%46] += 1
    newb[b[i]%46] += 1
    newc[c[i]%46] += 1

ans = 0
for i in range(46):
    for j in range(46):
        for k in range(46):
            if (i+j+k)%46==0:
                ans += newa[i]*newb[j]*newc[k]

print(ans)