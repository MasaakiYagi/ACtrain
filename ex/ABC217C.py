# ABC217-C
# https://atcoder.jp/contests/abc217/tasks/abc217_c

n = int(input())
p = list(map(int, input().split()))

q = [0]*n
for i in range(n):
    q[p[i]-1] = i+1

print(*q)