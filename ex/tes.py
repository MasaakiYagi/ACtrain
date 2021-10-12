# 割り算の整数部分ほしいなら//
# bit_shiftなら
    # <<左シフト
    # >>右シフト
# list(map(int, input().split()))
# int(input())

# 再帰の回数上限撤廃（再帰使うならPythonで通そう）
# import sys
# sys.setrecursionlimit(10**8)

import bisect

inf = 10**10

n = int(input())
a = list(map(int, input().split()))
q = int(input())
b = [int(input()) for _ in range(q)]

a = sorted(a)

# にぶたんで一番近いクラスを探索
for i in range(q):
    ind = bisect.bisect_left(a, b[i])
    cand1 = inf if ind==n else abs(a[ind]-b[i])
    cand2 = inf if ind==0 else abs(a[ind-1]-b[i])
    print(min(cand1,cand2))