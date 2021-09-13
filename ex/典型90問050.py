# 典型90問050
# https://atcoder.jp/contests/typical90/tasks/typical90_ax

n, l = list(map(int, input().split()))

# dpでいく
# dp[i] : i段目にたどり着くためのパターン数
dp = [0]*(n+1)
dp[0] = 1
for i in range(1,n+1):
    if i-l<0:
        dp[i] = dp[i-1]
    else:
        dp[i] = dp[i-1]+dp[i-l]

print(dp[n]%(10**9+7))