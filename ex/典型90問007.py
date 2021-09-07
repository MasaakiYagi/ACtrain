# 典型90問007
# https://atcoder.jp/contests/typical90/tasks/typical90_g

n = int(input())
a = list(map(int, input().split()))
q = int(input())
b=[int(input()) for _ in range(q)]

def is_ok(mid, ten):
    return (a[mid] - ten) > 0


def meguru_bisect(ng, ok, ten):
    '''
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    '''
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid, ten):
            ok = mid
        else:
            ng = mid
    if abs(a[ok]-ten)<=abs(a[ng]-ten):
        return ok
    else:
        return ng

# aを昇順ソート
a = sorted(a)

# 1人不満度の最小値を出す
for i in b:
    if a[0] >= i:
        # どのクラスよりもレートが低いならば
        print(abs(a[0]-i))
    elif a[-1] <= i:
        # どのクラスよりもレートが高いならば
        print(abs(a[-1]-i))
    else:
        # 用意されたクラス内にレートがあるならば，二分探索する
        c = meguru_bisect(-1, len(a), i)
        print(abs(a[c]-i))