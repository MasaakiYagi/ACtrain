# ABC214-C
# https://atcoder.jp/contests/abc214/tasks/abc214_c

N = int(input())
S = list(map(int,input().split()))
T = list(map(int,input().split()))

# i番目のすぬけが初めて宝石を貰うのは，高橋からの直わたしかi-1番目のすぬけからのパス
# 入力状態にて，すべて高橋から貰うパターンが最速である仮説となっている
# これを更新していく

for i in range(2*N):
    T[(i+1)%N] = min(T[(i+1)%N], T[i%N]+S[i%N])

for ans in T:
    print(ans)
