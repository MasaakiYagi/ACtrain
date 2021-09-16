# 典型90問069
# https://atcoder.jp/contests/typical90/tasks/typical90_bq

n, k = list(map(int, input().split()))

# 繰り返し二乗法
def modpow(a: int, p: int, mod: int) -> int:
    # return a**p (mod MOD) O(log p)
    if p == 0:
        return 1
    if p % 2 == 0:
        half = modpow(a, p//2, mod)
        return half*half % mod
    else:
        return a * modpow(a, p-1, mod) % mod

if n == 1:
    print(k%(10**9+7))
elif n == 2:
    print(k*(k-1)%(10**9+7))
else:
    # k*(k-1)*(k-2)^(n-2)が答え
    # 繰り返し二乗法で高速計算する
    print(k*(k-1)*modpow(k-2, n-2, 10**9+7)%(10**9+7))