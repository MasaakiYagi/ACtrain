# ABC218-D
# https://atcoder.jp/contests/abc218/tasks/abc218_d


n = int(input())
xys = set()
xyl = []
for i in range(n):
    x, y = map(int, input().split())
    xys.add((x,y))
    xyl.append((x,y))

# 頂点組み合わせ全探索
rects = 0
for i in range(n-1):
    for j in range(i+1,n):
        # 点iを左上に，点jを右下に持つ長方形は作れるか判定
        ix = xyl[i][0]
        iy = xyl[i][1]
        jx = xyl[j][0]
        jy = xyl[j][1]
        # iとjがx軸かy軸に平行だったら判定しない
        if not(ix == jx or iy == jy):
            if ((ix,jy) in xys) and ((jx,iy) in xys):
                rects += 1

rects = rects//2

print(rects)
