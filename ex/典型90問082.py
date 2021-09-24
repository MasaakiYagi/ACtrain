# 典型90問082
# https://atcoder.jp/contests/typical90/tasks/typical90_cd

l, r = list(map(int, input().split()))

# lとrの桁数を求める
lk = len(list(str(l)))
rk = len(list(str(r)))

m = (10**9+7)

def f(x):
    return (x%m)*((x+1)%m)//2

ans = 0

for i in range(lk,rk+1):
    # 左端
    li = max(l, 10**(i-1))-1
    # 右端
    ri = min(r, 10**(i)-1)
    # 総和の一般項
    ans += (f(ri)-f(li)+m)%m*i

print(ans%m)