# 典型90問084
# https://atcoder.jp/contests/typical90/tasks/typical90_cf

n = int(input())
s = list(input())

# 全体の組み合わせから余事象を引く
# 余事象はランレングス圧縮にて求める

# ランレングス圧縮を意識しながら余事象数総和をもとめていく
ret = 0
now = s[0]
chain = 1
for i in range(1,n):
    if now == s[i]:
        # chainが続くとき
        chain += 1
    else:
        # chainがとぎれたとき
        ret += chain*(chain+1)/2  # そこまでの余事象数をretに足す
        now = s[i]  # nowの切り替え
        chain = 1  # chainのリセット
ret += chain*(chain+1)/2

print(int(n*(n+1)/2-ret))
