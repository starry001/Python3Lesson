'''
urllib的request模块可以非常方便地抓取URL内容，也就是发送一个GET请求到指定的页面，然后返回HTTP的响应：
例如，对豆瓣的一个URLhttps://api.douban.com/v2/book/2129650进行抓取，并返回响应：
'''

from urllib import request, parse

with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data = f.read()
    print('status :', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('data:', data.decode('utf-8'))

'''
output:
status : 200 OK
Date: Sat, 04 Jun 2016 14:27:44 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 2055
Connection: close
Vary: Accept-Encoding
Expires: Sun, 1 Jan 2006 01:00:00 GMT
Pragma: no-cache
Cache-Control: must-revalidate, no-cache, private
Set-Cookie: bid=kKui6YFaUKc; Expires=Sun, 04-Jun-17 14:27:44 GMT; Domain=.douban.com; Path=/
X-DOUBAN-NEWBID: kKui6YFaUKc
X-DAE-Node: dis15
X-DAE-App: book
Server: dae
data: {"rating":{"max":10,"numRaters":16,"average":"7.4","min":0},"subtitle":"","author":["廖雪峰编著"],"pubdate":"2007-6","tags":[
'''

# 如果我们要想模拟浏览器发送GET请求，就需要使用Request对象，
# 通过往Request对象添加HTTP头，我们就可以把请求伪装成浏览器。
# 例如，模拟iPhone 6去请求豆瓣首页：

print('------模拟iPhone 6请求豆瓣首页-----')
req = request.Request('http://www.douban.com/')
req.add_header('User-Agent', 'Mozilla/6.0 '
                             '(iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) '
                             'Version/8.0 Mobile/10A5376e Safari/8536.25')

with request.urlopen(req) as  f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))

'''
如果要以POST发送一个请求，只需要把参数data以bytes形式传入。
我们模拟一个微博登录，先读取登录的邮箱和口令，然后按照weibo.cn的登录页的格式以username=xxx&password=xxx的编码传入
'''

print('------模拟post请求-----')
print('Login to weibo.cn...')
email = input('Email: ')
passwd = input('Password: ')
login_data = parse.urlencode([('username', email),
                              ('password', passwd),
                              ('entry', 'mweibo'),
                              ('client_id', ''),
                              ('savestate', '1'),
                              ('ec', ''),
                              ('pagerefer',
                               'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')])
req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent',
               'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer',
               'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')
with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    resp = f.read()
    print('status:', f.status, f.reason)
    for k, v in f.getheaders():
        print(k, v)
    print(resp.decode('utf-8'))

