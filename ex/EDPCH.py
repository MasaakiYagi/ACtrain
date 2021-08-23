# EDPC-H
# https://atcoder.jp/contests/dp/tasks/dp_h

h, w = list(map(int, input().split()))
a = []
for i in range(h):
    a.append(list(input()))

# dp:i,jマスにたどりつく方法は(i-1,j)と(i,j-1)の和，ただしa=#のときは0
dp = [[0]*w for _ in range(h)]
dp[0][0] = 1
for i in range(h):
    for j in range(w):
        if i == 0 and j == 0:
            continue
        
        if a[i][j] == '#':
            # 壁のとき，たどり着く方法は0
            continue
        
        fromleft = 0  # 左からのアプローチ数
        fromup = 0  # 上からのアプローチ数
        if i != 0:
            fromup = dp[i-1][j]
        if j != 0:
            fromleft = dp[i][j-1]
        dp[i][j] = fromup + fromleft

print(dp[-1][-1] % (10**9+7))