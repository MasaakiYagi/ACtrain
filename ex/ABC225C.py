# ABC225-C
# https://atcoder.jp/contests/abc224/tasks/abc225_c

n, m = list(map(int, input().split()))
b = [list(map(int, input().split())) for _ in range(n)]

# 全ての要素を7でわったあまりにする
for i in range(n):
    for j in range(m):
        b[i][j] = b[i][j]%7

# 行判定（すべての行が等しい）
flag_gyou = True
for i in range(1,n):
    if not(b[i]==b[0]):
        flag_gyou = False

# 列判定（列が[1,2,3,4,5,6,7]の部分配列）
cand = b[0]
cand = list(map(str,cand))
cand = "".join(cand)
if cand in "1234560":
    flag_retu = True
else:
    flag_retu = False

if flag_gyou and flag_retu:
    print("Yes")
else:
    print("No")