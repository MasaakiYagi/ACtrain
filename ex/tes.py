
n = int(input())
x = [0]*n
y = [0]*n
for i in range(n):
    x[i], y[i] = map(int, input().split())

# 座標圧縮し，走査探索

# 平面座標圧縮
table = {v: i for i,v in enumerate(sorted(set(x)))} 
x = list(map(lambda v:table[v], x))
table = {v: i for i,v in enumerate(sorted(set(y)))} 
y = list(map(lambda v:table[v], y))

# x方向走査
edge = []
ans = 0
for i in range(max(x)+1): #max2000
    cands = [ ind for ind , v in enumerate ( x ) if v == i ]
    if len(cands)>1:
        # iの線において点が2個以上見つかった場合，newedgeに追加
        newedge = []
        for i1 in range(len(cands)-1):
            for i2 in range(i1+1,len(cands)):
                newedge.append([y[cands[i1]], y[cands[i2]]])
        
        # edge中でnewedgeに一致するものの数をカウント（=長方形数）
        for p in newedge:
            ans += sum(q == p for q in edge)
        # newedgeをedgeに追加
        edge.extend(newedge)

print(ans)
