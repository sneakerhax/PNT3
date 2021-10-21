import whois
import sys
import time

# only does hostnames
# requires: whois
# install: pip3 install whois

whois_list = sys.argv[1]
site_list = []

with open(whois_list, 'r') as f:
    for line in f:
        site_list.append(line.rstrip('\n'))

for site in site_list:
    who = whois.query(site)
    if who:
        print("name: " + who.name + " " + "registar: " + who.registrar)
        print("--------------------------------------------------------------")
        time.sleep(3)
