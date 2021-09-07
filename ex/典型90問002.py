# 典型90問002
# https://atcoder.jp/contests/typical90/tasks/typical90_b

import itertools

n = int(input())

def judge(ks):
    num = 0
    for k in ks:
        if k=='0':
            num += 1
        elif k=='1':
            num -= 1
        if num<0:
            return False
    if num == 0:
        return True
    else:
        return False

if n%2 == 1:
    # 奇数なら0
    pass
else:
    keta = len(list(bin(2**n-1))[2:])
    # bit全探索する
    for i in range(2**n):
        pad = keta - len(list(bin(i))[2:])
        cand = ['0']*pad
        cand.extend(list(bin(i))[2:])
        if judge(cand):
            tex = ['(' if j == '0' else ')' for j in cand]
            print("".join(tex))