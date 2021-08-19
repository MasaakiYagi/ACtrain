# EDPC-G
# https://atcoder.jp/contests/dp/tasks/dp_g

n, m = list(map(int, input().split()))
uv = []
for i in range(m):
    uv.append(list(map(int, input().split())))

# 頂点をトポロジカルソート(関数で実装する)
tps = []
# トポロジカルソート順にdp
dp = [0]*n
i = 0
for u in tps:
    # i番目の頂点から遷移する複数の頂点に対して，最長経路を更新していく
    for v in u:
        dp[v] = max(dp[v], dp[i]+1)
    i += 1

# dpリスト中最大の数値が解
print(max(dp))