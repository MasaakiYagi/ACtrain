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

# トポロジカルソート
from collections import defaultdict, deque
from typing import List
class tpsort():
    def __init__(self, nodes, edges) -> None:
        self.nodes = nodes
        self.edges = edges
        self.graph = {}
        self.nowgraph = {}
        self.first_readies = []
        self.readies = []
    
    def sort(self) -> None:
        # nodesとedgesに対してトポロジカルソート実行 -> self.graphに格納
        outs = defaultdict(list)
        ins = defaultdict(int)
        for u, v in self.edges:
            outs[u].append(v)
            ins[v] += 1
        

        q = deque(u for u in self.nodes if ins[u] == 0)
        self.readies = list(q.copy())
        self.first_readies = list(q.copy())
        insc = ins.copy()
        while q:
            u = q.popleft()
            self.graph[u] = {
                                'status':0,
                                'next':outs[u] if outs[u] else [],
                                'ins':insc[u]
                            }
            for v in outs[u]:
                ins[v] -= 1
                if ins[v] == 0:
                    q.append(v)
        self.nowgraph = self.graph.copy()

    def done(self, node) -> bool:
        # 入力したnodeを完了にする。
        if node in self.get_ready():
            # 入力ノードが実行可能の場合，status=1
            self.graph[node]['status'] = 1
            # nowgraphの連結ノードからinsを-1
            for v in self.nowgraph[node]['next']:
                self.nowgraph[v]['ins'] -= 1
                if self.nowgraph[v]['ins'] == 0:
                    self.readies.append(v)
            # nowgraphとreadiesからnodeを削除
            self.nowgraph.pop(node)
            self.readies.remove(node)
            return True
        else:
            # 入力nodeが実行不可の場合
            return False

    def get_ready(self) -> List:
        # 現時点で実行可能なnodeのリストを返す
        return self.readies

    def get_undone(self) -> List:
        # 現時点で未実行なnodeのリストを返す
        return [i for i in self.graph if self.graph[i]['status']==0]
    
    def reset_done(self) -> None:
        # 全てundoneに戻す
        self.readies = list(self.first_readies.copy())
        for u in self.nodes:
            self.graph[u]['status'] = 0
        self.nowgraph = self.graph.copy()

    def is_complete(self) -> bool:
        # すべて完了していたらTrue, 1つ以上未実行があればFalse
        return True if not self.get_undone() else False

## function

# 最小公倍数
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

#a,bの最大公約数
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

## プロシージャ

# 座標圧縮
x = [20,1,50,1,2,3,60,98,12,36,152,150]  # 重複あり順不同な数列
table = {v: i for i,v in enumerate(sorted(set(x)))}  # 重複を排除し，値をキーとする圧縮座標辞書を作成
x = list(map(lambda v:table[v], x))  # mapでxの全要素をtableによって置き換える