# EDPC-J
# https://atcoder.jp/contests/dp/tasks/dp_j

n = int(input())
a = list(map(int, input().split()))

# dp[c1][c2][c3]は，寿司が1つ残っている皿の枚数c1，同様のc2，c3のときの，全て食べきるまでの試行回数期待値
# 次の漸化式が成立
# dp[c1][c2][c3] = 1/(1-0の皿を引く確率) + dp[c1-1][c2][c3]*(1の皿を引く確率)/(1-0の皿を引く確率)
#                                       + dp[c1+1][c2-1][c3]*(2の皿を引く確率)/(1-0の皿を引く確率) 
#                                       + dp[c1][c2+1][c3-1]*(3の皿を引く確率)/(1-0の皿を引く確率)
# つまり，第1項は第2~第4項のいずれかに遷移するための試行回数期待値
# 第2~第4項はそれぞれの状態の期待値に遷移確率の重みをつけたもの
dp = [[[0 for _ in range(301)] for _ in range(301)] for _ in range(301)]
flag = [[[False for _ in range(301)] for _ in range(301)] for _ in range(301)]
flag[0][0][0] = True
c = [0]*4

def f(c1,c2,c3):
    if flag[c1][c2][c3]:
        return dp[c1][c2][c3]
    else:
        flag[c1][c2][c3] = True
        p1 = c1/n
        p2 = c2/n
        p3 = c3/n
        p0 = 1-(p1+p2+p3)
        frans = 1/(1-p0)
        if c1>0:
            frans += dp[c1-1][c2][c3]*p1/(1-p0)
        if c2>0:
            frans += dp[c1+1][c2-1][c3]*p2/(1-p0)
        if c2>0:
            frans += dp[c1][c2+1][c3-1]*p3/(1-p0)
        dp[c1][c2][c3] = frans
        return dp[c1][c2][c3]
        
for i in a:
    c[i] += 1

ans = f(c[1],c[2],c[3])
print(ans)