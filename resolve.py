from dns import resolver
import socket

def mx_lookup(domain):
	mx = resolver.query(domain, 'MX')
	for record in mx:
		print record
		
def resolve_hostname(hostname):
	host = socket.gethostbyname(hostname)
	print host