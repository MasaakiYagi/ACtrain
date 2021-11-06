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
a = list(map(int, input().split()))

# 状態保存DP
audp = [{"num":0,"hist":[]} for _ in range(n+1)]
agdp = [{"num":0,"hist":[]} for _ in range(n+1)]
audp[0]["num"] = 1

for i in range(n):
    candau = audp[i].copy()
    candag = agdp[i].copy()
    # 金の最大値
    if candau["num"]>candag["num"]/a[i]:
        # 何もしない方がいいとき
        audp[i+1]["num"] = candau["num"]
        audp[i+1]["hist"] = candau["hist"].copy()
        audp[i+1]["hist"].append(0)
    else:
        # 銀を交換した方がいいとき
        audp[i+1]["num"] = candag["num"]/a[i]
        audp[i+1]["hist"] = candag["hist"].copy()
        audp[i+1]["hist"].append(1)
    # 銀の最大値
    if candag["num"]>candau["num"]*a[i]:
        # 何もしない方がいいとき
        agdp[i+1]["num"] = candag["num"]
        agdp[i+1]["hist"] = candag["hist"].copy()
        agdp[i+1]["hist"].append(0)
    else:
        # 金を交換した方がいいとき
        agdp[i+1]["num"] = candau["num"]*a[i]
        agdp[i+1]["hist"] = candau["hist"].copy()
        agdp[i+1]["hist"].append(1)
print(*audp[-1]["hist"])
