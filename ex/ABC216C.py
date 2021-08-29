#ABC216C

n = int(input())

rev_s = []
now = n
i=0
while(1):
    if now%2==0:
        # 偶数のとき
        rev_s.append('B')
        now = int(now/2)
    elif now%2==1:
        # 奇数のとき
        rev_s.append('A')
        now = now-1
    i += 1
    if now == 0:
        # 0になったら終わり
        break
    if now<=(120-i):
        for j in range(120-i):
            rev_s.append('A')
        break

s = reversed(rev_s)
print("".join(s))





