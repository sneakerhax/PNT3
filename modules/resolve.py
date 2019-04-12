import dns.resolver
import socket


# MX lookup
def mx_lookup(host_list):
    for host in host_list:
        try:
            for result in dns.resolver.query(host, 'MX'):
                print("[+] " + host + ": " + result.to_text())
        except:
            print("[-] " + host + ": " + "Unable to resolve")


# DNS lookup
def resolve_hostname(host_list):
    for host in host_list:
        try:
            ip = socket.gethostbyname(host)
            print("[+] " + host + ": " + ip)
        except socket.error:
            print("[-] " + host + ": " + "Unable to resolve")


# Reverse lookup
def reverse_lookup(ip_list):
    for ip in ip_list:
        try:
            hostname = socket.gethostbyaddr(ip)
            print("[+] " + str(ip) + ": " + str(hostname[0]))
        except socket.error:
            print("[-] " + ip + ": " + "Unable to resolve")
