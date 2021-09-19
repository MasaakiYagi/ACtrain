# 典型90問012
# https://atcoder.jp/contests/typical90/tasks/typical90_l

h, w = list(map(int, input().split()))
nq = int(input())
q = [list(map(int, input().split())) for _ in range(nq)]

hw = [[0 for _ in range(w+1)] for _ in range(h+1)]

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

uf = UnionFind(h*w+1)

# クエリを順に実行，移動判定はunionfind
for query in q:
    if query[0]==1:
        # 塗りつぶしクエリ
        # 塗りつぶす
        hw[query[1]][query[2]] = 1
        # 上下左右の赤ノードと結合
        node = (query[1]-1)*w+query[2]
        # 上
        if query[1]>1:
            if hw[query[1]-1][query[2]] == 1:
                tnode = (query[1]-1-1)*w+query[2]
                uf.union(node, tnode)
        # 下
        if query[1]<h:
            if hw[query[1]+1][query[2]] == 1:
                tnode = (query[1]+1-1)*w+query[2]
                uf.union(node, tnode)
        # 左
        if query[2]>1:
            if hw[query[1]][query[2]-1] == 1:
                tnode = (query[1]-1)*w+query[2]-1
                uf.union(node, tnode)
        # 右
        if query[2]<w:
            if hw[query[1]][query[2]+1] == 1:
                tnode = (query[1]-1)*w+query[2]+1
                uf.union(node, tnode)
    elif query[0]==2:
        # 判定クエリ
        p1 = [query[1],query[2]]
        p2 = [query[3],query[4]]
        # 両方赤かの判定
        if hw[p1[0]][p1[1]]==1 and hw[p2[0]][p2[1]]==1:
            # UnionFindでルート判定
            node1 = (p1[0]-1)*w+p1[1]
            node2 = (p2[0]-1)*w+p2[1]
            if node1 == node2:
                print("Yes")
            elif uf.same(node1,node2):
                print("Yes")
            else:
                print("No")
        else:
            print("No")