# 典型90問067
# https://atcoder.jp/contests/typical90/tasks/typical90_bo

n, k = map(int, input().split())

def base_convert(nl, ibase, obase):
    o = []
    while any(nl):
        c = 0
        for i in range(len(nl)):
            c = c * ibase + nl[i]
            nl[i],c = divmod(c,obase)
        o.append(c)
    o.reverse()
    return o

# nを配列表記
n = list(str(n))
n = list(map(int, n))

for i in range(k):
    # nを9進数に変換
    n = base_convert(n, 8, 9)
    # 8を5におきかえ
    n = list(map(lambda x:5 if x==8 else x, n))
    # 先頭に0がでてきたら排除
    if not(n):
        n.append(0)
    while n[0]==0 and len(n)>1:
        n.pop(0)

# 配列をマージして8進法として出力
n = list(map(str, n))
n = "".join(n)
n = int(n)
print(n)