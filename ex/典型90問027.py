# 典型90問027
# https://atcoder.jp/contests/typical90/tasks/typical90_aa

import numpy as np

n = int(input())
s = []
for i in range(n):
    s.append(input())

s = np.array(s)

u, indices = np.unique(s, return_index=True)
indices = np.sort(indices)
for i in indices:
    print(i+1)