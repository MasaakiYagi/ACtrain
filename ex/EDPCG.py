# EDPC-G
# https://atcoder.jp/contests/dp/tasks/dp_g

from collections import defaultdict, deque
from typing import List

n, m = list(map(int, input().split()))
uv = []
for i in range(m):
    uv.append(list(map(int, input().split())))

# トポロジカルソートクラス
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


# 頂点をトポロジカルソート
nodes = [i+1 for i in range(n)]
tps = tpsort(nodes, uv)
tps.sort()

# トポロジカルソート順にdp
dp = [0]*(n+1)
for u in tps.graph:
    # i番目の頂点から遷移する複数の頂点に対して，最長経路を更新していく
    for v in tps.graph[u]['next']:
        dp[v] = max(dp[v], dp[u]+1)

# dpリスト中最大の数値が解
print(max(dp))
