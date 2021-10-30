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
# import bisect
# from collections import deque


n = int(input())
p = []
for i in range(n):
    x, y = list(map(int, input().split()))
    p.append([x,y,x+y])

p = sorted(p, key=lambda x:x[2])
take = [p[-1]]
for i in range(1,n):
    # n-1-iを判定し，追加
    cand = p[n-1-i]
    flag = True
    for j in take:
        p0x, p0y = 0,0
        p1x, p1y = j[0]-1,j[1]
        p2x, p2y = j[0],j[1]-1
        px, py = cand[0]-1,cand[1]
        area = 0.5 *(-p1y*p2x + p0y*(-p1x + p2x) + p0x*(p1y - p2y) + p1x*p2y)
        s = 1/(2*area)*(p0y*p2x - p0x*p2y + (p2y - p0y)*px + (p0x - p2x)*py)
        t = 1/(2*area)*(p0x*p1y - p0y*p1x + (p0y - p1y)*px + (p1x - p0x)*py)
        if (0 < s < 1) and (0 < t < 1) and (0<1-s-t<1):
            flag = False
        px, py = cand[0],cand[1]-1
        area = 0.5 *(-p1y*p2x + p0y*(-p1x + p2x) + p0x*(p1y - p2y) + p1x*p2y)
        s = 1/(2*area)*(p0y*p2x - p0x*p2y + (p2y - p0y)*px + (p0x - p2x)*py)
        t = 1/(2*area)*(p0x*p1y - p0y*p1x + (p0y - p1y)*px + (p1x - p0x)*py)
        if (0 <= s <= 1) and (0 <= t <= 1) and (0<=1-s-t<=1):
            flag = False
    if flag:
        take.append(cand)


print(len(take))