# from wsgiref.simple_server import make_server

def application(enversion, start_response):
    start_response('200 OK', [('Content-type', 'text/html')])
    # return [b'<h1>hello world</h1>']
    body = '<h1>hello,%s</h1>' % enversion['PATH_INFO'][1:] or 'web'
    return [body.encode('utf-8')]
