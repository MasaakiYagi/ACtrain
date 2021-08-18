# EDPC-D
# https://atcoder.jp/contests/dp/tasks/dp_d

n, nw = list(map(int, input().split()))
w = []
v = []
for i in range(n):
    a, b = list(map(int, input().split()))
    w.append(a)
    v.append(b)

dp = [[0]*(nw+1) for _ in range(n)]
for i in range(n):
    for j in range(nw+1):
        if i == 0:
            # 1つめのアイテムについて
            dp[i][j] = v[i] if j>=w[i] else 0
        else:
            # 2つめ以降のアイテムについて
            if j >= w[i]:
                dp[i][j] = max(dp[i-1][j-w[i]]+v[i], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]

print(max(dp[-1]))