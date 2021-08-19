# EDPC-F
# https://atcoder.jp/contests/dp/tasks/dp_f

s = input()
t = input()

# tのi番目，sのj番目までで最大の文字列数をdpに格納していく
ns = len(s)
nt = len(t)
dp = [[0 for _ in range(ns+1)] for _ in range(nt+1)]

# 文字列変換関数
def strans(l):
    return list(map(lambda p:s[p-1], l))
def ttrans(l):
    return list(map(lambda p:t[p-1], l))

# dp
for i in range(nt+1):
    for j in range(ns+1):
        if not (i == 0 or j == 0):
            if t[i-1] == s[j-1]:
                # sとtの文字が一致しているとき
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                # 不一致時
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

# 今度はdpの値を逆順に辿って行って文字列を再構成する
i = nt
j = ns
len = dp[i][j]
words = []
while(len>0):
    if dp[i][j] == dp[i][j-1]:
        # j-1の最大文字長が同じ場合
        j = j-1
    elif dp[i][j] == dp[i-1][j]:
        # i-1の最大文字長が同じ場合
        i = i-1
    else:
        # j-1もi-1も最大文字長さが異なるならば，この時の文字が最後尾に使われる
        words.insert(0, s[j-1])
        i = i-1
        j = j-1
        len = dp[i][j]

print("".join(words))
