from hello import application
from wsgiref.simple_server import make_server

# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = make_server('', 8000, application)
print('start http on port 8000...')
# 开始监听
httpd.serve_forever()
