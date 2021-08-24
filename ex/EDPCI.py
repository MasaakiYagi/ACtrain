# EDPC-I
# https://atcoder.jp/contests/dp/tasks/dp_i

n = int(input())
p = list(map(float, input().split()))

# dp[i][j]:i枚目までコインを投げたとき，j枚表がでる確率
dp = [[0]*(n+1) for _ in range(n+1)]
for i in range(n+1):
    for j in range(n+1):
        if i == 0:
            continue
        if i<j:
            continue
        
        if i == 1 and j == 0:
            # 1枚目まで投げて0枚表の確率
            dp[i][j] = 1-p[i-1]
        elif i == 1 and j == 1:
            # 1枚目まで投げて1枚表の確率
            dp[i][j] = p[i-1]
        elif j == 0:
            # 出る表が0枚のとき
            dp[i][j] = dp[i-1][j]*(1-p[i-1])
        else:
            # d[i][j] = d[i-1][j-1]*i番目が表+d[i-1][j]*i番目が裏
            dp[i][j] = dp[i-1][j-1]*p[i-1] + dp[i-1][j]*(1-p[i-1])

print(sum(dp[-1][n//2+1:]))
