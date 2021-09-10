# 典型90問018
# https://atcoder.jp/contests/typical90/tasks/typical90_r

import math

t = int(input())
l, x, y = list(map(int, input().split()))
q = int(input())
es = [int(input()) for _ in range(q)]

# 像の位置
tk = [x,y,0]
for e in es:
    # 観覧車の座標計算
    pos = [
        0,
        -l/2*math.sin(2*math.pi*e/t),
        l/2-l/2*math.cos(2*math.pi*e/t)
    ]
    # 観覧車~像水平距離
    hor = math.sqrt(tk[0]**2+(tk[1]-pos[1])**2)
    rad = math.atan(pos[2]/hor)
    deg = math.degrees(rad)
    
    print(deg)