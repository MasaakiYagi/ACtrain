# ABC211-C
# https://atcoder.jp/contests/abc214/tasks/abc214_d

s = input()
c = 'chokudai'

n = len(s)
m = len(c)
dp = [[0]*(n+1) for _ in range(m+1)]

# DPを使う
for i in range(n+1):
    for j in range(m+1):
        if j==0:
            dp[j][i] = 1
        elif i==0:
            dp[j][i] = 0
        elif s[i-1] != c[j-1]:
            dp[j][i] = dp[j][i-1]
        elif s[i-1] == c[j-1]:
            dp[j][i] = dp[j][i-1]+dp[j-1][i-1]

# 答えは%(10^9+7)
ans = dp[m][n]%(10**9+7)
print(ans)