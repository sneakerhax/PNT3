from bs4 import BeautifulSoup
import urllib.request

url = urllib.request.urlopen("http://www.useragentstring.com/pages/useragentstring.php?name=Internet+Explorer")
# html = url.read(url)

soup = BeautifulSoup(url, features="html.parser")

agents = soup.body.findAll('a')

for a in agents:
    print(a.text.strip())
