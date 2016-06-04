from  html.parser import HTMLParser
from html.entities import name2codepoint
from urllib import request


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('starttag:<%s>' % tag)

    def handle_endtag(self, tag):
        print('endtag:</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('startendtag:<%s/>' % tag)

    def handle_data(self, data):
        print("data:", data)

    def handle_comment(self, data):
        print('comment:<!--', data, '-->')

    def handle_entityref(self, name):
        print('entityref:&%s;' % name)

    def handle_charref(self, name):
        print('charref:&#%s;' % name)


'''
feed()方法可以多次调用，也就是不一定一次把整个HTML字符串都塞进去，可以一部分一部分塞进去。
特殊字符有两种，一种是英文表示的&nbsp;，一种是数字表示的&#1234;，这两种字符都可以通过Parser解析出来。
'''
parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')


def getHtml(url):
    req = request.Request(url)
    # req.add_header('User-Agent',
    # 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    with request.urlopen(req) as f:
        # print('Status:', f.status, f.reason)
        # for k, v in f.getheaders():
        #     print('%s: %s' % (k, v))
        return f.read().decode('utf-8')


class MyHTMLParser(HTMLParser):
    def __init__(self):
        super(MyHTMLParser, self).__init__()
        self.Events = {}
        self._tag = ''
        self._counter = 0

    def handle_starttag(self, tag, attrs):
        if tag == 'h3' and attrs and attrs[0][0] == 'class' and attrs[0][1] == 'event-title':
            self._tag = 'title'
            # print('<%s>' % attrs)
        if tag == 'time' and attrs and attrs[0][0] == 'datetime':
            self._tag = 'datetime'
            # print('<%s>' % attrs)
        if tag == 'span' and attrs and attrs[0][0] == 'class' and attrs[0][1] == 'event-location':
            self._tag = 'location'
            # print('<%s>' % attrs)

    def handle_data(self, data):
        if self._tag == 'title':
            self.Events[self._counter] = {'title': data.strip("\n")}
        if self._tag == 'datetime':
            self.Events[self._counter]['time'] = data.strip("\n")
        if self._tag == 'location':
            self.Events[self._counter]['location'] = data.strip("\n")
            self._counter += 1
        self._tag = ''

    def printEvents(self):
        for k in self.Events:
            print("title:%s  Time: %s  Loaction:%s" % (
                self.Events[k]['title'], self.Events[k]['time'], self.Events[k]['location']))



            # if __name__=='__main__':
            #     parser = MyHTMLParser()
            #     parser.feed(getHtml('https://www.python.org/events/python-events/'))
            #     parser.printEvents()
