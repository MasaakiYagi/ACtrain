# EDPC-G
# https://atcoder.jp/contests/dp/tasks/dp_g

from numpy.core.fromnumeric import sort
import math

s, k = input().split()
k = int(k)
ns = len(s)

# 辞書順(最小)の文字の並びを求める
sorted_s = sorted(s)

# 下2桁，3桁の文字列で作れる文字列の個数を求め，最初にkを超える数字lを求める

# 文字列tを並び変えて作れる文字列の数
def calc_n(t) -> int:
    aa = {}
    for i in t:
        if i in aa:
            aa[i] += 1
        else:
            aa[i] = 1
    
    p = math.factorial(len(t))
    for a in aa:
        if aa[a] > 1:
            p = p/math.factorial(aa[a])
    
    return int(p)

pp = []
qq = []
for i in range(ns):
    z = calc_n(sorted_s[-(i+1):])
    if k <= z:
        pp = i
        break
    
print(pp)
print(z)
