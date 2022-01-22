heros = ['蜘蛛侠', '绿巨人', '黑寡妇', '鹰眼', '灭霸', '雷神']
heros[heros.index("黑寡妇")] = "神奇女侠"
print(heros)

heros = ['蜘蛛侠', '绿巨人', '黑寡妇', '鹰眼', '灭霸', '雷神']
heros[:2] = ["猪猪侠",  "女巨人"]
print(heros)

s = [1, 2, 3, 4, 5]
s[1:2] = [6, 6]
print(s)
