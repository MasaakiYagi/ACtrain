# 割り算の整数部分ほしいなら//
# bit_shiftなら
    # <<左シフト
    # >>右シフト
# list(map(int, input().split()))
# int(input())

# 再帰の回数上限撤廃（再帰使うならPythonで通そう）
# import sys
# sys.setrecursionlimit(10**8)

from collections import deque

n=int(input())
tab = {0:"(",
        1:")"}

if n%2==0:  # 奇数は無視
    for i in range(2**n):
        bi = list(bin(i)[2:])
        bi = list(map(int, bi))
        bi = deque(bi)
        sa = n-len(bi)
        if sa>0:  # 桁数が足りなかったら補完
            salist = [0]*sa
            for j in salist:
                bi.appendleft(j)
        
        # 正しいカッコか判定
        cnt = 0
        flag = 1
        for j in bi:
            if j==0:
                cnt += 1
            else:
                cnt -= 1
            
            if cnt<0:
                flag = 0
                break
            
        if not(cnt==0):
            flag = 0
        
        if flag:
            ans = list(map(lambda v:tab[v], bi))
            print("".join(ans))
