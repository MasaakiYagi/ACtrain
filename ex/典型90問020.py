# 典型90問020
# https://atcoder.jp/contests/typical90/tasks/typical90_t

a, b, c = list(map(int, input().split()))

bc = 1
for _ in range(b):
    bc = bc*c

if a<bc:
    print("Yes")
else:
    print("No")
