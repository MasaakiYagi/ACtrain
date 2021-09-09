# 典型90問018
# https://atcoder.jp/contests/typical90/tasks/typical90_r

import math
import numpy as np

t = int(input())
l, x, y = list(map(int, input().split()))
q = int(input())
es = [int(input()) for _ in range(q)]

# 像の位置
tk = np.array([x,y,0])
for e in es:
    # 観覧車の座標計算
    pos = np.array([
        0,
        -l/2*math.sin(2*math.pi*e/t),
        l/2-l/2*math.cos(2*math.pi*e/t)
    ])
    # 観覧車~像ベクトル計算
    tkkn = tk-pos
    # 観覧車から像方向への水平ベクトル
    knhor = np.copy(tkkn)
    knhor[2] = 0
    # tkknとknhorの内積
    d = np.dot(knhor,tkkn)
    # tkknとknhorの絶対値積
    dd = np.linalg.norm(tkkn)*np.linalg.norm(knhor)
    # 回答ラジアン
    if d>dd:
        dd=d
    rad = math.acos(d/dd)
    deg = np.rad2deg(rad)
    
    if deg<0:
        deg = abs(deg)
    while(deg>90):
        deg -= 90
    
    print(deg)