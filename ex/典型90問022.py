# 典型90問022
# https://atcoder.jp/contests/typical90/tasks/typical90_v

a, b, c = list(map(int, input().split()))

# 最大公約数を求める
# 最大公約数で除して1を引いた数が，その辺を切断すべき回数

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

gcd_abc = gcd(gcd(a,b),c)
n = [a//gcd_abc-1, b//gcd_abc-1, c//gcd_abc-1]
print(sum(n))