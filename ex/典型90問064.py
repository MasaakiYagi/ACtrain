# 典型90問064
# https://atcoder.jp/contests/typical90/tasks/typical90_bl

n, q = list(map(int, input().split()))
a = list(map(int, input().split()))
v = [list(map(int, input().split())) for _ in range(q)]


# 階差配列bを作成b[i] = a[i+1]-a[i]
b = []
suma = 0
for i in range(n-1):
    b.append(a[i+1]-a[i])
    suma += abs(b[i])

# 地殻変動更新
for i in range(q):
    dl = 0
    dr = 0
    if v[i][0]>1:
        dl = -abs(b[v[i][0]-2])
        b[v[i][0]-2] += v[i][2]
        dl += abs(b[v[i][0]-2])
    if v[i][1]<n:
        dr = -abs(b[v[i][1]-1])
        b[v[i][1]-1] -= v[i][2]
        dr += abs(b[v[i][1]-1])
    suma += dl+dr
    print(suma)