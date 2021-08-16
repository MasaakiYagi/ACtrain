# ABC213-C
# https://atcoder.jp/contests/abc213/tasks/abc213_c

h, w, n = list(map(int, input().split()))
x = []
y = []
for i in range(n):
    a, b = list(map(int, input().split()))
    x.append(a)
    y.append(b)

# x, yともに独立に昇順圧縮していけばよい
# まずは重複を排除してソート
xsort = sorted(set(x))
ysort = sorted(set(y))

# 置き換えテーブルを作成
xtrans = {v: i for i, v in enumerate(xsort)}
ytrans = {v: i for i, v in enumerate(ysort)}

# ソートテーブルを参照し，xおよびyの置き換えを行う
x = list(map(lambda a:xtrans[a]+1,x))
y = list(map(lambda a:ytrans[a]+1,y))

# 出力
for i in range(n):
    print(x[i],y[i])