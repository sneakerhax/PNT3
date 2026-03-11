import argparse
import modules.data as data
import modules.resolve as resolve
import modules.curl as curl
import modules.whois as whois

# Generate banner: https://patorjk.com/software/taag/#p=display&f=Slant&t=PNT3
def banner():
    print(r"""
    ____  _   _____________
   / __ \/ | / /_  __/__  /
  / /_/ /  |/ / / /   /_ < 
 / ____/ /|  / / /  ___/ / 
/_/   /_/ |_/ /_/  /____/                             
    
Python Network Tools
          
by: sneakerhax
""")


def main():
    banner()
    parser = argparse.ArgumentParser(description='Python Network Tools')
    parser.add_argument('--ucurl', action='store_true', help='Curl a provided URL with urllib must use http://')
    parser.add_argument('--mxlookup', action='store_true', help='Lookup MX record')
    parser.add_argument('--dnsresolve', action='store_true', help='resolve hostname')
    parser.add_argument('--dnsreverse', action='store_true', help='reverse lookup')
    parser.add_argument('--whois', action="store_true", help="whois lookup")
    parser.add_argument('--targets', required=True, help='file to open')
    parser.add_argument('--debug', action='store_true', help='Print debug information')
    args = parser.parse_args()

    if args.ucurl:
        host_list = data.make_list_file(args.targets)
        curl.urllib_curl(host_list)
    if args.mxlookup:
        host_list = data.make_list_file(args.targets,)
        resolve.mx_lookup(host_list, args.debug)
    if args.dnsresolve:
        host_list = data.make_list_file(args.targets)
        resolve.resolve_hostname(host_list)
    if args.dnsreverse:
        ip_list = data.make_list_file(args.targets)
        resolve.reverse_lookup(ip_list)
    if args.whois:
        host_list = data.make_list_file(args.targets)
        whois.get_whois_org(host_list)


if __name__ == "__main__":
    main()
