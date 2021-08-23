# ABC215-C
# https://atcoder.jp/contests/abc215/tasks/abc215_c

import itertools as it

s, k = input().split()
k = int(k)

sorted_s = sorted(s)
all_sorts = it.permutations(sorted_s)
all_sorts = list(all_sorts)
all_sorts = list(map(lambda v:"".join(v), all_sorts))
all_sorts = set(all_sorts)
all_sorts = list(sorted(all_sorts))
ans = all_sorts[k-1]
print(ans)