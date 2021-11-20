import requests
import threading
import sys

# requires: requests
# install: python3 -m pip install requests

usage = "usage: servercheck.py <http://url> <ports>"


def banner():
    print("+---------------------------------+")
    print("|         Web Server Check        |")
    print("+---------------------------------+")
    print("")


def http_check(url, i):
    try:
        site = url + ":" + str(i) + "/"
        s = requests.get(site, timeout=2)
        print("[+] " + site + " " + "Server: " + str(s.headers['server']) + " " + str(s.status_code))
    except Exception as e:
        pass


def start(url, r):
    for i in r:
        t = threading.Thread(target=http_check, args=(url, i))
        t.start()


def main():
    if len(sys.argv) == 3:
        ports = int(sys.argv[2])
        url = str(sys.argv[1])
        r = range(ports)
        banner()
        print("Starting server check...")
        start(url, r)
    else:
        print(usage)


if __name__ == "__main__":
    main()
