# ABC210-C
# https://atcoder.jp/contests/abc210/tasks/abc210_c

n, k = list(map(int, input().split()))
c = list(map(int, input().split()))

# 愚直解で
ans = 0
for i in range(n-k+1):
    # i~i+k-1までの配列抜き出し
    c_p = c[i:i+k]
    # c_pにふくまれるキャンディの種類
    num_c = len(set(c_p))
    ans = max(ans,num_c)

print(ans)