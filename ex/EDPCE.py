# EDPC-E
# https://atcoder.jp/contests/dp/tasks/dp_e

INF = 10**9+1

n, nw = list(map(int, input().split()))
w = []
v = []
for i in range(n):
    a, b = list(map(int, input().split()))
    w.append(a)
    v.append(b)

maxv = sum(v)
# Dの問題通りにやるとwの数がえげつない→dp[i][j]をi番目までのアイテムについて価値がjになるようにした場合の最小重さとする(満たす組み合わせがなければINF)
dp = [[INF]*(maxv+1) for _ in range(n+1)]
dp[0][0] = 0
for i in range(n):
    for j in range(maxv+1):
        if j<v[i]:
            dp[i+1][j] = dp[i][j]
        else:
            dp[i+1][j] = min(
                dp[i][j-v[i]]+w[i],
                dp[i][j]
            )

# dp[-1][j]のうちnw以下で最大のときのjが答えになる
#maxw = max([i for i in dp[-1] if i<=nw])
#print(dp[-1].index(maxw))
for i in range(maxv,-1,-1):
    if dp[-1][i] <= nw:
        print(i)
        break