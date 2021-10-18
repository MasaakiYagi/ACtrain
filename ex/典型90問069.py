# 典型90問069
# https://atcoder.jp/contests/typical90/tasks/typical90_bq

n, k = list(map(int, input().split()))
m = 10**9+7

if n == 1:
    ans = k
elif n == 2:
    ans = k*(k-1) if k*(k-1)>0 else 0
else:
    if k*(k-1)*(k-2)>0:
        ans = k*(k-1)%m
        a = pow(k-2,n-2,m)
        ans *= a
    else:
        ans = 0

ans = ans%m
print(ans)