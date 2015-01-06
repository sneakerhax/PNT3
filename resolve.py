from dns import resolver

def mx_lookup(domain, *args):
	mx = resolver.query(domain, 'MX')
	for record in mx:
		print record
	