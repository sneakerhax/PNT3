from bulkwhois.shadowserver import BulkWhoisShadowserver
import whois
import sys
import time

# only does ip list

whois_list = sys.argv[1]
site_list = []

bulk_whois = BulkWhoisShadowserver()

with open(whois_list, 'r') as f:
    for line in f:
        site_list.append(line.rstrip('\n'))

records = bulk_whois.lookup_ips(site_list)

for record in records:
    print "[+] ip address: " + records[record]['ip'], "[+] org name: " + records[record]['org_name']
