# 典型90問014
# https://atcoder.jp/contests/typical90/tasks/typical90_n

# Pythonで提出

import numpy as np

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a = np.array(a)
b = np.array(b)
a = np.sort(a)
b = np.sort(b)
print(np.sum(np.abs(a-b)))