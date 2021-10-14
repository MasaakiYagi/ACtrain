# 典型90問014
# https://atcoder.jp/contests/typical90/tasks/typical90_n


n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a = sorted(a)
b = sorted(b)

ans = 0
for i in range(n):
    ans += abs(a[i]-b[i])
    
print(ans)