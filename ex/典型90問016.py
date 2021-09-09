# 典型90問016
# https://atcoder.jp/contests/typical90/tasks/typical90_p

n = int(input())
a = list(map(int, input().split()))

a = sorted(a, reverse=True)

# 全探索（ただし，3重ループではなく2重）
ans = 9999
for i in range(int(n/a[0])+2):
    for j in range(int((n-i*a[0])/a[1])+2):
        if n >= (i*a[0]+j*a[1]):
            q = (n-(i*a[0]+j*a[1]))//a[2]
            mod = (n-(i*a[0]+j*a[1]))%a[2]
            if mod == 0 and ans>(q+i+j):
                ans = q+i+j
print(ans)