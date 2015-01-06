import argparse
import curl
import resolve


def banner():
    print "#################################"
    print "##     python network tools    ##"
    print "#################################"


def usage():
    print "How to use python network tools:"
    print "--curl        - curl with pycurl lib"
    print "--urllib_curl - curl with urllib2 lib"

    print "examples:"
    print "curl.py --curl www.website.com"
    print "curl.py --urllib_curl http:\\website.com"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Python Network Tools')
    parser.add_argument('-c', help='Curl a provided URL with pycurl')
    parser.add_argument('--urllibcurl', help='Curl a provided url with urllib')
    args = parser.parse_args()
    if args.c:
        result = curl.curl(args.c)
        print result
    if args.urllibcurl:
        result = curl.urllib_curl(args.urllibcurl)
        print result
