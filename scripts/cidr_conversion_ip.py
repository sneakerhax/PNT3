from netaddr import IPNetwork
import sys

# requires: netaddr
# install: python3 -m pip install netaddr

usage = "usage: cidr_conversion_ip.py <target_list>"

cidr_list = []


def banner():
    print("#################################")
    print("#       cidr_conversion_ip.py   #")
    print("#        by: sneakerhax         #")
    print("#################################")
    print("")


def cidr_conversion_ip(target_list):
    with open(target_list, 'r') as f:
        for line in f:
            cidr = line.strip()
            cidr_list.append(cidr)

    with open("iplist.txt", 'w') as g:
        for subnet in cidr_list:
            for ip in IPNetwork(subnet):
                g.write(str(ip) + "\n")


def main():
    if len(sys.argv) == 2:
        try:
            target_list = sys.argv[1]
            banner()
            print("[+] Converting CIDR addresses to ip list")
            cidr_conversion_ip(target_list)
            print("[+] IP list written to iplist.txt")
        except Exception as e:
            print("[-] Error when converting list")
    else:
        print(usage)


if __name__ == "__main__":
    main()
