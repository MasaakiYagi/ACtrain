# ABC215-D
# https://atcoder.jp/contests/abc215/tasks/abc215_d

n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
maxa = max(max(a),m)

k = [True]*(maxa+1)  # iが条件を満たすか．初期True
isprime = [True]*(maxa+1)  # iが素数かどうか
aprime = []  # Aに含まれる素因数

# aの要素はFalseに
for ae in a:
    k[ae] = False

# エラトステネスで素数の数え上げ．このとき，aの要素の素因数かどうかも調べる
for i in range(2,maxa+1):
    if not isprime[i]:
        continue
    
    for j in range(i*2,maxa+1,i):
        isprime[j] = False
        k[i] = k[i] and k[j]
        
    if not k[i]:
        # iの倍数にAの要素が1つ以上現れた＝iは使えない素因数
        aprime.append(i)

# aprimeの倍数をすべてk-Falseにする
for p in aprime:
    for j in range(p*2,m+1,p):
        k[j] = k[p] and k[j]

ans = [1]
for i in range(2,m+1):
    if k[i]:
        ans.append(i)

print(len(ans))
for i in ans:
    print(i)