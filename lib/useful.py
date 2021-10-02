# 再帰の回数上限撤廃（再帰使うならPythonで通そう）
import sys
sys.setrecursionlimit(10**8)

## lib
import heapq  # 優先度付きキュー（最小値探索につかえる）

## class

# BFS,DFS(典型03)
class Graph:
    def __init__(self, size):
        # id starts from 0
        self.size = size
        #self.vertices = [0] * size
        self.edges = [None] * size
        for i in range(size):
            self.edges[i] = []
    def __repr__(self):
        out = []
        #out.append("vertices {}".format(self.vertices))
        for i, e in enumerate(self.edges):
            out.append("{}{}".format(i, pf(e)))
        return "\n".join(out)
    def add_edge(self, frm, to):
        self.edges[frm].append(to)
        self.edges[to].append(frm)

def dfs(graph, v, parent=-1, depth=0):
    max_depth = depth
    max_leaf = v
    depth += 1
    for to in graph.edges[v]:
        if to == parent:
            continue
        d, leaf = dfs(graph, to, v, depth)
        if d > max_depth:
            max_depth = d
            max_leaf = leaf
    return max_depth, max_leaf

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

# 最小費用流(minimum cost flow)
class MinCostFlow:
    def __init__(self, n):
        self.n = n
        self.G = [[] for i in range(n)]

    def addEdge(self, f, t, cap, cost):
        # [to, cap, cost, rev]
        self.G[f].append([t, cap, cost, len(self.G[t])])
        self.G[t].append([f, 0, -cost, len(self.G[f])-1])

    def minCostFlow(self, s, t, f):
        n = self.n
        G = self.G
        prevv = [0]*n; preve = [0]*n
        INF = 10**9+7

        res = 0
        while f:
            dist = [INF]*n
            dist[s] = 0
            update = 1
            while update:
                update = 0
                for v in range(n):
                    if dist[v] == INF:
                        continue
                    gv = G[v]
                    for i in range(len(gv)):
                        to, cap, cost, rev = gv[i]
                        if cap > 0 and dist[v] + cost < dist[to]:
                            dist[to] = dist[v] + cost
                            prevv[to] = v; preve[to] = i
                            update = 1
            if dist[t] == INF:
                return -1

            d = f; v = t
            while v != s:
                d = min(d, G[prevv[v]][preve[v]][1])
                v = prevv[v]
            f -= d
            res += d * dist[t]
            v = t
            while v != s:
                e = G[prevv[v]][preve[v]]
                e[1] -= d
                G[v][e[3]][1] += d
                v = prevv[v]
        return res

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

# a,bの最大公約数
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# n進数からm進数に変換（nlは配列表記してあげる必要あり）
def base_convert(nl, ibase, obase):
    o = []
    while any(nl):
        c = 0
        for i in range(len(nl)):
            c = c * ibase + nl[i]
            nl[i],c = divmod(c,obase)
        o.append(c)
    o.reverse()
    return o

# めぐる式2分探索
def is_ok(arg):
    # 条件を満たすかどうか？問題ごとに定義
    pass


def meguru_bisect(ng, ok):
    '''
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    '''
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

# 繰り返し二乗法
def kuripow(x, n):
    ans = 1
    while n:
        if n % 2:
            ans *= x
        x *= x
        n >>= 1
    return ans

def modpow(a: int, p: int, mod: int) -> int:
    # return a**p (mod MOD) O(log p)
    if p == 0:
        return 1
    if p % 2 == 0:
        half = modpow(a, p//2, mod)
        return half*half % mod
    else:
        return a * modpow(a, p-1, mod) % mod

# 素因数分解
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

## プロシージャ

# 座標圧縮
x = [20,1,50,1,2,3,60,98,12,36,152,150]  # 重複あり順不同な数列
table = {v: i for i,v in enumerate(sorted(set(x)))}  # 重複を排除し，値をキーとする圧縮座標辞書を作成
x = list(map(lambda v:table[v], x))  # mapでxの全要素をtableによって置き換える