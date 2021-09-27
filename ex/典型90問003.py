# 典型90問003
# https://atcoder.jp/contests/typical90/tasks/typical90_c

import sys
sys.setrecursionlimit(10**7)
import collections

n = int(input())
a = [0]*(n-1)
b = [0]*(n-1)
for i in range(n-1):
    a[i], b[i] = list(map(int, input().split()))

# 経路数が最大になるu,vを見つけ（木の直径という），その数+1
# 任意のノードからDFSで最大距離ノードを探す（＝これが直径の端点aとなる），再度aからBFSで最大距離を探索すればそれが直径になる

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

def solve(g):
    u, v = dfs(g, 0)
    u, v = dfs(g, v)
    return u+1

# グラフ作成
g = Graph(n)
for i in range(n-1):
    g.add_edge(a[i]-1,b[i]-1)

print(solve(g))

