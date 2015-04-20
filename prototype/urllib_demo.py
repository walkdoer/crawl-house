import urllib2

response = urllib2.urlopen("http://www.baidu.com")
print response.read()


req = urllib2.Request('http://www.examplexxxxx.com')
try:
    urllib2.urlopen(req)
except urllib2.URLError, e:
    print e.reason


req = urllib2.Request('http://blog.csdn.net/cqcre')
try:
    urllib2.urlopen(req)
except urllib2.HTTPError, e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reason
else:
    print "OK"


import cookielib
cookie = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
response = opener.open('http://www.baidu.com')
for item in cookie:
    print 'Name = '+item.name
    print 'Value = '+item.value

filename = 'cookie.txt'
cookie = cookielib.MozillaCookieJar(filename)
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
response = opener.open("http://www.baidu.com")
cookie.save(ignore_discard=True, ignore_expires=True)


cookie = cookielib.MozillaCookieJar()
# read cookie from file
cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
req = urllib2.Request("http://www.baidu.com")
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open(req)
html_doc = response.read()


import re

pattern = re.compile(r'\d+')
print re.findall(pattern,'one1two2three3four4')


from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc)
print(soup.prettify())
print 'title', soup.title
print soup.find_all('a')


for link in soup.find_all('a'):
    print(link.get('href'))

# print soup.head.contents


for child in soup.head.children:
    print child