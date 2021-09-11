# 典型90問048
# https://atcoder.jp/contests/typical90/tasks/typical90_av

import heapq

n, k = list(map(int, input().split()))
a = [0]*n
b = [0]*n
for i in range(n):
    a[i], b[i] = map(lambda j:-j, list(map(int, input().split())))

# heapqにて最大値（実際は-1倍して最小値）を常にpopする。
# b[i]がpopしたら，a[i]-b[i]をheap配列にpushする
bh = b
heapq.heapify(bh)
ah =[]
checka = [False]*n
checkb = [False]*n

point = 0
while(k>0):
    # bhとahの最小値のうち，より小さい方をpopする
    if not(bh):
        minb = 1000000
    else:
        minb = bh[0]
    if not(ah):
        mina = 1000000
    else:
        mina = ah[0]
    
    if minb<mina:
        # bからpopするとき
        heapq.heappop(bh)
        # 対応するa-bをahにheappushする
        ind = b.index(minb)
        checkb[ind] = True
        heapq.heappush(ah, a[ind]-b[ind])
        # point加算
        point += minb
    else:
        # aからpopするとき
        heapq.heappop(ah)
        ind = a.index(mina)
        checka[ind] = True
        point += mina
    
    k -= 1

point = -1*point
print(point)