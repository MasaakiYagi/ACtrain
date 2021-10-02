# 典型90問026
# https://atcoder.jp/contests/typical90/tasks/typical90_z

import sys
sys.setrecursionlimit(10**8)

n = int(input())
tree = [set() for _ in range(n)]
for i in range(n-1):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    tree[a].add(b)
    tree[b].add(a)

col = [-1]*n

def dfs(i,prev,color):
    col[i] = color^1
    for j in tree[i]:
        if j == prev:
            continue
        dfs(j,i,col[i])

dfs(0,-1,0)

if sum(col)>=n//2:
    print(*[i for i,color in enumerate(col,1) if color==1][:n//2])
else:
    print(*[i for i,color in enumerate(col,1) if color==0][:n//2])