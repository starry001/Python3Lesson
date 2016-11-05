from bs4 import BeautifulSoup
import re

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

# 将本地 index.html 文件打开，用它来创建 soup 对象
soup = BeautifulSoup(html, 'html.parser')
# 打印一下 soup 对象的内容，格式化输出
# print(soup.prettify())

# 找的是在所有内容中的第一个符合要求的标签
print(soup.head)
print(soup.title)
print(soup.body)

print(soup.a)
print(type(soup.a))  # 对于 Tag，有两个重要的属性，是 name 和 attrs
print(soup.p)

print(soup.name)
print(soup.head.name)
print(soup.a.attrs)
print(soup.p.attrs)

print(soup.p.get('class'))  # 等价于 soup.p.['class']
soup.p['class'] = 'title2'  # 更改属性
print(soup.p.get('class'))

# 获取标签内部的文字
print(type(soup.p.string))
# Comment 对象是一个特殊类型的 NavigableString 对象，其实输出的内容仍然不包括注释符号，但是如果不好好处理它，可能会对我们的文本处理造成意想不到的麻烦。
print(type(soup.a.string))

print(soup.p.string)

print(soup.name)
# [document]
print(soup.attrs)
# {} 空字典

print(soup.head.contents)  # [<title>The Dormouse's story</title>]
print(soup.head.contents[0])  # <title>The Dormouse's story</title>

print(soup.head.children)  # list 生成器对象
for child in soup.body.children:
    print('child:', child)


#.contents 和 .children 属性仅包含tag的直接子节点，.descendants 属性可以对所有tag的子孙节点进行递归循环
for child in soup.body.descendants:
    print(child)

print('--------------- line -----------------\n')
for string in soup.stripped_strings:
    print(repr(string))

print('--------------- line -----------------\n')
for tag in soup.find_all(re.compile('^b')):
    print(tag.name)