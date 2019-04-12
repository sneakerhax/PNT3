from netaddr import IPNetwork
import sys

# requires: netaddr
# install: pip3 install netaddr

ip_list = sys.argv[1]
cidr_list = []

with open(ip_list, 'r') as f:
    for line in f:
        cidr = line.strip()
        cidr_list.append(cidr)

with open("iplist.txt", 'w') as g:
    for subnet in cidr_list:
        for ip in IPNetwork(subnet):
            g.write(str(ip) + "\n")
