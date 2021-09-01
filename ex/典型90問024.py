# 典型90問024
# https://atcoder.jp/contests/typical90/tasks/typical90_x

import numpy as np

n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a = np.array(a)
b = np.array(b)

# 各i番目の要素の差の絶対値の和をSとする
# S<=Kで(K-S)%2==0なら操作可能
s = np.sum(np.abs(a-b))
if (s<=k) and ((k-s)%2 == 0):
    print('Yes')
else:
    print('No')
