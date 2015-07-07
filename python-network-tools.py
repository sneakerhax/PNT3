import argparse
import curl
import resolve


def banner():
    print "#################################"
    print "##     python network tools    ##"
    print "#################################"

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Python Network Tools')
	parser.add_argument('--curl', help='Curl a provided URL with pycurl')
	parser.add_argument('--ucurl', help='Curl a provided URL with urllib must use http://')
	parser.add_argument('--mx', help='Lookup MX record')
	parser.add_argument('--dnsresolve', help='resolve hostname')
	parser.add_argument('--dnsreverse', help='reverse lookup')
	args = parser.parse_args()
	
banner()
if args.curl:
	result = curl.curl(args.curl)
	print result
if args.ucurl:
	result = curl.urllib_curl(args.ucurl)
	print result
if args.mx:
	result = resolve.mx_lookup(args.mx)
	print result
if args.dnsresolve:
	result = resolve.resolve_hostname(args.dnsresolve)
	print result
if args.dnsreverse:
	result = resolve.reverse_lookup(args.dnsreverse)
	print result
