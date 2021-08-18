# EDPC-B
# https://atcoder.jp/contests/dp/tasks/dp_b

n, k = list(map(int, input().split()))
h = list(map(int, input().split()))

# DP
c = [0]*n #i番目にたどり着く最小コストを格納
for i in range(n):
    if i == 0:
        c[i] = 0
    else:
        # i-1~i-k もしくは i-1~0(i<k)までの候補を算出
        cand = []
        end = k if i>k else i
        for j in range(1,end+1,1):
            cand.append(c[i-j]+abs(h[i]-h[i-j]))
        # candの最小値がc[i]に入る
        c[i] = min(cand)

print(c[-1])
