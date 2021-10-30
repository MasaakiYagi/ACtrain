# ABC225-D
# https://atcoder.jp/contests/abc224/tasks/abc225_d

n, q = list(map(int, input().split()))

train = [{"prev":-1,"next":-1} for _ in range(n)]
for i in range(q):
    query = list(map(int, input().split()))
    if query[0]==1:
        # 連結のクエリ
        x, y = query[1], query[2]
        train[x-1]["next"] = y-1
        train[y-1]["prev"] = x-1
        
    elif query[0]==2:
        # 切断のクエリ
        x, y = query[1], query[2]
        train[x-1]["next"] = -1
        train[y-1]["prev"] = -1
        
    else:
        # 出力のクエリ
        x = query[1]
        
        # xの属するグループの先頭車両番号を探索
        now = x-1
        while(train[now]["prev"]>=0):
            now = train[now]["prev"]
        
        # headから最終車両までの車両番号をappend
        ans = [now+1]
        while(train[now]["next"]>=0):
            now = train[now]["next"]
            ans.append(now+1)
        print(len(ans),*ans)