# 典型90問069
# https://atcoder.jp/contests/typical90/tasks/typical90_bq

n, k = list(map(int, input().split()))

if n == 1:
    print(k)
elif n == 2:
    print(k*(k-1))
else:
    # k*(k-1)*(k-2)^(n-2)が答え
    # 繰り返し二乗法で高速計算する
    # https://math.nakaken88.com/textbook/cp-binary-exponentiation-and-recursive-function/