# 作者：李帅宇    时间 : 2022/1/22
a=[[x, y] for x in range(10) if x % 2 == 0 for y in range(10) if y % 3 == 0]
print(a)
_ = []
for x in range(10):
    if x % 2 == 0:
        for y in range(10):
            if y % 3 == 0:
                _.append([x,y])
print(_)
print(("i love"))
