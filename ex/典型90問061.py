# 典型90問061
# https://atcoder.jp/contests/typical90/tasks/typical90_bi

from collections import deque

q = int(input())
tx = []
for _ in range(q):
    tx.append(list(map(int, input().split())))

y = deque()
for i in tx:
    if i[0] == 1:
        # 山札の上に数追加
        y.append(i[1])
    elif i[0] == 2:
        # 山札の下に数追加
        y.appendleft(i[1])
    else:
        # 山札上からi[1]番目の出力
        print(y[-i[1]])