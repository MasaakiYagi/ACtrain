# ABC187-D
# https://atcoder.jp/contests/abc187/tasks/abc187_d

n = int(input())
p = [[] for _ in range(n)]

aokisigma = 0

for i in range(n):
    x, y = list(map(int, input().split()))
    p[i] = [x,y,2*x+y]
    aokisigma += x

p = sorted(p, key=lambda x:x[2])
ans = 0
i = 1
ans += p[-i][2]
while(aokisigma>=ans):
    i += 1
    ans += p[-i][2]
    

print(i)