import pycurl
from StringIO import StringIO
import urllib2

def curl(website):
    buffer = StringIO()
    c = pycurl.Curl()
    c.setopt(c.URL, website)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()
    body = buffer.getvalue()
    print(body)

def urllib_curl(website):
    body = urllib2.urlopen(website)
    print body.read()
