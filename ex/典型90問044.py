# 典型90問044
# https://atcoder.jp/contests/typical90/tasks/typical90_ar

from collections import deque

n, q = list(map(int, input().split()))
a = list(map(int, input().split()))
t = [list(map(int, input().split())) for _ in range(q)]

a = deque(a)
shift = 0

# シフトは添え字操作で表現する
def cor(x):
    return x-shift

for i in t:
    if i[0]==1:
        # swap
        temp = a[cor(i[1])-1]
        a[cor(i[1])-1] = a[cor(i[2])-1]
        a[cor(i[2])-1] = temp
    elif i[0]==2:
        # shift
        shift += 1
        if shift==n:
            shift=0
    else:
        # output
        print(a[cor(i[1])-1])