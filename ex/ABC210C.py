# 典型90問004
# https://atcoder.jp/contests/typical90/tasks/typical90_d

import numpy as np

h, w = list(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(h)]
a = np.array(a)

retu = np.sum(a, axis=0, dtype=int)
gyou = np.sum(a, axis=1, dtype=int)

b = np.zeros((h,w), dtype=np.int64)
for i in range(len(gyou)):
    b[i,:] += int(gyou[i])
for j in range(len(retu)):
    b[:,j] += int(retu[j])

b = b-a
b = b.tolist()
for i in b:
    print(*i)