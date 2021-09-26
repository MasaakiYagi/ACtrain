# ABC220-D
# https://atcoder.jp/contests/abc220/tasks/abc220_d

n = int(input())
a = list(map(int, input().split()))
m = 998244353

# dp[i][j] A[i]まで操作したとき，先頭がjであるパターン数
dp = [[0 for _ in range(10)] for _ in range(n+1)]

# 初回
dp[1][a[0]] = 1

# ループ
for i in range(1,n):
    for j in range(10):
        dp[i+1][(j+a[i])%10] = (dp[i+1][(j+a[i])%10]+dp[i][j])%m
        dp[i+1][(j*a[i])%10] = (dp[i+1][(j*a[i])%10]+dp[i][j])%m

for j in range(10):
    print(dp[-1][j])