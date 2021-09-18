# ABC219-C
# https://atcoder.jp/contests/abc219/tasks/abc219_c

x = list(input())
al = list("abcdefghijklmnopqrstuvwxyz")
n = int(input())
s = [input() for _ in range(n)]

dic =  {key: val for key, val in zip(x, al)}

# 新アルファベットから通常アルファベット表記に変換し，セットで辞書格納
names = {}
for i in s:
    gen = list(map(lambda v:dic[v], list(i)))
    gen = "".join(gen)
    names[i] = gen

# 通常アルファベット表記にてソート
names = sorted(names.items(), key=lambda x:x[1])

# ans
for i in names:
    print(i[0])