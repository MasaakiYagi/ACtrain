# 割り算の整数部分ほしいなら//
# bit_shiftなら
    # <<左シフト
    # >>右シフト
# list(map(int, input().split()))
# int(input())

# 再帰の回数上限撤廃（再帰使うならPythonで通そう）
# import sys
# sys.setrecursionlimit(10**8)


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
