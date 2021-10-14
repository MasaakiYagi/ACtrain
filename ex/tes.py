# 割り算の整数部分ほしいなら//
# bit_shiftなら
    # <<左シフト
    # >>右シフト
# list(map(int, input().split()))
# int(input())

# 再帰の回数上限撤廃（再帰使うならPythonで通そう）
# import sys
# sys.setrecursionlimit(10**8)

n = int(input())
a, b, c = list(map(int, input().split()))

# 全探索（効率よく）
ans = 10000
for i in range(10001):
    for j in range(10001-i):
        tot = i*a+j*b
        sub = n-tot
        if sub>0 and sub%c==0:
            # cを整数倍出すことで，丁度tot合計がnとなったとき
            k = sub//c
            ans = min(ans, i+j+k)

print(ans)