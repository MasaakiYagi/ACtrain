# 典型90問016
# https://atcoder.jp/contests/typical90/tasks/typical90_p

n = int(input())
a, b, c = list(map(int, input().split()))

# 全探索（効率よく）
ans = 10000
for i in range(10000):
    for j in range(10000-i):
        tot = i*a+j*b
        sub = n-tot
        if sub>0 and sub%c==0:
            # cを整数倍出すことで，丁度tot合計がnとなったとき
            k = sub//c
            ans = min(ans, i+j+k)
        elif sub==0:
            # cが0枚で丁度tot合計がnのとき
            ans = min(ans, i+j)

print(ans)