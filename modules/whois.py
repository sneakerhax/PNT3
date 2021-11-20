import whois as whois2


def get_whois_org(host_list):
    for host in host_list:
        try:
            w = whois2.whois(host)
            print("[+] Whois data for " + str(host) + ":")
            print("Org: " + w.org)
            print("Country: " + w.country)
        except Exception as e:
            print("[-] Unable to retrieve whois data for " + str(host))
            pass
