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

import networkx

m = int(input())
e = [list(map(int, input().split())) for _ in range(m)]
p = list(map(int, input().split()))

# 正しい場所への最小移動回数の総和+1?
