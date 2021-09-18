# 典型90問075
# https://atcoder.jp/contests/typical90/tasks/typical90_bw

n = int(input())

# 素因数分解し，素因数の数を超える最小の2^pとなるときのpが答え

# まず素因数分解する
def factorization(n):
    arr = []
    temp = n
    count = 0
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])
            count += cnt

    if temp!=1:
        arr.append([temp, 1])
        count += 1

    if arr==[]:
        arr.append([n, 1])
        count += 1

    return count

n_facts = factorization(n)
n_facts = list(bin(n_facts))[2:]
n_facts = list(map(int, n_facts))
if sum(n_facts)==1:
    print(len(n_facts)-1)
else:
    print(len(n_facts))