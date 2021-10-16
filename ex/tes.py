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

a, b = list(map(int, input().split()))

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

gcdn = gcd(a,b)
ans = a//gcdn
ans *= b
if ans>10**18:
    print("Large")
else:
    print(ans)