# 典型90問046
# https://atcoder.jp/contests/typical90/tasks/typical90_at

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

# すべて46で割ったあまりに変換
a = list(map(lambda i:i%46, a))
b = list(map(lambda i:i%46, b))
c = list(map(lambda i:i%46, c))

# 各あまりがいくつあるかカウント
ac = [0]*46
bc = [0]*46
cc = [0]*46
for i in a:
    ac[i] += 1
for i in b:
    bc[i] += 1
for i in c:
    cc[i] += 1

count = 0
for i in range(46):
    for j in range(46):
        for k in range(46):
            if (i+j+k)%46==0:
                count += ac[i]*bc[j]*cc[k]

print(count)