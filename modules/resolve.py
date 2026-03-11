import dns.resolver
import socket


# MX lookup
def mx_lookup(host_list, debug):
    for host in host_list:
        try:
            for result in dns.resolver.resolve(host, 'MX'):
                print("[+] " + host + ": " + result.to_text())
        except dns.resolver.NoAnswer:
            print("[-] " + host + ": " + "No MX record discovered")
        except dns.resolver.NXDOMAIN:
            print("[-] " + host + ": " + "Domain does not exist")
        except dns.resolver.NoNameservers as e:
            if debug:
                print("[-] " + host + ": " + "Nameserver error, " + str(e))
            else:
                print("[-] " + host + ": " + "Nameserver error")
        except Exception as e:
            if debug:
                print("[-] " + host + ": " + "Error, " + str(e))
            else:
                print("[-] " + host + ": " + "Error resolving" )
            pass


# DNS lookup
def resolve_hostname(host_list):
    for host in host_list:
        try:
            ip = socket.gethostbyname(host)
            print("[+] " + host + ": " + ip)
        except socket.error:
            print("[-] " + host + ": " + "No A record discovered")
        except Exception as e:
            print("[-] " + host + ": " + "Error: " + str(e))
            pass


# Reverse lookup
def reverse_lookup(ip_list):
    for ip in ip_list:
        try:
            hostname = socket.gethostbyaddr(ip)
            print("[+] " + str(ip) + ": " + str(hostname[0]))
        except socket.error:
            print("[-] " + ip + ": " + "No hostname record discovered")
        except Exception as e:
            print("[-] " + ip + ": " + "Error: " + str(e))
            pass
