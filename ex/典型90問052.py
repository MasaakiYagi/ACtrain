# 典型90問052
# https://atcoder.jp/contests/typical90/tasks/typical90_az

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

ans = 1
for i in range(n):
    ans = ans*sum(a[i])

print(ans%(10**9+7))