# ARC128-A
# https://atcoder.jp/contests/arc128/tasks/arc128_a

n = int(input())
a = list(map(int, input().split()))

ans = [0]*n
for i in range(n-1):
    if a[i]>a[i+1]:
        ans[i] ^= 1
        ans[i+1] ^= 1

print(*ans)