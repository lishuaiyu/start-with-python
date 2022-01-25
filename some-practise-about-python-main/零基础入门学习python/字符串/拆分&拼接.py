# 作者：李帅宇    时间 : 2022/1/25

# 从左到右和从右到左分为三元组
"www.iloveFish.com".partition(".")
"www.iloveFish.com".rpartition(".")
# split(sep=None, maxsplit=-1)，第一个参数指定分隔符，第二个指定分割次数
'苟日新，日日新，又日新'.split()
'苟日新，日日新，又日新'.split('，')
'苟日新，日日新，又日新'.rsplit('，')
'苟日新，日日新，又日新'.split('，', 1)
'苟日新，日日新，又日新'.rsplit('，', 1)
'苟日新\n日日新\n又日新'.split('\n')
# splitlines()将字符串按行分割，用列表形式返回
'苟日新\n日日新\n又日新'.splitlines()
# join(iterable)
'.'.join(["www", "iloveFish", "com"])

