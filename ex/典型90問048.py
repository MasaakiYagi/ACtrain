# 典型90問048
# https://atcoder.jp/contests/typical90/tasks/typical90_av


n, k = list(map(int, input().split()))
a = [0]*n
b = [0]*n
for i in range(n):
    a[i], b[i] = list(map(int, input().split()))

# bi>(ai-bi)が保障されるため，biとai-biを全て配列に格納し，大きい順にK個選べばいい
ab = [x - y for (x, y) in zip(a, b)]
b.extend(ab)
b = sorted(b)
print(sum(b[-k:]))