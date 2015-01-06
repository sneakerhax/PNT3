from dns import resolver
import sys

def mx_lookup(domain, *args):
	mx = resolver.query(sys.argv[2], 'MX')
	print mx[0]
	