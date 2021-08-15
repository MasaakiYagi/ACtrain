# ABC214-D
# https://atcoder.jp/contests/abc214/tasks/abc214_d

class UnionFind():
    def __init__(self, n):
        # すべて森で初期化
        self.n = n
        self.par = [-1]*n
    
    # 根を探すメソッド
    def root(self, x):
        if self.par[x] < 0:
            return x
        else:
            return self.root(self.par[x])

    # 根が同じかチェック
    def same(self, x, y):
        if self.root(x)==self.root(y):
            return True
        else:
            return False

    # xが属する森の大きさ(所属要素数)
    def size(self, x):
        return -self.par[self.root(x)]

    # 森の結合
    def union(self, x, y):
        rx = self.root(x)
        ry = self.root(y)

        # xとyの根が同じかチェック
        if rx == ry:
            return

        # より要素数の大きい根をrxとする
        if self.par[rx] > self.par[ry]:
            rx, ry = ry, rx
        
        # rxにryを属させる
        self.par[rx] += self.par[ry]
        self.par[ry] = rx


    # 枝の切断(指定した頂点が根となる)
    def cut(self, x):
        self.par[x]=x

n = int(input())
g = [list(map(int,input().split())) for _ in range(n-1)]

# gを重みの低い順にソート
g = sorted(g, key=lambda x:x[2])

# Union-Find インスタンス作成
uf = UnionFind(n)

ans = 0
for i in range(n-1):
    # wiを最大の重みとする最短経路の数を計算
    su = uf.size(g[i][0]-1)
    sv = uf.size(g[i][1]-1)
    sp = su*sv
    # wiを最大の重みとする最短経路の最大重みの総和
    sigw = g[i][2]*sp
    # ansに加算
    ans += sigw
    # u, vを連結する
    uf.union(g[i][0]-1,g[i][1]-1)

print(ans)