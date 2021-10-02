# ABC221-D
# https://atcoder.jp/contests/abc221/tasks/abc221_d

n=int(input())
days = []
for _ in range(n):
    a,b = list(map(int, input().split()))
    days.append([a,1])
    days.append([a+b,-1])

days.sort()

ans = [0]*(n+2)
s = days[0][0]
num = 1

for d in days:
    ans[num] += d[0]-s
    if d[1]==1:
        num += 1
    else:
        num -= 1
    s = d[0]

print(*ans[2:])