import dns
from dns import resolver
import sys

def mx_lookup(domain):
	mx = dns.resolver.query(sys.argv[2], 'MX')
	print mx[0]
	