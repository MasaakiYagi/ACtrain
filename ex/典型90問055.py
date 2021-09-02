# 典型90問055
# https://atcoder.jp/contests/typical90/tasks/typical90_bc

n, p, q = list(map(int, input().split()))
a = list(map(int, input().split()))

# 順当に全探索(PyPy3は通るけどpythonはTLE)
count = 0
for i in range(n):
    for j in range(i):
        for k in range(j):
            for l in range(k):
                for m in range(l):
                    if a[i]%p*a[j]%p*a[k]%p*a[l]%p*a[m]%p==q:
                        count += 1

print(count)