from bs4 import BeautifulSoup
import urllib.request
import sys

# Requires BeautifulSoup, requests
# install: python3 -m pip install beautifulsoup4 requests

chrome_url = "https://www.useragentstring.com/pages/useragentstring.php?name=chrome"
firefox_url = "https://www.useragentstring.com/pages/useragentstring.php?name=firefox"
ie_url = "http://www.useragentstring.com/pages/useragentstring.php?name=Internet+Explorer"

usage = """usage: user_agents.py <user_agent_type>

available agent lists:
* chrome
* firefox
* ie (Internet Explorer)
"""


def banner():
    print("#################################")
    print("#       user_agents.py          #")
    print("#       by: sneakerhax          #")
    print("#################################")
    print("")


def user_agents(url):
    req = urllib.request.Request(
        url,
        data=None,
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        }
    )

    url = urllib.request.urlopen(req)
    soup = BeautifulSoup(url, features="html.parser")
    agents = soup.body.findAll('a')

    for a in agents:
        agent_string = "/"
        agent_string_page = a.text.strip().splitlines()
        for agent in agent_string_page:
            if agent_string in agent:
                print(agent)
            else:
                pass


def main():
    if len(sys.argv) == 2:
        try:
            agent_type = sys.argv[1]
            banner()
            print("[+] Downloading user agent list:")
            if agent_type == "ie":
                user_agents(ie_url)
            if agent_type == "firefox":
                user_agents(firefox_url)
            if agent_type == "chrome":
                user_agents(chrome_url)
        except Exception as e:
            print("[-] Error getting user agent list")
    else:
        print(usage)


if __name__ == "__main__":
    main()
