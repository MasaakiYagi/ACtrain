# 典型90問010
# https://atcoder.jp/contests/typical90/tasks/typical90_j

n = int(input())
ten = []
for i in range(n):
    ten.append(list(map(int, input().split())))
q = int(input())
lr = []
for i in range(q):
    lr.append(list(map(int, input().split())))

# 累積和リストを作成
cs1 = [0]*n
cs2 = [0]*n
for i in range(n):
    if i > 0:
        cs1[i] = cs1[i-1]
        cs2[i] = cs2[i-1]
    
    if ten[i][0] == 1:
        # 1組なら
        cs1[i] += ten[i][1]
    else:
        # 2組なら
        cs2[i] += ten[i][1]

# 累積和リストからans算出
for i in range(q):
    l = cs1[lr[i][1]-1] - cs1[lr[i][0]-2] if lr[i][0]>=2 else cs1[lr[i][1]-1]
    r = cs2[lr[i][1]-1] - cs2[lr[i][0]-2] if lr[i][0]>=2 else cs2[lr[i][1]-1]
    print(*[l,r])