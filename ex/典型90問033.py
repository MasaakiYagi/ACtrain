# 典型90問033
# https://atcoder.jp/contests/typical90/tasks/typical90_ag

import numpy as np

h, w = list(map(int, input().split()))
if (h==1)or(w==1):
    print(h*w)
else:
    print(int(np.ceil(h/2)*np.ceil(w/2)))