import sys
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
	banner()    
	if sys.argv[1] == "--curl":
		print "curling website..."
		curl.curl(sys.argv[2])
	elif sys.argv[1] == "--urllib_curl":
		print "curling website..."
		curl.urllib_curl(sys.argv[2])
	elif sys.argv[1] == "--mx":
		print "MX record:"
		resolve.mx_lookup(sys.argv[2])
	elif sys.argv[1] == "--help":
		usage()
	else:
		usage()