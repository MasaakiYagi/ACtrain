## lib
import heapq  # 優先度付きキュー（最小値探索につかえる）

## class

# Union Find
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

## プロシージャ

# 座標圧縮
x = [20,1,50,1,2,3,60,98,12,36,152,150]  # 重複あり順不同な数列
table = {v: i for i,v in enumerate(sorted(set(x)))}  # 重複を排除し，値をキーとする圧縮座標辞書を作成
x = list(map(lambda v:table[v], x))  # mapでxの全要素をtableによって置き換える