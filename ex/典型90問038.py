# 典型90問038
# https://atcoder.jp/contests/typical90/tasks/typical90_al

a, b = list(map(int, input().split()))

# 最大公約数
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

d = gcd(a,b)

ans = a*b//d if a*b//d<=10**18 else 'Large'
print(ans)
