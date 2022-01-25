# 作者：李帅宇    时间 : 2022/1/25

"    左侧要留白".lstrip()
"右侧要留白    ".rstrip()
"  左右都不留白  ".strip()
# lstrip(chars=None)
# rstrip(chars=None)
# strip(chars=None), 删除指定的元素,匹配单个字符
"www.iloveFish.com".lstrip("wcom.")
"www.iloveFish.com".rstrip("wcom.")
"www.iloveFish.com".strip("wcom.")

"www.iloveFish.com".removeprefix("www.")
"www.iloveFish.com".removesuffix("www.")