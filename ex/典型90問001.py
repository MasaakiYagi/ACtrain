# 典型90問001
# https://atcoder.jp/contests/typical90/tasks/typical90_a

n, l = list(map(int, input().split()))
k = int(input())
a = list(map(int, input().split()))

# 解の候補は1~L→「全ての切れ端をx以上にすることは可能か」という判定で2分探索を行っていく
def check(x):
    count = 0
    cut = 0
    for i in range(n):
        if a[i]-cut >= x:
            # 左から走査し，xの長さを初めて超えたらカットする
            count += 1
            cut = a[i]
        
        if count == k:
            if l-cut >= x:
                # 全てx以上でk回カットできた
                return True
            else:
                # 最後の切れ端がxを下回った
                return False
    
    # cut数がkを下回った
    return False

left = -1
right = l+1
mid = (left+right)//2

while(right-left>1):
    if check(mid):
        # mid以上の切れ端を作れる場合
        left = mid
        mid = int((left+right)/2)
    else:
        # mid未満である場合
        right = mid
        mid = int((left+right)/2)

print(left)