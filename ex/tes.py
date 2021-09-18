# list(map(int, input().split()))
# int(input())
"""
n = int(input())
x, y = list(map(int, input().split()))
ab = [list(map(int, input().split())) for _ in range(n)]

# 次に取るべき弁当のスコアを更新しながら選択していく
bentos = [[0, i] for i in ab]
cnt = 0
while (x>0 or y>0) and not(not(bentos)):
    x = 0 if x<0 else x
    y = 0 if y<0 else y
    # bentosスコア更新
    xw = x/(x+y)
    yw = y/(x+y)
    m = 0
    ind = len(bentos)
    for i in range(len(bentos)):
        # xを超過する分については評価しない
        hyokax = x if bentos[i][1][0]>x else bentos[i][1][0]
        hyokay = y if bentos[i][1][1]>y else bentos[i][1][1]
        bentos[i][0] = hyokax*xw+hyokay*yw
        if bentos[i][0]>m:
            m = bentos[i][0]
            ind = i
    # bentos最大スコア選択
    maxbento = bentos.pop(ind)
    # x,yの値更新
    x -= maxbento[1][0]
    y -= maxbento[1][1]
    cnt += 1
    
if not(bentos) and (x>0 or y>0):
    print(-1)
else:
    print(cnt)
"""

n = int(input())
x, y = list(map(int, input().split()))
ab = [list(map(int, input().split())) for _ in range(n)]

# 全部取ったあと，寄与度の少ない弁当を取り除いていく
sx = sum([i[0] for i in ab])
sy = sum([i[1] for i in ab])
bentos = [[0, i] for i in ab]

# 寄与度計算
for i in range(len(bentos)):
    bentos[i][0] = bentos[i][1][0]/x + bentos[i][1][1]/y

bentos = sorted(bentos, key=lambda x:x[0])

if sum([i[1][0] for i in bentos])>=x and sum([i[1][1] for i in bentos])>=y:
    while(sum([i[1][0] for i in bentos])>=x and sum([i[1][1] for i in bentos])>=y):
        bentos.pop(0)
    print(len(bentos)+1)
else:
    print(-1)