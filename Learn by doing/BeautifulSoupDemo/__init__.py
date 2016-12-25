# coding:utf-8

from bs4 import BeautifulSoup
import urllib.request, urllib.parse
import http.cookiejar

url = 'http://reeoo.com'
resp = urllib.request.urlopen(url, timeout=20)

content = resp.read()
# print(content)
soup = BeautifulSoup(content, 'html.parser')
tag = soup.title
print(tag)
print(tag.name)

tag = soup.article
print(tag['class'])
print(tag.attrs)

tag = soup.article.div.ul.li
print(tag)

try:
    req = urllib.request.urlopen('http://blog.csdn.net/cqcre')
except urllib.request.HTTPError as e:
    print(e.code)
    print(e.reason)

