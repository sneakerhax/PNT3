import argparse
import curl
import resolve


def banner():
    print "#################################"
    print "##     python network tools    ##"
    print "#################################"


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Python Network Tools')
	parser.add_argument('-curl', help='Curl a provided URL with pycurl')
	parser.add_argument('-urllibcurl', help='Curl a provided url with urllib')
	parser.add_argument('-mx', help='Lookup MX record')
	args = parser.parse_args()

if args.curl:
	result = curl.curl(args.curl)
	print result
if args.urllibcurl:
	result = curl.urllib_curl(args.urllibcurl)
	print result
if args.mx:
	result = resolve.mx_lookup(args.mx)
	print result
