# ABC036-A
# https://atcoder.jp/contests/abc036/tasks/abc036_b

# 入力受付
n = int(input())
m = []
for i in range(n):
    m.append(list(input()))

z = [[0]*n for i in range(n)]
# (i,j) ⇒ (j,n-i)となる
for i in range(n):
    for j in range(n):
        z[j][n-1-i] = m[i][j]

for l in z:
    print("".join(l))