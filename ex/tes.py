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
t = [0]*(n+1)
e = [[] for _ in range(n+1)]
for i in range(1,n+1):
    x = list(map(int, input().split()))
    for j in range(len(x)):
        if j == 0:
            t[i] = x[j]
        elif j == 1:
            k = x[j]
        else:
            e[i].append(x[j])
            e[x[j]].append(i)

# 技nからbfsで葉までを探索，最も総時間の少ないルートの時間をansとする