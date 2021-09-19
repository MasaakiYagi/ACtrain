# ABC219-D
# https://atcoder.jp/contests/abc219/tasks/abc219_d

n = int(input())
x, y = list(map(int, input().split()))
ab = [list(map(int, input().split())) for _ in range(n)]

# dp[i][j][k] 1~i番目の弁当で，たこやきj個以上，タイ焼きk個以上になる最小の弁当数
INF = 10**9
dp = [[[INF for k in range(y+1)] for j in range(x+1)] for i in range(n+1)]
dp[0][0][0] = 0
for i in range(n):
    for j in range(x+1):
        for k in range(y+1):
            # i+1番目の弁当を買うケースの更新
            dp[i+1][min(j+ab[i][0], x)][min(k+ab[i][1], y)] = min(dp[i+1][min(j+ab[i][0], x)][min(k+ab[i][1], y)],
                                                                dp[i][j][k]+1)
            # i+1番目の弁当を買わないケースの更新
            dp[i+1][j][k] = min(dp[i+1][j][k], dp[i][j][k])

ans = -1 if dp[-1][-1][-1]==INF else dp[-1][-1][-1]
print(ans)