# EDPC-C
# https://atcoder.jp/contests/dp/tasks/dp_c

n = int(input())
h = []
for i in range(n):
    h.append(list(map(int, input().split())))

# DP
c = [[0]*3 for _ in range(n)]
for i in range(n):
    if i == 0:
        # 初日のアクションはそれぞれの通り
        c[i] = h[i]
    else:
        # i日目のそれぞれのアクションはi-1日目の総和に依存
        for j in range(3):
            c[i][j] = h[i][j] + max(c[i-1][(j+1)%3], c[i-1][(j+2)%3])

# 最終日のa or b or cの最大のものが答え
print(max(c[-1]))