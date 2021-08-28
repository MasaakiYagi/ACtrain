# EDPC-K
# https://atcoder.jp/contests/dp/tasks/dp_k

n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

# dp[i]残りの石がiのとき，直後の手の人が勝てるか（True/False）
dp = [True]*(k+1)
for i in range(k+1):
    if i == 0 or i < min(a):
        dp[i] = False
    else:
        # i-a[j]が0以上のaを抽出
        # 打てる手で，Falseに遷移できるのであればTrue
        dp_dash = [dp[i-j] for j in a if i-j>=0]
        dp[i] = not(all(dp_dash))

if dp[k]:
    print("First")
else:
    print("Second")