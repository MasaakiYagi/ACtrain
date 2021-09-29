# 典型90問008
# https://atcoder.jp/contests/typical90/tasks/typical90_h

n = int(input())
s = list(input())
a = list("atcoder")

m = 10**9+7

# dp[i][j] sのi文字目までで"atcoder"のj文字目までを作れる個数
dp = [[0 for _ in range(len(a))] for _ in range(n)]

for i in range(n):
    for j in range(len(a)):
        if i == 0:
            if s[i]==a[j] and j==0:
                dp[i][j] = 1
        else:
            if j==0:
                # 1文字目aの場合
                if s[i]==a[j]:
                    dp[i][j] = dp[i-1][j] + 1
                else:
                    dp[i][j] = dp[i-1][j]
            else:
                # 2文字目以降の場合
                if s[i]==a[j]:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                else:
                    dp[i][j] = dp[i-1][j]

print(dp[-1][-1]%m)