# ABC036-C
# https://atcoder.jp/contests/abc036/tasks/abc036_c

# 入力受付
n = int(input())
a = [int(input()) for i in range(n)]

# 重複排除してソート
sad = sorted(set(a))

# 値と圧縮値の対応テーブル作成
table = {v: i for i, v in enumerate(sad)}

# 置き換え
ans = list(map(lambda v: table[v], a))

for i in ans:
    print(i)