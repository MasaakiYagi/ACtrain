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

n = int(input())
p = [list(map(int, input().split())) for _ in range(n)]

ps = set()
for i in range(n):
    ps.add((p[i][0],p[i][1]))

# 全ての2点の組み合わせに対して，残る2頂点があるかを確認
ans = 0
for i in range(n-1):
    for j in range(i+1,n):
        x1 = p[i][0]
        y1 = p[i][1]
        x2 = p[j][0]
        y2 = p[j][1]
        if not(x1==x2) and not(y1==y2):
            if (x1,y2) in ps and (x2,y1) in ps:
                ans += 1

print(ans//2)
