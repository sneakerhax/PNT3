from dns import resolver
import socket

#MX lookup
def mx_lookup(domain):
	mx = resolver.query(domain, 'MX')
	for record in mx:
		print record
		
#DNS lookup		
def resolve_hostname(hostname):
	ip = socket.gethostbyname(hostname)
	return ip
	
#Reverse lookup
def reverse_lookup(ip):
	hostname = socket.gethostbyaddr(ip)
	return hostname[0]
