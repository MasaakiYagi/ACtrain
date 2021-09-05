# 典型90問078
# https://atcoder.jp/contests/typical90/tasks/typical90_bz


n, m = list(map(int, input().split()))
e = [[] for _ in range(n)]

for i in range(m):
    a, b = list(map(int, input().split()))
    e[a-1].append(b-1)
    e[b-1].append(a-1)

# 条件を満たすnodeをカウントアップ
count = 0
for i in range(1,n):
    n = [j for j in e[i] if j<i]
    if len(n)==1:
        count += 1

print(count)