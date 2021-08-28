# EDPC-K
# https://atcoder.jp/contests/dp/tasks/dp_k

n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

# dp[i]残りの石がiのとき，最適戦略で終了するまでの手数　0のとき終わってる
dp = [0]*(k+1)
for i in range(k+1):
    if i == 0 or i < min(a):
        dp[i] = 0
    else:
        # i-a[j]が0以上のaを抽出
        # min(dp[i-a])+1がdp[i]の値となる
        dp_dash = [dp[i-j] for j in a if i-j>=0]
        dp[i] = min(dp_dash)+1

if dp[k]%2 == 0:
    print("Second")
else:
    print("First")