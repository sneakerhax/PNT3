import socket
import sys

usage = "usage: port scanner <url> <ports>"

def port_scanner(url,ports):	
	for port in ports:
		try:
			print "[+] Connecting to: " + url + " port:" + str(port) +" [+]"
			s = socket.socket()
			s.connect((url,int(port)))
			s.send('sneakerhax \n')
			banner = s.recv(1024)
			if banner:
				print "[+] Port " +str(port)+ " open [+] \n"+ banner
				s.close()
		except: pass
def main():
	if len(sys.argv) == 3:
		url = sys.argv[1]
		ports = sys.argv[2].split(",")
		port_scanner(url,ports)
	else:
		print usage
	
if __name__ == "__main__":
    main()