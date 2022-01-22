s = input("请输入字符串：")

list = []

for c in s:
    if c == "(" or c == "[" or c == "{":
        list.append(c)
    else:
        if len(list) == 0:
            print("非法")
            break

        if c == ')':
            d = '('
        elif c == ']':
            d = '['
        elif c == '}':
            d = '{'
        
        if d != list.pop():
            print("非法T_T")
            break
else:
    if len(list) == 0:
        print("合法")
    else:
        print("非法")

