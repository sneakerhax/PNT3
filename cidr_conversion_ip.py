from netaddr import IPNetwork
import sys

ip_list = sys.argv[1]
cidr_list = []

with open(ip_list, 'r') as f:
    for line in f:
        cidr = line.strip()
        cidr_list.append(cidr)

with open("iplist.txt", 'wb') as g:
    for subnet in cidr_list:
        for ip in IPNetwork(subnet):
            g.write(str(ip) + "\n")
