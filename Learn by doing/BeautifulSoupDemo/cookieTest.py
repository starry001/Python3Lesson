from http import cookiejar
from  urllib import request, parse

# get cookie
cookie = cookiejar.CookieJar()
handler = request.HTTPCookieProcessor(cookie)
opener = request.build_opener(handler)
response = opener.open('http://www.baidu.com')
for item in cookie:
    print('Name = ' + item.name)
    print('Value = ' + item.value)

# save cookie
fileName = 'cookie.txt'
cookie = cookiejar.MozillaCookieJar(fileName)
handler = request.HTTPCookieProcessor(cookie)
opener = request.build_opener(handler)
resp = opener.open('http://www.baidu.com')
# ignore_discard的意思是即使cookies将被丢弃也将它保存下来，
# ignore_expires的意思是如果在该文件中cookies已经存在，则覆盖原文件写入
cookie.save(ignore_discard=True, ignore_expires=True)

login_data = parse.urlencode([
    ('email', '763264652@qq.com'),
    ('password', 'wang790494292'),
]).encode('utf-8')
req = request.Request('http://www.imooc.com/',login_data)
respon = request.urlopen(req)
print(respon.status)

fileName = 'mooc_cookie.txt'
cookie = cookiejar.MozillaCookieJar(fileName)
handler = request.HTTPCookieProcessor(cookie)
opener = request.build_opener(handler)
r = opener.open(req)
cookie.save(ignore_discard=True, ignore_expires=True)

#利用cookie请求访问另一个网址，此网址是成绩查询网址
gradeUrl = 'http://www.imooc.com/u/2002116/courses'
#请求访问成绩查询网址
result = opener.open(gradeUrl)
print(result.read().decode('utf-8'))
