# ABC218-C
# https://atcoder.jp/contests/abc218/tasks/abc218_c

import numpy as np

n = int(input())
s = [list(input()) for _ in range(n)]
t = [list(input()) for _ in range(n)]

s = np.array(s)
t = np.array(t)

# すべての#を含む最小のパディングをし，4方向照合する

# sのパディング
# うえから
while(np.all(s[0,:]==".")):
    s = np.delete(s, 0, axis=0)
# したから
while(np.all(s[-1,:]==".")):
    s = np.delete(s, -1, axis=0)
# 左から
while(np.all(s[:,0]==".")):
    s = np.delete(s, 0, axis=1)
# 右から
while(np.all(s[:,-1]==".")):
    s = np.delete(s, -1, axis=1)
    

# tのパディング
# うえから
while(np.all(t[0,:]==".")):
    t = np.delete(t, 0, axis=0)
# したから
while(np.all(t[-1,:]==".")):
    t = np.delete(t, -1, axis=0)
# 左から
while(np.all(t[:,0]==".")):
    t = np.delete(t, 0, axis=1)
# 右から
while(np.all(t[:,-1]==".")):
    t = np.delete(t, -1, axis=1)

# 4方向判定
ans = "No"
for _ in range(4):
    if s.shape==t.shape:
        if (s == t).all():
            ans = "Yes"
    t = np.rot90(t)

print(ans)