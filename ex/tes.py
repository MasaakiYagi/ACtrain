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

h, w = list(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(h)]
b = [list(map(int, input().split())) for _ in range(h)]

# 0~h-2,0~w-2までを一致させるよう処理し，h-1,w-1のL字成分が一致しているかを判定
ans = 0
for i in range(h-1):
    for j in range(w-1):
        sa = b[i][j]-a[i][j]
        a[i][j] += sa
        a[i+1][j] += sa
        a[i][j+1] += sa
        a[i+1][j+1] += sa
        ans += abs(sa)

flag = True
for i in range(h):
    if not(a[i][-1]==b[i][-1]):
        flag = False
for i in range(w):
    if not(a[-1][j]==b[-1][j]):
        flag = False

if flag:
    print("Yes")
    print(ans)
else:
    print("No")