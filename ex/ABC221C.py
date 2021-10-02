# ABC221-C
# https://atcoder.jp/contests/abc221/tasks/abc221_c

import itertools
import math

n=int(input())

n = list(str(n))
keta = len(n)
keta2 = math.ceil(keta/2)
ns = list(itertools.permutations(n,len(n)))

ans = []
for p in ns:
    for j in range(1,keta2+1):
        num1 = p[0:j]
        num2 = p[j:]
        if not(num1[0] == '0' or num2[0] == '0'):
            num1=int("".join(num1))
            num2=int("".join(num2))
            ans.append(num1*num2)
print(max(ans))