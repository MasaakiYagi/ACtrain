# 典型90問079
# https://atcoder.jp/contests/typical90/tasks/typical90_ca

h, w = list(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(h)]
b = [list(map(int, input().split())) for _ in range(h)]

# 左上のますから順番にaをbに一致させていき，最後逆L字の要素が一致するかで判定
cnt = 0
for i in range(h-1):
    for j in range(w-1):
        # aとbの(i,j)要素の差を計算
        d = b[i][j] - a[i][j]
        # aの(i,j)~(i+1,j+1)の2*2マスにdを足してbと部分一致させる
        a[i][j] += d
        a[i+1][j] += d
        a[i][j+1] += d
        a[i+1][j+1] += d
        # 操作回数を加算
        cnt += abs(d)
        
# 逆L字要素についてaとbが一致しているか判定
ah = a[-1]
bh = b[-1]
aw = [i[-1] for i in a]
bw = [i[-1] for i in b]

if ah==bh and aw==bw:
    print("Yes")
    print(cnt)
else:
    print("No")
