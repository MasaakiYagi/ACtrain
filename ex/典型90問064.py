# 典型90問064
# https://atcoder.jp/contests/typical90/tasks/typical90_bl

n, q = list(map(int, input().split()))
a = list(map(int, input().split()))
v = [list(map(int, input().split())) for _ in range(q)]


# 初期不便さ計算
m = sum(a)/len(a)
da = list(map(lambda i:abs(i-m), a))
suma = int(sum(da)*2-da[0]-da[-1])

for i in range(len(v)):
    # 変動境界の不便さをsumaから引く
    if v[i][0]>1:
        suma -= abs(a[v[i][0]-1]-a[v[i][0]-2])
    if v[i][1]<len(a):
        suma -= abs(a[v[i][1]]-a[v[i][1]-1])
    # 隆起
    a[v[i][0]-1:v[i][1]] = list(map(lambda j:j+v[i][2], a[v[i][0]-1:v[i][1]]))
    # 変動部分再計算
    if v[i][0]>1:
        suma += abs(a[v[i][0]-1]-a[v[i][0]-2])
    if v[i][1]<len(a):
        suma += abs(a[v[i][1]]-a[v[i][1]-1])
    print(suma)