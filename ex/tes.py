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

l, r = list(map(int, input().split()))
m = 10**9+7

cl = len(str(l))  # lのケタ
cr = len(str(r))  # rのケタ

def souwa(x):
    return (x%m)*((x+1)%m)//2

if cl==cr:
    # ケタ数が同じのとき
    ans = (souwa(r)-souwa(l-1))*cl%m
elif cr-cl==1:
    # ケタ差が1のとき
    eol = 10**cl-1  # lのケタの最後の数
    sor = 10**(cr-1)  # rのケタの最初の数
    ans = (cr*(souwa(r)-souwa(sor-1))+cl*(souwa(eol)-souwa(l-1)))%m
else:
    # ケタ差が2以上のとき
    eol = 10**cl-1  # lのケタの最後の数
    sor = 10**(cr-1)  # rのケタの最初の数
    a1 = cr*(souwa(r)-souwa(sor-1))%m
    a2 = cl*(souwa(eol)-souwa(l-1))%m
    ans = (a1+a2)%m
    for i in range(cl+1,cr):
        soi = 10**(i-1)
        eoi = 10**i-1
        ai = i*(souwa(eoi)-souwa(soi-1))
        ans = (ans+ai)%m

print(int(ans))